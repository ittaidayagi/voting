class config():

    def __init__(self):
        self.config_file = {
            "DB_HOST": "localhost",
            "DB_PORT": 27017,
            "DB_NAME": "votes",
            "GOOD_COLLECTIONS": ["users", "ballots"],
            "VALID_KEYS_TO_COLLECTION": {"users": ["Personal_ID", "ballot", "pwd"], "ballots": ["ip", "name", "results"]}
        }

    def get(self, key):

        if key in self.config_file.keys():

            return self.config_file[key]
        else:
            return False, "There is no such key"

