for i in range(1):
    for j in range(1,10):   
        if(j==2 or j==3 or j==7 or j==8):
            print("* ",end='')
        else:
            print("  ",end='')  
print()                  
for i in range(1):
    for j in range(1,10):                                   
        if j==5:
                print("  ",end='')
        else:
                print("* ",end='') 
print()                
for i in range(1):
     for j in range(1,10):
          print("* ",end='')   
print()
for i in range(4):
    for j in range(1,10):
        if(j<=(1+i) or j>=(9-i)):
            print("  ",end='')
        else:
            print("* ",end='')  
    print()
                                                   