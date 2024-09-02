rate = [None,51,24,20]
print(f" Menu --> 1.Coffee 2.Water 3.Tea ")
select = int(input("เลือกเครื่องดื่มต้องการ 1-3 "))
pay = rate[select]
print(pay)

while pay > 0:
    m = int(input("1,2,5,10 --> "))
    if m == 1 or m == 2 or m == 5 or m == 10:
        pay = pay-m
        if pay > 0:
            print(f"เงินที่ต้องจ่าย {pay}")
    else:
        print("ไม่รับเงินจำนวนนี้")

amount = -pay
print(amount)

while amount > 0 :
    if amount>= 10:
        c1 = amount//10
        amount = amount%10
        print(f"เหรียญ 10 จำนวน{c1} ")

    if amount>=5 and amount<9:
        c2 = amount//5
        amount = amount%5
        print(f"เหรียญ 5 จำนวน{c2} ")

    if amount>1 :
        c3 = amount//2
        amount = amount%2
        print(f"เหรียญ 2 จำนวน{c3} ")

    if amount==1 :
        amount = 0
        print(f"เหรียญ 1 จำนวน 1")
    