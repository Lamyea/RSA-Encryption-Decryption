import rsa
from cryptography.fernet import Fernet #importing fernet class from cryptography library
# using fernet to symmetric  key
key = Fernet.generate_key()

# write the symmetric key to a file becaue every time a new key will be generated
#saving it helps to use it easily
k = open('product.key2','wb') # saving the product key with user 1 name
k.write(key)
k.close()

# creating 2048 bits of RSA public and private key
(pubkey_user2,privkey_user2)=rsa.newkeys(2048)



#saving public key with a file
pukey2 = open('publickey_user2.key','wb')
pukey2.write(pubkey_user2.save_pkcs1('PEM')) # Privacy Enhanced Mail (PEM)
pukey2.close()


# saving the private key with a file to decrypt any encrypted file with user 1 public key
prkey2 = open('privkey_user2.key','wb')
prkey2.write(privkey_user2.save_pkcs1('PEM'))
prkey2.close()


#Startig digintature signature for integrity
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


# Here loading private key for the digital signature
privkey = rsa.PrivateKey.load_pkcs1(file_open('privkey_user2.key'))

# Open the secret message file and return data to variable
message = file_open('user2_message.txt')


# Sign the message with the owners private key
signature = rsa.sign(message, privkey, 'SHA-512')

s = open('user2_signature_file','wb')
s.write(signature)



