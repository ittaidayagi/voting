from config import config
import db_utils

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

    def close_connection(self):

        self.socket_handler.close_socket(self.client_id)

    def main(self):

        if self.check_ballot():
            print "cool bro"
            self.socket_handler.communicate_with_client(self.client_id, "good boi")
        else:
           print "Your not authorized dude"
        self.close_connection()
