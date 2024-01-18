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
#pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey_user1.key'))
pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey_user2.key'))


message = file_open('user2_message.txt')
signature = file_open('user2_signature_file')

# Verify the signature to show if successful or failed
try:
    rsa.verify(message,signature,pubkey)
    print("Signature successfully verified")

except:
    print("Wrong key!!! Check the source")

prkey_user3 = open('privkey_user3.key','rb')
pkey_user3 = prkey_user3.read()
private_key_user3 = rsa.PrivateKey.load_pkcs1(pkey_user3)

#e = open('encrypted_key_file1','rb')
e = open('encrypted_key_file2','rb')
ekey = e.read()

dpubkey_user3 = rsa.decrypt(ekey,private_key_user3)

cipher_user3 = Fernet(dpubkey_user3)
encrypted_data_user3 = open('encrypted_file2','rb')
edata_user3 = encrypted_data_user3.read()



decrypted_data_user3 = cipher_user3.decrypt(edata_user3)
ekey = open('decrypted_file2','wb')
ekey.write(decrypted_data_user3)
print(decrypted_data_user3.decode())