arr=[["a","b","c"],["d","e","f"],["g","h","i"]]
hide=[[555,555,555],[555,555,555],[555,555,555]]
for i in range(0,3):
    for m in range(0,1):
              print (" ",arr[i][m]," | ",arr[i][m+1]," | ",arr[i][m+2])
D=["a","b","c","d","e","f","g","h","i"]
A=[1,3,5,7,9]
Z=[0,2,4,6,8]
p1="player1"
p2="pleyer2"
game=True
t=1
while t<=5:
    while game ==True:
                print(p1)
                print(D)
                n= input("please,enter where you want to put your num from above")#p1
                x=n.lower()
                if x=='a':
                    z=0
                    s=0
                elif x=='b':
                    z=0
                    s=1
                elif  x== 'c':
                    z=0
                    s=2
                elif x=='d':
                    z=1
                    s=0
                elif x== 'e':
                    z=1
                    s=1
                elif x== 'f':
                   z=1
                   s=2
                elif x=='g':
                   z=2
                   s=0
                elif x=='h':
                    z=2
                    s=1
                elif x=='i':
                    z=2
                    s=2
                while( x not in D):
                    n=input("please,enter where you want to put your num from above")
                    x=n.lower()
                print(A)   
                y=int(input("please,enter odd num from above"))  #p1
                while(y%2==0):
                    while( y not  in A):
                        y=int(input("please,enter odd num from above"))
             
                if y%2!=0:
                    arr[z][s]=y
                    hide[z][s]=y
                    for i in range(0,3):
                        for m in range(0,1):
                                  print (" " ,arr[i][m]," | ",arr[i][m+1]," | ",arr[i][m+2])
                    
                D.remove(x)
                A.remove(y)
                if ((hide[0][0]+hide[0][1]+hide[0][2]==15)or (hide[1][0]+hide[1][1]+hide[1][2]==15)or(hide[2][0]+hide[2][1]+hide[2][2]==15)or(hide[0][0]+hide[1][0]+hide[2][0]==15)or(hide[0][1]+hide[1][1]+hide[2][1]==15)or(hide[0][2]+hide[1][2]+hide[2][2]==15)or(hide[0][0]+hide[1][1]+hide[2][2]==15)or(hide[0][2]+hide[1][1]+hide[2][0]==15)):
                                                                     print("player1 win")
                                                                     game=False
                elif t==5:
                    print("Draw")
                    game=False
                break
            
    while game ==True:
                print(p2)
                print(D)
                n= input("please,enter where you want to put your num from above")#p1
                x=n.lower()
                if x=='a':
                    z=0
                    s=0
                elif x=='b':
                    z=0
                    s=1
                elif  x== 'c':
                    z=0
                    s=2
                elif x=='d':
                    z=1
                    s=0
                elif x== 'e':
                    z=1
                    s=1
                elif x== 'f':
                   z=1
                   s=2
                elif x=='g':
                   z=2
                   s=0
                elif x=='h':
                    z=2
                    s=1
                elif x=='i':
                    z=2
                    s=2
                while( x not in D):
                    n=input("please,enter where you want to put your num from above")
                    x=n.lower()
                print(Z)   
                y=int(input("please,enter even num from above"))  
                while(y%2!=0):
                    while( y not  in Z):
                        y=int(input("please,enter even num from above"))
             
                if y%2==0:
                    arr[z][s]=y
                    hide[z][s]=y
                    for i in range(0,3):
                        for m in range(0,1):
                                  print (" ",arr[i][m]," | ",arr[i][m+1]," | ",arr[i][m+2] )
                    
                D.remove(x)
                Z.remove(y)
                if ((hide[0][0]+hide[0][1]+hide[0][2]==15)or (hide[1][0]+hide[1][1]+hide[1][2]==15)or(hide[2][0]+hide[2][1]+hide[2][2]==15)or(hide[0][0]+hide[1][0]+hide[2][0]==15)or(hide[0][1]+hide[1][1]+hide[2][1]==15)or(hide[0][2]+hide[1][2]+hide[2][2]==15)or(hide[0][0]+hide[1][1]+hide[2][2]==15)or(hide[0][2]+hide[1][1]+hide[2][0]==15)):
                                                                     print("player2 win")
                                                                     game=False
                else:
                    t+=1
                break
                                                        

                                                        
