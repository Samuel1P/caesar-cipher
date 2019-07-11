#https://repl.it/languages/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

enc_msg  = input("Paste the encoded message here  : ")
key = int(input("Enter the unlock key : "))
decoded_msg = ''
for char in enc_msg:
    if char.islower():
        if char in alphabet:
            pos = alphabet.find(char)
            final_pos = (pos - key) % 26
            decoded_msg += alphabet[final_pos]
    elif char.isupper():
        if char in alphabet_c:
            pos = alphabet_c.find(char)
            #print (pos)
            new_pos = (pos - key) % 26
            enc = alphabet_c[new_pos]
            decoded_msg += enc
    else:
        decoded_msg += char

print ("Decoded Message is : ", decoded_msg)