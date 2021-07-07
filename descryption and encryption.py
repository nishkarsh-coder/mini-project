import string 

def machine():
    # key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !"
    key= string.ascii_letters + string.punctuation +string.digits + " "
    print(key)
    value= key[-1]+key[0:-1]
    encryptDict= dict(zip(key,value))
    decryptDict= dict(zip(value,key))
    message=input("Enter ur message:")
    mode=input("what u want encrption(E) or decryption(D):")

    if mode.upper()=="E":
        new_message= ''.join([encryptDict[letter] for letter in message])
    elif mode.upper()=="D":
        new_message=''.join([decryptDict[letter] for letter in message])
    else:
        print("enter the valid mode!!!!!!!!!!!!")
    return new_message
print(machine()) 