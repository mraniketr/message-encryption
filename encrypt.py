import pyperclip
import base64
import math

# reverse cipher
def revc(msg):
    crev=''
    i=len(msg)-1
    while i>=0:
        crev=crev+msg[i]
        i=i-1
    pyperclip.copy(crev)
    return crev
        

#transposition cipher
#ref - https://inventwithpython.com/hacking/chapter8.html
def tc(msg1):
    msg=msg1
    print("Enter Key")
    key=int(input())
    cipher=encmsg(key,msg)
    print(cipher + '|')
    pyperclip.copy(cipher)
    
def encmsg(mkey,message):
    cipher=['']*mkey
    for col in range(mkey):
        pos=col
        while pos<len(message):
            cipher[col]+=message[pos]
            pos+=mkey
    return ''.join(cipher)

#decprytion of transpositon cipher
def dc(msg):
    myMessage = msg
    print("Enter Key")
    myKey = int(input())
    plaintext = decryptMessage(myKey, myMessage)
    print("The plain text is")
    print(plaintext)


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = list(' ' * numOfColumns)
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


print ("input message")
msg=input()
print("1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")
ch = int(input())
if ch==1:
    print(revc(msg))
elif ch==2:
        tc(msg)
elif ch==3: 
    #base64 encoding3
    #https://docs.python.org/2/library/base64.html
    encoded_data = base64.b64encode(msg.encode())
    print(str(encoded_data,'utf-8'))
    pyperclip.copy(str(encoded_data,'utf-8'))
else:
    print(1)

print ("\n\n\nDecoding\n")
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
    encoded_data=input()
    decoded_data = base64.b64decode(encoded_data)
    print(str(decoded_data, 'utf-8'))

