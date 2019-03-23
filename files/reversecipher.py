import pyperclip

def revc(msg):
    crev=''
    i=len(msg)-1
    while i>=0:
        crev=crev+msg[i]
        i=i-1
    pyperclip.copy(crev)
    return crev
