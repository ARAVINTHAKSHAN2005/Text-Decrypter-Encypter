#Encrypter 
plain_text = input ("enter message to be encrypted : ")

encrypted_text = ""

for letter in plain_text:
    
    com_letter = ord(letter)
    
    com_letter = (com_letter) + 1
    
    reverse = chr(com_letter)
    
    encrypted_text = encrypted_text + str(reverse)
    
print(encrypted_text)

