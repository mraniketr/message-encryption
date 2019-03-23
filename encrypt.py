from files.reversecipher import *
from files.transpostion import *
from files.basesix4 import *

print ("input message")
msg=input()
print("1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")
ch = int(input())
if ch==1:
    print(revc(msg))
elif ch==2:
        tc(msg)
elif ch==3:
    print(str(enc(msg),'utf-8'))
    pyperclip.copy(str(enc(msg),'utf-8'))
else:
    print(1)


print ("\n\nDecoding\n")

print("1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")
print("Enter your choice")
ch=int(input())
if ch ==1:
    emsg = input()
    print(revc(emsg))

elif ch ==2:
    emsg=input()
    dc(emsg)

elif ch==3:
    encoded_data = input()
    print(str(dec(encoded_data), 'utf-8'))

