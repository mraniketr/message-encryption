from files.reversecipher import *
from files.transpostion import *
from files.basesix4 import *

print("Encoding")
print("\n1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")
ch = int(input())

print("Input message")
msg = input()

if ch == 1:
    print(revc(msg))
elif ch == 2:
        tc(msg)
elif ch == 3:
    print(str(enc(msg),'utf-8'))
    pyperclip.copy(str(enc(msg),'utf-8'))
else:
    print("Incorrect Input")


print ("\nDecoding\n")

print("1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")

print("Enter your choice")
ch=int(input())

print("Enter Cipher")
emsg = input()

if ch == 1:
    print(revc(emsg))

elif ch == 2:
    dc(emsg)

elif ch == 3:
    print(str(dec(emsg), 'utf-8'))
else:
    print("Incorrect Input")