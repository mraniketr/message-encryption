# reverse cipher
def revc(msg):
    crev=''
    i=len(msg)-1
    while i>=0:
        crev=crev+msg[i]
        i=i-1
    return  crev
        
print ("input message")
msg=input()
print("1. Rev cipher \n 2. ROT13")
ch = int(input())
if ch==1:
    print(revc(msg))
elif ch==2:
    print(1)
else:
    print(1)
