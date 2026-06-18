print("โปรแกรมคำนวณคะแนนรวมเทียบเกรด")

score1 = int(input("คะแนนวิชาที่1: "))
score2 = int(input("คะแนนวิชาที่2: "))
score3 = int(input("คะแนนวิชาที่3: "))

total_score = (score1 + score2 + score3)
average = total_score/3

if average < 60 :
    print("คะแนนรวมของคุณ = ", total_score)
    print("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("คะแนนของคุณไม่ผ่านเกณฑ์ ควรแก้ไขปรับปรุง")
elif average < 80:
    print("คะแนนรวมของคุณ = ", total_score)
    print("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("คะแนนของคุณอยู่ในระดับผ่านเกณฑ์")
else: 
    print("คะแนนรวมของคุณ = ", total_score)
    print("คะแนนเฉลี่ย 3 วิชา = ", average)
    print("คะแนนของคุณอยู่ในเกณฑ์ดีเยี่ยม")
    