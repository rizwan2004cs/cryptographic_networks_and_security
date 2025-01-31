strs =  input("Enter s string : ")
shift_value = int(input("Enter shift value :"))
y = ""
for s in strs:
    if s.isupper():
        t = chr((ord(s)+shift_value-65)%26+65)
    elif s.islower():
        t =  chr((ord(s)+shift_value-97)%26+97)
    elif s.isnumeric():
        t =  str((int(s)+shift_value)%10)
    elif 1 <= ord(s) <= 47:
        t = chr((ord(s) + shift_value - 1) % 47 + 1)
    elif 58 <= ord(s) <= 64:
        t = chr((ord(s) + shift_value - 58) % 7+ 58)
    elif 91 <= ord(s) <= 96:
        t = chr((ord(s) + shift_value - 91) % 6 + 91)
    elif 1 <= ord(s) <= 47:
        t = chr((ord(s) + shift_value - 1) % 47 + 1)
    elif 123 <= ord(s) <= 256:
        t = chr((ord(s) + shift_value - 123) % 134 + 123)
    else:
        t = s
    y = y + t

print(y)