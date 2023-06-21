#rot chipers: rot5, rot13, rot 18
import string
import codecs

def rot_5_enc(text):
    mytable = str.maketrans('0123456789','5678901234')
    text_enc = text.translate(mytable)
    return text_enc

result = rot_5_enc('number 2023')
print(result)

def rot_5_dec(text):
    mytable = str.maketrans('5678901234','0123456789')
    text_dec = text.translate(mytable)
    return text_dec

result = rot_5_enc('number 7578')
print(result)

#--------------------------------
def rot_13_enc(text):
    a = string.ascii_lowercase #alphabet
    b = string.ascii_uppercase #alphabet
    mytable = str.maketrans(a+b,a[13:]+a[:13]+b[13:]+b[:13])
    text_enc = text.translate(mytable)
    return text_enc

result = rot_13_enc('The Quick Brwon fox Jumped over the Lazy Dog')
print(result)

def rot_13_dec(text):
    a = string.ascii_lowercase #alphabet
    b = string.ascii_uppercase #alphabet
    mytable = str.maketrans(a[13:]+a[:13]+b[13:]+b[:13],a+b)
    text_enc = text.translate(mytable)
    return text_enc

result = rot_13_enc('Gur Dhvpx Oejba sbk Whzcrq bire gur Ynml Qbt')
print(result)


#--------------------------------
def rot_18_enc(text):
    #encoding with library
    d = string.digits
    mytable = str.maketrans(d,d[5:]+d[:5])
    text = text.translate(mytable)
    encode = codecs.encode(text, 'rot13')
    return encode


result = rot_18_enc('The Quick Brwon fox Jumped over the Lazy Dog 0123456789')
print(result)

def rot_18_dec(text):
    #decoding with library
    d = string.digits
    mytable = str.maketrans(d[5:]+d[:5],d)
    text = text.translate(mytable)
    decode = codecs.decode(text, 'rot13')
    return decode


result = rot_18_dec('Gur Dhvpx Oejba sbk Whzcrq bire gur Ynml Qbt 5678901234')
print(result)




