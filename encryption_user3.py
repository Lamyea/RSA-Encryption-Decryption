from cryptography.fernet import Fernet
import rsa
# open the symmetric key file


skey = open('product.key3','rb')
key = skey.read()

# create the cipher
cipher = Fernet(key)

# open file for encrypting

myfile = open('file3.txt','rb')
myfiledata= myfile.read()

# encrypt the data for user2

encrypted_data_user1 = cipher.encrypt(myfiledata)
edata = open('encrypted_file3','wb')
edata.write(encrypted_data_user1)


#print(encrypted_data_user1)

# open the public key file
pkey_user1 = open('publickey_user1.key','rb')
pkdata_user1 = pkey_user1.read()

# load the file
pubkey_user1 = rsa.PublicKey.load_pkcs1(pkdata_user1)

# encrypt the symmetric key file with the public key
encrypted_key_file3 = rsa.encrypt(key,pubkey_user1)


ekey = open('encrypted_key_file3','wb')
ekey.write(encrypted_key_file3)


#print(encrypted_key_file3)


