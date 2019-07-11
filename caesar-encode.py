#https://repl.it/languages/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 9

new_msg = ''
msg = input("Enter a message : ")
for char in msg:
    if char.islower():
        if char in alphabet:
            pos = alphabet.find(char)
            #print (pos)
            new_pos = (pos + key) % 26
            enc = alphabet[new_pos]
            new_msg += enc
    elif char.isupper():
        if char in alphabet_c:
            pos = alphabet_c.find(char)
            #print (pos)
            new_pos = (pos + key) % 26
            enc = alphabet_c[new_pos]
            new_msg += enc
    else:
        new_msg +=char
print (new_msg)