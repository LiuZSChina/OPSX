
## EV 按照640测得
import os
import matplotlib.pyplot as plt

amb_file = open('ambient.txt')
amb_lines = amb_file.readlines()
amb_stage1 = []
amb_stage2 = []
for i in amb_lines:
    i = i.replace('\n','')
    temp = i.split(';')
    amb_stage1.append(float(temp[0]))
    amb_stage2.append(float(temp[1]))

avg_amb_s1 = sum(amb_stage1)/len(amb_lines)
avg_amb_s2 = sum(amb_stage2)/len(amb_lines)
print("avg_amb_s1,avg_amb_s2",avg_amb_s1,avg_amb_s2)

meter_file = open('meter_ev.txt')
meter_lines = meter_file.readlines()
meter_ev = []
meter_lux = []
for i in meter_lines:
    i = i.replace('\n','')
    meter_ev.append(float(i))
    meter_lux.append(10*(2**(float(i)-2)))
print('meter raw ev',meter_ev, meter_lux)

cam_file = open('cam_data.txt')
cam_lines = cam_file.readlines()
cam_s1 = []
cam_s2 = []
for i in cam_lines:
    i = i.replace('\n','')
    temp = i.split(';')
    cam_s1.append(float(temp[0]))
    cam_s2.append(float(temp[1]))

print(cam_s1,cam_s2)

meter_lux_s2_g = []
s2_g = []
#plt.plot(meter_lux,cam_s1,'o',meter_lux,cam_s2,'o')
for i in range(len(meter_ev)):
    if cam_s2[i] <=2800:
        s2_g.append(cam_s2[i])
        meter_lux_s2_g.append(10*(2**(float(meter_ev[i])-2)))
print(meter_lux_s2_g,s2_g)
#plt.plot(meter_ev,cam_s1,'o',meter_ev,cam_s2,'o')
#plt.show()
#plt.scatter(amb_stage1, amb_stage2)
#plt.show()