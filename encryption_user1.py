from cryptography.fernet import Fernet
import rsa


#user1 symmteric file to encrypt
skey = open('product.key1','rb')
key = skey.read()

# create the cipher
cipher = Fernet(key)


#opeining the file to encrypt
myfile = open('file1.txt','rb')
myfiledata= myfile.read()

# encrypted the file for another user

encrypted_data_user2 = cipher.encrypt(myfiledata)
edata = open('encrypted_file1','wb')
edata.write(encrypted_data_user2)




# open the public key file of the user (to send encrypted file with it)
pkey_user2 = open('publickey_user2.key','rb')
pkdata_user2 = pkey_user2.read()

# load the file
pubkey_user2 = rsa.PublicKey.load_pkcs1(pkdata_user2)

# encrypt the symmetric key file with the public key
encrypted_key_file1 = rsa.encrypt(key,pubkey_user2)


ekey = open('encrypted_key_file1','wb')
ekey.write(encrypted_key_file1)


#print(encrypted_key_file1)


