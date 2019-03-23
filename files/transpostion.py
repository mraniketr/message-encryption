import math
import pyperclip

# transposition cipher
# ref - https://inventwithpython.com/hacking/chapter8.html
def tc(msg1):
    msg = msg1
    print("Enter Key")
    key = int(input())
    cipher = encmsg(key, msg)
    print(cipher + '|')
    pyperclip.copy(cipher)


def encmsg(mkey, message):
    cipher = [''] * mkey
    for col in range(mkey):
        pos = col
        while pos < len(message):
            cipher[col] += message[pos]
            pos += mkey
    return ''.join(cipher)


# decprytion of transpositon cipher
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


