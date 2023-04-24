from machine import Pin,PWM,ADC
import time

_CAMERA_DBG_ = True
Red_Button_Pressed = 1
if_focused = False
de_bounce_time = 1
de_bounce_count = 10
adc_de_bonuce_count = 50
# Code Start at "#End of Config"

# Config Output Pins <See Pins.xls>
shutter_pin = 9
apture_pin = 17
motor_pin = 5
LED_Y_PIN = 12
LED_B_PIN = 13
# End Config Output

# Config Input Pins <See Pins.xls>
S1F_PIN = 2 # Sw 1 Focus
S1T_PIN = 1 # Sw 1 Take Photo
S1F_FBW_PIN = 22
S3_PIN = 7
S3_PIN = 7
S5_PIN = 6
ADC_STAGE1_PIN = 27
ADC_STAGE2_PIN = 28
# End Config Input Pins

# Config ShutterDelay  sht(1/n) or sht(n)s
sht4s = 4000
sht3s = 3000
sht2s = 2000
sht1s = 1000
sht2 = 600
#ev75 = 440
sht4 = 280
sht6 =210
sht8 = 155
sht10 =120
sht15 = 97
sht20 = 70
sht30 = 48
#ev115 = 40
sht60 = 33
#ev125 = 29
sht125 = 25
#ev135 = 23
sht250 = 21
#ev145 = 20
sht500 = 19
sht1000 = 18
# End Config ShutterDelay

#End of Config

# Inital camera
def camera_init():
    global motor,shutter,apture,LED_Y,LED_B,s3,s5,s1t,s1f,S1F_FBW,ADC0,ADC1,iso
    shutter = PWM(Pin(shutter_pin))
    shutter.freq(20000)
    shutter.duty_u16(0)
    apture = PWM(Pin(apture_pin))
    apture.freq(70000)
    apture.duty_u16(0)
    
    motor = Pin(motor_pin,Pin.OUT, value=0)
    LED_Y = Pin(LED_Y_PIN, Pin.OUT,value = 1)
    LED_B = Pin(LED_B_PIN, Pin.OUT,value = 1)	
    S1F_FBW = Pin(S1F_FBW_PIN, Pin.OUT,value = 0)
    
    s3 = Pin(S3_PIN,Pin.IN,Pin.PULL_UP)
    s5 = Pin(S5_PIN,Pin.IN,Pin.PULL_UP)
    s1f = Pin(S1F_PIN,Pin.IN)
    s1t = Pin(S1T_PIN,Pin.IN)
    
    ADC0 = ADC(Pin(ADC_STAGE1_PIN))  # 通过GPIO27初始化ADC
    ADC1 = ADC(Pin(ADC_STAGE2_PIN))  # 通过GPIO28初始化ADC
    
    f = open('./dat/iso.txt')
    iso = f.readline()
    iso.replace(" ","")
    f.close()
    if _CAMERA_DBG_:
        print("ISO at %s!"%iso)
    if iso == '600':
        LED_Y.value(0)
    else:
        LED_B.value(0)

def close_led():
    LED_Y.value(1)
    LED_B.value(1)
    
def led_iso():
    if iso == '600':
        LED_B.value(0)
    else:
        LED_Y.value(0)

def de_bounce_read_pins(pin_list):
    global de_bounce_time,de_bounce_count
    pin_value = [0]*len(pin_list)
    for i in range(de_bounce_count):
        for j in range(len(pin_list)):
            pin_value[j] += pin_list[j].value()
        time.sleep_ms(de_bounce_time)
    for i in range(len(pin_value)):
        pin_value[i] = round(pin_value[i]/de_bounce_count)
        if i >1:
            i = 1
    return pin_value

def apture_engage():
    apture.duty_u16(32700)
    
def apture_disengage():
    apture.duty_u16(0)

def meter():
    read_voltage0 = 0
    read_voltage1 = 0
    for i in range(adc_de_bonuce_count):
        read_voltage0 += ADC0.read_u16()*3300/65535   # 读取ADC通道0的数值并根据ADC电压计算公式得到GPIO26引脚上的电压
        read_voltage1 += ADC1.read_u16()*3300/65535   # 读取ADC通道0的数值并根据ADC电压计算公式得到GPIO26引脚上的电压
        time.sleep_ms(1)
    read_voltage0 = read_voltage0/adc_de_bonuce_count
    read_voltage1 = read_voltage1/adc_de_bonuce_count
    if _CAMERA_DBG_:
        print("1st stage voltage = {0:.2f}mV \t\t  2nd stage voltage = {1:.2f}mV \t\t".format(read_voltage0, read_voltage1))

def shut(Shutter_Delay, f="1"):
    if _CAMERA_DBG_:
        print("Taking Picture")
    if _CAMERA_DBG_:
        print("Shutter start to close!")
    shutter.duty_u16(65535)
    time.sleep_ms(18)
    shutter.duty_u16(10000)
    motor.value(1)
    if _CAMERA_DBG_:
        print("Motor Start Moving")
    while True:
        if s3.value() == 1:
            motor.value(0)
            if _CAMERA_DBG_:
                print("Motor Stoped!")
            break
        
    if f=='0': #Engage apture
        apture_engage() 
    time.sleep_ms(18) # Y delay
    
    shutter.duty_u16(0) #open shutter
    if _CAMERA_DBG_:
        print("Shutter Start to Open, Exposure Starts")

    # Start Exposure
    if f == '0':
        if _CAMERA_DBG_:
            print("Flash Mode!")
        gap=int(Shutter_Delay*0.3)
        time.sleep_ms(gap)
        fl.value(1)
        time.sleep_ms(gap)
        fl.value(0)
        apture_disengage() # Apture goes back
        time.sleep_ms(gap)
    elif f == '1':
        time.sleep_ms(Shutter_Delay)
    elif f == 'B':
        time.sleep_ms(15)
        while True:
            time.sleep_ms(3)
            if btn.value() == 1:
                break
    elif f == 'T':
        time.sleep(100)
        while True:
            time.sleep(3)
            if btn.value() == 0:
                break
    # End Exposure
    
    shutter.duty_u16(65535) # Close Shutter
    if _CAMERA_DBG_:
        print("Shutter Closing!")
    time.sleep_ms(20)
    shutter.duty_u16(10000) # Keep Shutter Closed
    if _CAMERA_DBG_:
        print("Shutter Closd. Exposure Finished")
    
    motor.value(1)
    if _CAMERA_DBG_:
        print("Motor Working!")
    while True:
        if s5.value() == 0:
            motor.value(0)
            shutter.duty_u16(0)
            break
        

def test_cam():
    time.sleep_ms(3800)
    LED_Y.value(1)
    shutter.duty_u16(65535)
    time.sleep_ms(3800)
    shutter.duty_u16(0)
    motor.value(1)
    LED_Y.value(0)
    
def test_cam1():
    global if_focused, CAMERA_DBG
    while True:
        dbpv = de_bounce_read_pins([s1f,s1t])
        foc = dbpv[0]
        tak = dbpv[1]
        if foc == Red_Button_Pressed and if_focused == False:
            S1F_FBW.value(1);
            if_focused = True
            print("Focusing!")
            if _CAMERA_DBG_:
                print(dbpv)
        if foc != Red_Button_Pressed and if_focused == True:
            S1F_FBW.value(0);
            if_focused = False
            print("Stop Focus")
            if _CAMERA_DBG_:
                print(dbpv)
        if tak == Red_Button_Pressed:
            meter()
            LED_Y.value(1)
            LED_B.value(1)
            shut(1000);
            print("Taken!")
            led_iso()
            
            if _CAMERA_DBG_:
                print(dbpv)
            #return
    
if __name__ == "__main__":
    camera_init()
    #test_cam()
    #shut(1000)
    test_cam1()