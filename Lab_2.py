from itertools import count

choice = input("""Виберіть ваш варіант: 
A - Кількість букв в тексті
B - Сортувати за абеткою
Ваш вибір  : """)

def countstr(leter):
    d = {}
    for w in leter:
        d[w] = leter.count(w)
    for k in sorted(d):
        print(k + ":" + str(d[k]))

while choice == "A":
    print("Ви обрали операцію 'A' (Обрахувати кількість кожної букви у тексті )")
    ttx = (input("""Введіть ваш текст : 
    """)).strip()
    countstr(ttx)
    print("Програма виконана! ")
    print("Якщо бажаєте продовжити натисніть - 1")
    print("Вихід - 2")
    choice2 =  input("Ваша операція : ")
    if choice2 =="2":
        break
    if choice2 == "1":
        choice == "A"
    else: print("ти зламав програму!!! ")
while choice == "B":
    print("Ви обрали опрерацію 'B' (Посортувати слова в словниковому порядку)")
    ttx = input("""Введіть ваш текст  : 
    """).replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', '').replace('!', '').replace('&', '').replace('#','').replace(';','').replace('(','').replace(')','')
    ttx = ttx
    ttx = sorted(ttx)
    print(ttx)
    print("Програма виконана!")
    print("Якщо бажаєте продовжити натисніть - 1")
    print("Вихід - 2")
    choice3 =  input("Ваша операція : ")
    if choice3 =="2":
        break
    if choice3 == "1":
        choice == "B"
    else: print("ти зламав програму!!! ")
