print("This is my second attempt at making a calculator")            
print("Start now")
### IMPORTS ###
import os 
### FUNCTIONS ###

def Calculator():
   n=[0]*3
   for i in range(3):
       inp(n,i)
   ans=Calc(n)
   print('\nans= ', ans)
   Continue(n,ans) 

def inp(n,i):
    if i==0:
        n[i]=input()
        try: 
            n[i]=int(n[i])
        except ValueError:
            n[i]=float(n[i])
        except:
            print('\nPlease Input Valid Number')
            inp(n,i)
    if i==2:
        n[i]=input(str(n[0])+str(n[1])+'')
        try: 
            n[i]=int(n[i])
        except ValueError:
            n[i]=float(n[i])
        except:
            print('\nPlease Input Valid Number')
            inp(n,i)          
    elif i==1:
        n[i]=input('+,-,*,/= ')
        if n[i]!='+' and n[i]!='-' and n[i]!='*' and n[i]!='/' :
            print('\nPlease Input Valid Operator')
            inp(n,i)
            
def Calc(n):
    if n[1]=='+':
        ans=n[0]+n[2]
    if n[1]=='-':
        ans=n[0]-n[2]
    if n[1]=='*':
        ans=n[0]*n[2]
    if n[1]=='/':
        ans=n[0]/n[2]
    try:
        ans=int(ans)
    except:
        ans=float(ans)
    return ans

def Continue(n,ans):
    n[0]=ans    
    for i in range(1,3):
        inp(n,i)
    ans=Calc(n)
    print('\nans= ', ans)
    Continue(n,ans) 
   
### RUNNING CODE ###

Calculator()