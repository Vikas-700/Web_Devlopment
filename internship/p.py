import random as r
import numpy as np
x=[i for i in range(1,1000001)]
new_array=np.array(x)
print(new_array)
x=input("Enter your Name First player:")
y=input("Enter Second Player Your name:")
x1=0
x2=0
l=0
while(1):
    for i in range(1):
        val=r.randint(1,6)
        print(f"{x} choose",val)
        x1+=val
        if x1<10000:
            print(f"{x} is position",x1)
            if x1%13==0:
                x1-=r.randint(10,80)
            elif x1%7==0:
                if x1<40:
                    x1+=r.randint(10,7000)
                elif x1>40 and x1<80:
                    x1+=r.randint(1,2000)        
        elif x1==10000: 
            print(f"{x} won in this game.")
            print(l)
            x1+=10000
            break
        elif x1>10000:
            x1-=val 
            print(f"{x} Next try for your luck")      
    for j in range(1):
        val=r.randint(1,6) 
        print(f"{y} choose:",val)
        x2+=val
        if x2<10000:
            print(f"{y} is position",x2)
            if x2%13==0:
                x2-=r.randint(10,80)
            elif x2%7==0:
                if x2<40:
                    x2+=r.randint(10,7000)
                elif x2>40 and x2<80:
                    x2+=r.randint(1,2000)   
        elif x2==10000: 
            print(f"{y} won in this game.") 
            print(l)
            x2+=10000
            break
        elif x2>10000:
            x2-=val  
            print(f" {y} Next try for your luck")       
    if x1>10000 or x2>10000:
        break
    l=l+1