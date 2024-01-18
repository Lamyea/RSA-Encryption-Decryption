import rsa
from cryptography.fernet import Fernet

#user 2
# load the private key to decrypt the public key
# Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Open public key file and load in key
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey_user1.key'))

message = file_open('user1_message.txt')
signature = file_open('user1_signature_file')

# Verify the signature to show if successful or failed
try:
    rsa.verify(message,signature,pubkey)
    print("Signature successfully verified")

except:
    print("Wrong key!!! Check the source")

prkey_user2 = open('privkey_user2.key','rb')
pkey_user2 = prkey_user2.read()
private_key_user2 = rsa.PrivateKey.load_pkcs1(pkey_user2)

e = open('encrypted_key_file1','rb')
ekey = e.read()

dpubkey_user2 = rsa.decrypt(ekey,private_key_user2)

cipher_user2 = Fernet(dpubkey_user2)
encrypted_data_file1 = open('encrypted_file1','rb')
edata_user2 = encrypted_data_file1.read()



decrypted_data_user2 = cipher_user2.decrypt(edata_user2)
ekey = open('decrypted_file1','wb')
ekey.write(decrypted_data_user2)
print(decrypted_data_user2.decode())