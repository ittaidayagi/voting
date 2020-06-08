from clientHandler import clientHandler
from socketHandler import SocketHandler
import cryptographicUtils
import socket

def main():

    #socket_handler = SocketHandler()
    #socket_handler.wait_for_connections()
    pub_key =  cryptographicUtils.read_public_key(r"c:\users\ittai\pycharmProjects\voting\venv\keys\192.168.8.13.pub")
    #encrypted =  cryptographicUtils.encrypt_message("hey you", pub_key)
    key_and_iv = cryptographicUtils.initialize_key()
    encrypted_message = cryptographicUtils.aes_encrypt(key_and_iv, "hey you guyz")
    print encrypted_message
    message = cryptographicUtils.aes_decryptor(key_and_iv, encrypted_message)
    print message

if __name__ == "__main__":
    main()