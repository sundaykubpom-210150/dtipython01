# Control Flow คือ กระบวนการทำงานของโปรแกรม ใช้คู่กับ Control Statement
# Control Flow มี 2 ประเภท
# 1. Selection/Dicission แบบเลือกทำ คือ ต้องพิสูจน์/ตรวจสอบก่อนที่จะทำงานใดๆ โดยมี 3 แบบย่อย
# - พิสูจน์ตรวจสอบครั้งเดียว จริงทำ เท็จไม่ทำ (if)
# - พิสูจน์ตรวจสอบครั้งเดียว จริงทำ เท็จเท็จทำ (if-else)
# - พิสูจน์ตรวจสอบหลายครั้ง (if-elif-else)
 
 
# 2. Loop/Iteration/Repetitionc แบบทำซ้ำ คือ ทำงานเดิมๆ ซ้ำ มี 2 แบบย่อย
# - รู้จำนวนครั้งในการทำซ้ำ
# - ไม่รู้จำนวนครั้งในการทำซ้ำ
# *** การทำซ้ำต้องรู้จบ
# Control Statement -> คำสั่ง while, for
 
# เพิ่มเติม 2 คำสั่งที่มักใช้กับ Loop คือ break และ continue

# -พิสูจน์ตรวจสอบหลายครั้ง (if-elif-else)
score = 55

if score >= 80 : 
    print('Grade A')
elif score >= 70 :
    print('Grade B')
elif score >= 60 :
    print('Grade C')
elif score >= 50 :
    print('Grade D')
else : # อย่าลืมใส่ Colon *** ตัวสุดท้่ายสามารถใข้ else หรือ elif ก็ได้้
    print('Grade F')
    print(' อย่าเสียใจนะ T-T')

print('Bye Bye ....')
print('ei ei ....')