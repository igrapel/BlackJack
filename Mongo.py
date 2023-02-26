import pymongo




class Mongo:

    def __init__(self, score, user):
        self.myClient = pymongo.MongoClient("mongodb+srv://aralia:aralia@cluster0.bihpcca.mongodb.net/?retryWrites=true&w=majority")
        self.blackjack_db = self.myClient["BlackJack"]
        self.col = self.blackjack_db["Top Scores"]
        self.user = user
        self.score = score
        print("Entered Constructor")
        self.current_score = {"Player": self.user, "Score": self.score}
        self.res = self.col.insert_one(self.current_score)



