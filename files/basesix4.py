import base64

def enc(msg):
    # base64 encoding3
    # https://docs.python.org/2/library/base64.html
    encoded_data = base64.b64encode(msg.encode())

    return encoded_data

def dec(msg):
    decoded_data = base64.b64decode(msg)
    return decoded_data
