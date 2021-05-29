#Decrypter
enter_encrypted_text = input("enter encrypted text:")

decrypted_text = ""

for char in enter_encrypted_text:
    
    com_char = ord(char)
    
    com_char = (com_char) - 1
    
    reverser = chr(com_char)
    
    decrypted_text = decrypted_text + str(reverser)
    
print("your decrypted message is : ",decrypted_text)
