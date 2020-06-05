from config import config
import db_utils

class clientHandler():

    def __init__(self, client_ip, client_id):

        self.client_ip = client_ip
        self.client_id = client_id
        self.main()

    def check_ballot(self):

        collection =  db_utils.connect_to_collection(config().get("DB_HOST"), config().get("DB_PORT"), "ballots")
        if db_utils.query_collection(collection,{"ip": self.client_ip}):
            collection.database.client.close()
            return True
        else:
            collection.database.client.close()
            return False

    def main(self):

        if self.check_ballot():
            print "cool bro"
        else:
           print "Your not authorized dude"
