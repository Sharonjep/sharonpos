print("Numbers divisible by 7 not 3")
for number in range(100):
    if(number %7==0) and (number %3!=0):
        print(number)