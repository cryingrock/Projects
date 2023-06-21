# Affine chiper encoder and decoder with know A and B values
def encAffine(text,a,b):
    enc_text = ''
    for i in text:
        if i.isspace()==True:
            enc_text +=i
        elif i.isalpha()==True:
            if i.islower()==True:
                enc_text += chr((((ord(i)-97)*a+b)%26)+97)
            elif i.isupper()==True:
                enc_text += chr((((ord(i) - 65) * a + b) % 26) + 65)
        else:
            enc_text += i
    return enc_text


a=int(input("Enter first coefficient:"))
b=int(input("Enter second coefficient:"))
text=str(input('Enter texy to decode:'))
encoded_text = encAffine(text,a,b)
print(encoded_text)


#3 // 4
#Attack at Dawn
#Ejjeki ej Nesr

def decAffine(text,a,b):
    dec_text = ''
    for i in text:
        if i.isalpha()==True:
            if i.islower()==True:
                dec_text+=chr((((a*(ord(i)-97+26-b)))%26)+97)
            elif i.isupper()==True:
                dec_text += chr((((a * (ord(i) - 65 + 26 - b))) % 26)+65)
        else:
            dec_text+=i
    return dec_text


a = int(input("Enter first coefficient:"))
b = int(input("Enter second coefficient:"))
text = str(input('Enter texy to decode:'))
decoded_text = decAffine(text,a,b)
print(decoded_text)