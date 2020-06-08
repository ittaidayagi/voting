from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
from cryptography.hazmat.primitives import padding as pad
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

BACKEND = default_backend()

def read_public_key(path):
    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

def assymetric_encrypt_message(message, public_key):

    encrypted = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256())
                                                         ,algorithm=hashes.SHA256(), label=None))
    return encrypted

def initialize_key():

    key = os.urandom(32)
    iv = os.urandom(16)
    return key, iv

def aes_encrypt(key_and_iv, message):
    padder = pad.PKCS7(256).padder()
    padded_message = padder.update(message)
    padded_message += padder.finalize()
    key, iv = key_and_iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_message) + encryptor.finalize()
    return ct

def aes_decryptor(key_and_iv, encrypted_message):
    unpadder = pad.PKCS7(256).unpadder()
    key, iv = key_and_iv
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(encrypted_message) + decryptor.finalize()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message

