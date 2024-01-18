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
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey_user3.key'))

message = file_open('user3_message.txt')
signature = file_open('user3_signature_file')

# Verify the signature to show if successful or failed
try:
    rsa.verify(message,signature,pubkey)
    print("Signature successfully verified")

except:
    print("Wrong key!!! Check the source")

prkey_user1 = open('privkey_user1.key','rb')
pkey_user1 = prkey_user1.read()
private_key_user1 = rsa.PrivateKey.load_pkcs1(pkey_user1)

e = open('encrypted_key_file3','rb')
ekey = e.read()

dpubkey_user1 = rsa.decrypt(ekey,private_key_user1)

cipher_user1 = Fernet(dpubkey_user1)
encrypted_file3 = open('encrypted_file3','rb')
edata_user1 = encrypted_file3.read()



decrypted_file3 = cipher_user1.decrypt(edata_user1)
ekey = open('decrypted_file3','wb')
ekey.write(decrypted_file3)
print(decrypted_file3.decode())