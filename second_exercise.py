class Caesar:

    def encrypt_char(self, char, key):
        return chr(ord('A') + (ord(char) - ord('A') + key) % 26)

    def encrypt_message(self, message, key):
        message = message.upper()
        cipher = ''
        for char in message:
            if char not in ' ,.':
               a = self.encrypt_char(char, key)
               cipher += a
            else:
                cipher += char
        print("Encrypted message : " + cipher)
        return cipher
    
    def decrypt_char(self, char, key):
        return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)

    def decrypt_message(self, cipher, key):
        cipher = cipher.upper()
        message = ''
        for char in cipher:
            if char not in " ,.;'":
                message += self.decrypt_char(char, key)
            else:
                message += char
        print("Decrypted message : " + message )
        return message

c1 = Caesar()
c1.decrypt_message("WKH HDJOH LV LQ SODB; PHHW DW MRH'V.", 3)    

