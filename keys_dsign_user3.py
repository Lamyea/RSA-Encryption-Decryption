import rsa
from cryptography.fernet import Fernet #importing fernet class from cryptography library
# using fernet to symmetric  key
key = Fernet.generate_key()

# write the symmetric key to a file becaue every time a new key will be generated
#saving it helps to use it easily
k = open('product.key3','wb') # saving the product key with user 1 name
k.write(key)
k.close()

# creating 2048 bits of RSA public and private key
(pubkey_user3,privkey_user3)=rsa.newkeys(2048)



#saving public key with a file
pukey3 = open('publickey_user3.key','wb')
pukey3.write(pubkey_user3.save_pkcs1('PEM')) # Privacy Enhanced Mail (PEM)
pukey3.close()


# saving the private key with a file to decrypt any encrypted file with user 1 public key
prkey3 = open('privkey_user3.key','wb')
prkey3.write(privkey_user3.save_pkcs1('PEM'))
prkey3.close()


#Startig digintature signature for integrity
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Here loading private key for the digital signature
privkey = rsa.PrivateKey.load_pkcs1(file_open('privkey_user3.key'))

# Open the secret message file and return data to variable
message = file_open('user3_message.txt')


# Sign the message with the owners private key
signature = rsa.sign(message, privkey, 'SHA-512')

s = open('user3_signature_file','wb')
s.write(signature)



