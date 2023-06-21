def Caesar_cipher_enc(text,n):
    enc_text = ''
    for i in text:
        if i.isalpha()==True:
            if i.islower():
                enc_text+=chr((ord(i) - 97 + n) % 26 + 97)
            elif i.isupper()==True:
                enc_text+=chr((ord(i) - 65 +n) % 26 + 65)
        else:
            enc_text+=i
    return enc_text


result = Caesar_cipher_enc('the quick brown FOX JUMPS OVER THE LAZY DOG',23)
print(result)

def Caesar_cipher_dec(text):
    # decode with brutforce
    dec_text =''
    for i in range(26):
        for j in text:
            if j.isalpha() == True:
                if j.islower():
                    dec_text += chr((ord(j) - 97 + i) % 26 + 97)
                elif j.isupper() == True:
                    dec_text += chr((ord(j) - 65 + i) % 26 + 65)
            else:
                dec_text += j
        dec_text+=' shift number: {} \n '.format(i)
    return dec_text



result = Caesar_cipher_dec('qeb nrfzh yoltk CLU GRJMP LSBO QEB IXWV ALD')
print(result)