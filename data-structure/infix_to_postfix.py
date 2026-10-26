
import string


SIZE = 10
STACK = [None] * SIZE
top = -1
operators={"+" :0, "-":0,"*":1,"/":1,"^":2 }
operands = list(string.ascii_lowercase)
a=input("enter:")
a="".join(a.split())

result=""
def isFull():
    if (top == SIZE - 1):
        return True
    return False

def push(x):
    global top
    if(not isFull()):
        top +=1
        STACK[top]=x
    else:
        print("stack overflow!")
        
def isEmpty():
    if(top==-1):
        return True
    return False
        
def pop():
    global top
    if(not isEmpty()):
        x=STACK[top]
        STACK[top]=None
        top -=1
        return x
    else:
        print("stack underflow!")
        return None

def operatorsPrecedence (i):
    if operators == -1:
        return True
    elif STACK[top]=="(":
        return True
    return operators[a[i]]>operators[STACK[top]]
        

for i in range (0,len(a)):
    if a[i] == '(':
        push(a[i])
    elif a[i] == ')':
        while top != -1 and STACK[top] != '(':
            result += pop()
        pop()
    elif(a[i] in operators):
        if top == -1:
            push(a[i])
            
        elif operatorsPrecedence(i):
            push(a[i])
        else:
            while top != -1 and  not operatorsPrecedence(i):
                b=pop()
                result +=b
            push(a[i])    
            
    elif a[i].lower() in operands or isinstance(int(a[i]),(int,float)):
        result += a[i]
        
while top != -1 :
    
        b=pop()
        result+=b

print(result)
