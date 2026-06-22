print("โปรแกรมการคำนวณคะแนนรวม \n ")

Thai = int(input("คะแนนภาษาไทย "))
Math = int(input("คะแนนคณิตศาสตร์ "))
English= int(input("คะแนนภาษาอังกฤษ "))

total_point= (Thai + Math + English)
average = total_point/3

print("\nคะแนนรวมของคุณ = " , total_point)
print("คะแนนเฉลี่ยของคุณ = " , average)

if average < 60:
    print("คะแนนของคุณควรปรับปรุง")
elif average < 80:
    print("คะแนนของคุณผ่านเกณฑ์")
else :
    print("คะแนนของคุณอยู่ในขั้นดีเยี่ยม")

print(" จัดทำโดย พิมพ์พิศา ผโลศิลป์ เลขที่ 32 ")