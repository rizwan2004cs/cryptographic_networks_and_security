def onetime_encrypt(plain,key):
    res = ""
    if plain.isalpha() and key.isalpha() and len(plain) == len(key) :
        plain = plain.upper()
        key = key.upper()   
        for i in range(len(plain)):
           res += chr(((ord(plain[i])+ord(key[i]))-130)%26+65)
    return res

def onetime_decrypt(plain,key):
    res = ""
    if plain.isalpha() and key.isalpha() and len(plain) == len(key) :
        plain = plain.upper()
        key = key.upper()   
        for i in range(len(plain)):
           res += chr(((ord(plain[i])-ord(key[i]))-130)%26+65)
    return res

def main():
    choice = int(input("1 - Encrypt \n2 - Decrypt\nSelect one of the option :"))
    if choice == 1:
        plain = input("Enter plain text:")
        key = input("Enter key:")
        print("cipher text is",onetime_encrypt(plain,key)) 
    elif choice == 2:
        cipher = input("Enter cipher text:")
        key = input("Enter key:")
        print("palin text is ",onetime_decrypt(cipher,key)) 
    else :
        print("Invalid choice")
    
if __name__ == "__main__":
    main()