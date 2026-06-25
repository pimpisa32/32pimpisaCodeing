print(" โปรแกรมตรวจสอบค่าความเร็วรถ \n")

speed = int(input(" ค่าความเร็วรถของคุณ "))

total = speed

print(" ค่าความเร็วรถของคุณคือ " , total,"km/h")

if speed < 80 :
    print(" ปลอดภัย ")

elif 81 < speed < 100 :
    print(" เตือน ")

elif 101 < speed <120 :
    print(" เสี่ยงถูกปรับ ")

else :
    print(" ผิดกฏหมาย (ปรับทันที) ")