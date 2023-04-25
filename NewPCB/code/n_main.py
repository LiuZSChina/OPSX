from machine import Pin,PWM,ADC
import time

_CAMERA_DBG_ = True
Red_Button_Pressed = 1
if_focused = False
de_bounce_time = 1
de_bounce_count = 10
adc_de_bonuce_count = 70
# Code Start at "#End of Config"

# Config Output Pins <See Pins.xls>
shutter_pin = 9
apture_pin = 17
motor_pin = 5
LED_Y_PIN = 12
LED_B_PIN = 13
S1F_FBW_PIN = 22
# End Config Output

# Config Input Pins <See Pins.xls>
S1F_PIN = 2 # Sw 1 Focus
S1T_PIN = 1 # Sw 1 Take Photo
S3_PIN = 7
S5_PIN = 6
ADC_STAGE1_PIN = 27
ADC_STAGE2_PIN = 28
# End Config Input Pins

# Config ShutterDelay  sht(1/n) or sht(n)s
sht4s = 4000
sht3s = 3000
sht2s = 2000
sht1s = 1000 # EV6
sht2 = 600 #EV7
sht3 = 440 #EV7.5	
sht4 = 280 #EV8
sht6 =210 #EV8.5
sht8 = 155 #EV9
sht10 =120 #EV9.5
sht15 = 97 #EV10
sht20 = 70 #EV10.5
sht30 = 48 #EV11
sht45 = 40 #EV11.5
sht60 = 33 #EV12
sht90 = 29 #EV12.5
sht125 = 25 #EV13
sht180 = 23 #EV13.5
sht250 = 21 #EV14
sht360 = 20 #EV14.5
sht500 = 19 #EV15
sht1000 = 18 #EV16
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
    
    ADC0 = ADC(Pin(ADC_STAGE1_PIN))  # 初始化ADC
    ADC1 = ADC(Pin(ADC_STAGE2_PIN))  # 初始化ADC
    
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
        LED_Y.value(0)
    else:
        LED_B.value(0)

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
        read_voltage0 += ADC0.read_u16()*3000/65535   # 读取ADC通道0的数值并根据ADC电压计算公式得到GPIO26引脚上的电压
        read_voltage1 += ADC1.read_u16()*3000/65535   # 读取ADC通道0的数值并根据ADC电压计算公式得到GPIO26引脚上的电压
        time.sleep_ms(1)
    read_voltage0 = read_voltage0/adc_de_bonuce_count
    read_voltage1 = read_voltage1/adc_de_bonuce_count
    if _CAMERA_DBG_:
        print("1st stage voltage = {0:.2f}mV \t\t  2nd stage voltage = {1:.2f}mV \t\t".format(read_voltage0, read_voltage1))
    
    if read_voltage1 <=2700: #Stage2 Working
        if read_voltage1 >=1875:
            return sht360
        if read_voltage1 >=1175:
            return sht250
        if read_voltage1 >=788:
            return sht180
        if read_voltage1 >=543:
            return sht125
        if read_voltage1 >=382:
            return sht90
        if read_voltage1 >=273:
            return sht60
        if read_voltage1 >=210:
            return sht45
        if read_voltage1 >=145:
            return sht30
        if read_voltage1 >=109:
            return sht20
        if read_voltage1 >=84:
            return sht15
        if read_voltage1 >=66:
            return sht10
        if read_voltage1 >=53:
            return sht8
        if read_voltage1 >=44.5:
            return sht6
        if read_voltage1 >=38.5:
            return sht4
        if read_voltage1 >=34:
            return sht3
        if read_voltage1 >=29.5:
            return sht2
        else:
            return sht1s
    else: # Stage1
        if read_voltage0>54.85:
            return sht1000
        if read_voltage0>41.5:
            return sht500
        else:
            return sht360
        
        
    

def shut(Shutter_Delay, f="1"):
    if _CAMERA_DBG_:
        print("Taking Picture")
    if _CAMERA_DBG_:
        print("Shutter start to close!")
    shutter.duty_u16(65535)
    time.sleep_ms(30)
    shutter.duty_u16(30000)
    #time.sleep_ms(30)
    time.sleep_ms(3000)
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
    time.sleep_ms(30)
    shutter.duty_u16(30000) # Keep Shutter Closed
    if _CAMERA_DBG_:
        print("Shutter Closd. Exposure Finished")
    time.sleep_ms(18)
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
            #S1F_FBW.value(1);
            St = meter()
            if_focused = True
            print("Focusing!")
            if _CAMERA_DBG_:
                print(dbpv)
        if foc != Red_Button_Pressed and if_focused == True:
            #S1F_FBW.value(0);
            if_focused = False
            print("Stop Focus")
            if _CAMERA_DBG_:
                print(dbpv)
        if tak == Red_Button_Pressed:
            #meter()
            LED_Y.value(1)
            LED_B.value(1)
            print("EXP Time:",str(St))
            shut(St);
            print("Taken!")
            led_iso()
            
            if _CAMERA_DBG_:
                print(dbpv)
            #return
    
if __name__ == "__main__":
    camera_init()
    #test_cam()
    #shut(1000)
    #test_cam1()
    while True:
        #meter()
        #time.sleep_ms(1000)
        test_cam1()
        #time.sleep_ms(2000)
        #shut(meter())