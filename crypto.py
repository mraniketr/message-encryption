import pyperclip
import base64

# reverse cipher
def revc(msg):
    crev=''
    i=len(msg)-1
    while i>=0:
        crev=crev+msg[i]
        i=i-1
    return  crev
        

#transposition cipher
#ref - https://inventwithpython.com/hacking/chapter8.html
def main(msg1):
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

        
print ("input message")
msg=input()
print("1.Rev cipher \n2.Transposition Cipher \n3.base64 Cipher")
ch = int(input())
if ch==1:
    print(revc(msg))
elif ch==2:
    if __name__=='__main__':
        main(msg)    
elif ch==3: 
    #base64 encoding3 
    #https://docs.python.org/2/library/base64.html
    encoded_data = base64.b64encode('Encode this text')
    print("Encoded text with base 64 is")
    print(encoded_data)
else:
    print(1)
