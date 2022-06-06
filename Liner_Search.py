start = 0
end = 100
med = 0
print("Guessing a number between 0 : 100  ")
while True :
    med = (start+end)//2
    print('Is your number is ' + str(med) )
    print("type 1 if true")
    print("type 0 if false ")
    x=int(input())
    if x==0 :
        select = (input("Type 'h' if your number higher and type 'l' if your number lower :  "))
        if select == 'h':
            start = med 
        elif select == 'l':
            end = med 
    elif x==1 :
        break
    else :
        print("Wrong select (0-0)")
