a=0
while a<100:
    a+=1
    if a%10==7 or a/7==a//7 or a//10==7:
        continue
    print(a)
