from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify


#Generating private key (RsaKey object)
print("")
strength = int(input("Enter RSA key Size. Type 1024, 2048, 4096: "))
private_key = RSA.generate(strength)
print("")

#Generating the public keyfrom the private key
public_key = private_key.publickey()

 # (Print classes not needed) print (type(private_key), type(public_key))

#Converting the RsaKey objects to string 
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()

# (Print classes not needed) print(type(private_pem), type(public_pem))
print(private_pem)
print("")
y=input("Enter to continue")
print("")
print(public_pem)
print("")


#Storing Keys in files
print("")
y=input("Enter to save keys")
print("")



with open('Frank_private_key.pem', 'w+') as pr:
    pr.write(private_pem)

print("Private key saved")

print("")
    
with open('Frank_public_key.pem', 'w+') as pu:
    pu.write(public_pem)
    print("Public key saved")

print("---")

y=input("Ensure reciever public key is in designated folder! ")

print("")

#Importing keys from files, converting it into the RsaKey object   

receiverpublickey= input("Enter key file name: ")

print("")

pr_key = RSA.import_key(open('Frank_private_key.pem', 'r').read())
pu_key = RSA.import_key(open(receiverpublickey, 'r').read())

print("Reciever key loaded")

print("---")

#Instantiating PKCS1_OAEP object with the public key for encryption
cipher = PKCS1_OAEP.new(key=pu_key)

#Encrypting the message with the PKCS1_OAEP object

message= bytes(input("Enter text to encrypt: "), 'utf-8')



print("")

cipher_text = cipher.encrypt(message)

print("")

input("Print coded message ?")

print("")

print(cipher_text.hex())

filenamez=input("Enter file name(.txt): ")


with open(filenamez, 'w+') as xx:
    xx.write(cipher_text.hex())

print("File saved")

print("")

input("Decrypt file ?")

print("")

#Instantiating PKCS1_OAEP object with the private key for decryption
decrypt = PKCS1_OAEP.new(key=pr_key)

#Decrypting the message with the PKCS1_OAEP object
decrypted_message = decrypt.decrypt(cipher_text)
print("")
print(decrypted_message)

print("")

print("Goodbye!")
