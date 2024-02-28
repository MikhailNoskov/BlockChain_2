import os
import json
import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate public-private key pairs
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.public_key().export_key()

# Encrypt and store private key securely
# password = input("Enter password: ")
#
# cipher_rsa = PKCS1_OAEP.new(key)
# encrypted_private_key = cipher_rsa.encrypt(password.encode() + private_key)  # works with ValueError
# with open('private_key.txt', 'wb') as f:
#     f.write(encrypted_private_key)
#
# # Load encrypted private key and decrypt
# with open('private_key.txt', 'rb') as f:
#     encrypted_private_key = f.read()
# decrypted_private_key = cipher_rsa.decrypt(encrypted_private_key)

# Sign transactions using the private key
message = 'Hello, world!'
hash_message = SHA256.new(message.encode())
hash_wrong_message = SHA256.new('hash_message'.encode())

signature = pkcs1_15.new(key).sign(hash_message)
print(signature)

try:
    pkcs1_15.new(key.publickey()).verify(hash_message, signature)
    print("Signature is valid")
except (ValueError, TypeError):
    print("Signature is invalid")