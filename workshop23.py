
'''
match expression/ ตัวแปร :
   case คำ | คำ | ... : 
      คำสั่ง
   case คำ | คำ | ... : 
      คำสั่ง
    case คำ | คำ | ... : 
      คำสั่ง
    case คำ | คำ | ... : 
      คำสั่ง
    case คำ | คำ | ... : 
      คำสั่ง
'''

xx = 20

match xx :
    case 10 | 20 :
        print('Hello...')
        print('Wow')
    case 100 : 
        print('Hi...')
    case 555 | 666 | 777 | 888 :
        print('Hey')
        print('Humm')
    case _ :
        print('Bye Bye ')