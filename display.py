import math
import time
count=1
space=40
char="_"
letter_S=[[0 for i in range(5)] for i in range(7)]
letter_S[0][2:5]=[1,1,1]
letter_S[1][1]=letter_S[2][1]=1
letter_S[4][4]=letter_S[5][4]=1
letter_S[3][2:4]=[1,1]
letter_S[6][1:4]=[1,1,1]

letter_C=[[0 for i in range(5)] for i in range(7)]
letter_C[0][2:5]=[1,1,1]
letter_C[6][2:5]=[1,1,1]
letter_C[2][0]=letter_C[3][0]=letter_C[4][0]=1
letter_C[5][1]=letter_C[1][1]=1
letter_C[6][2:5]=[1,1,1]
skip=True

letter_5=[[0 for i in range(5)] for i in range(7)]
letter_5[0][:4]=[1,1,1,1]
letter_5[3][:4]=[1,1,1,1]
letter_5[6][:4]=[1,1,1,1]
letter_5[1][0]=letter_5[2][0]=letter_5[4][3]=letter_5[5][3]=1

letter_0=[[0 for i in range(5)] for i in range(7)]
letter_0[0][2]=letter_0[6][2]=letter_0[5][0]=letter_0[5][4]=letter_0[1][0]=letter_0[1][4]=1
letter_0[2][0]=letter_0[3][0]=letter_0[4][0]=letter_0[2][4]=letter_0[3][4]=letter_0[4][4]=1
letter_0[0][1]=letter_0[0][3]=letter_0[6][1]=letter_0[6][3]=1
for i in range(19):
    print()
    print(" "*space,end='')
    for j in range(space,count+space):
        
        if i-6>=0 and i-6<7 :
            if j-26>=0 and j-26<5:
                if letter_C[i-6][j-26]==1:
                    print("|",end="")
                else:
                    print("_",end='')
            
                
            
            
        
        
            elif j-33>=0 and j-33<5:
                if letter_S[i-6][j-33]==1:
                    print("|",end="")
                
                else:
                
                    print("_",end="")
            elif j-45>=0 and j-45<5:
                if letter_5[i-6][j-45]==1:
                    print("|",end='')
                else:
                    print("_",end='')
            
            elif j-51>=0 and j-51<5:
                if letter_0[i-6][j-51]==1:
                    print("|",end='')
                else:
                    print("_",end='')

            
            
            
            else:
                print("_",end='')

            
        else:
            print("_",end='')


   
    if i<9:
        count+=6
        space-=3
    else:
        count-=6
        space+=3

    
    time.sleep(0.1)




