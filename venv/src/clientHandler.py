from config import config
import db_utils
import cryptographicUtils

class clientHandler():

    def __init__(self, client_ip, client_id, socket_handler):

        self.client_ip = client_ip
        self.client_id = client_id
        self.socket_handler = socket_handler
        self.main()

    def check_ballot(self):

        collection =  db_utils.connect_to_collection(config().get("DB_HOST"), config().get("DB_PORT"), "ballots")
        if db_utils.query_collection(collection,{"ip": self.client_ip}):
            collection.database.client.close()
            return True
        else:
            collection.database.client.close()
            return False

    def send_message(self, message_code):

        message = config().get_message(message_code)
        if message["message_id"] in config().get("ASYMMETRIC_MESSAGE"):

            message["key"] = cryptographicUtils.initialize_key()
            public_key = cryptographicUtils.read_public_key(r"c:\Users\ittai\PycharmProjects\voting\venv\keys\192.168.8.13.pub")
            encrypted_message = cryptographicUtils.assymetric_encrypt_message(str(message["key"]), public_key)
            clear_message = str(message["message_id"]) + str(message["message"])
            self.socket_handler.communicate_with_client(self.client_id, encrypted_message + "stop" + clear_message )

    def close_connection(self):

        self.socket_handler.close_socket(self.client_id)

    def main(self):

        if self.check_ballot():
            self.send_message("ASK_PERSONAL_ID")
            self.socket_handler.communicate_with_client(self.client_id, "good boi")
        else:
           print "Your not authorized dude"
        self.close_connection()
