class config():

    def __init__(self):
        self.config_file = {
            "DB_HOST": "localhost",
            "DB_PORT": 27017,
            "DB_NAME": "votes",
            "GOOD_COLLECTIONS": ["users", "ballots"],
            "VALID_KEYS_TO_COLLECTION": {"users": ["Personal_ID", "ballot", "pwd"], "ballots": ["ip", "name", "results"]},
            "ASYMMETRIC_MESSAGE": [1],
            "SYMMETROC_MESSAGE": []
        }

        self.messages = {
            "ASK_PERSONAL_ID": {"message_id": 1, "message": "please send your personal id", "key": "{0}"}
        }

    def get(self, key):

        if key in self.config_file.keys():

            return self.config_file[key]
        else:
            return False, "There is no such key"

    def get_message(self, key):
        if key in self.messages.keys():
            return self.messages[key]
        else:
            return False, "There is no such message"
