from cryptography.fernet import Fernet
import rsa
# open the symmetric key file


skey = open('product.key2','rb')
key = skey.read()

# create the cipher
cipher = Fernet(key)

# open file for encrypting

myfile = open('file2.txt','rb')
myfiledata= myfile.read()

# encrypt the data for user2

encrypted_file2 = cipher.encrypt(myfiledata)
edata = open('encrypted_file2','wb')
edata.write(encrypted_file2)


#print(encrypted_file2)

# open the public key file
pkey_user3 = open('publickey_user3.key','rb')
pkdata_user3 = pkey_user3.read()

# load the file
pubkey_user3 = rsa.PublicKey.load_pkcs1(pkdata_user3)

# encrypt the symmetric key file with the public key
encrypted_key_file2 = rsa.encrypt(key,pubkey_user3)


ekey = open('encrypted_key_file2','wb')
ekey.write(encrypted_key_file2)


#print(encrypted_key_file2)


