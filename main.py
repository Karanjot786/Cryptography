from cryptography.fernet import Fernet

# For private key generate and save in mykey.key file
# key = Fernet.generate_key()
# 
# with open('mykey.key','wb') as mykey:
    # mykey.write(key)

# For Read key for the file
with open('mykey.key', 'rb' ) as mykey:
    key = mykey.read()

# print(key)



# To Encrypt the file

# f = Fernet(key)
# with open('file.txt', 'rb') as original_file:
#     original = original_file.read()
# encrypted = f.encrypt(original)
# with open('enc_file.txt','wb') as enc_file:
#     enc_file.write(encrypted)




# TO decrypt the file

f = Fernet(key)
with open('enc_file.txt','rb') as original_file:
    encrypted = original_file.read()
decr = f.decrypt(encrypted)
with open('dec_file.txt', 'wb') as dec_karanjot:
    dec_karanjot.write(decr)