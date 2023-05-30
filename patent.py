from random import choice
class patent():

    def __init__(self, user_name, level = 100, score = 0):
        self.user_name = user_name
        self.level = level
        self.score = score
    
    @classmethod
    def game_data(cls):
        with open("dict_inventions.txt", "r") as fh_game:  
            cls.patent_dict = eval(fh_game.read())

    def user_data(self, action = "save"):
            if action == "load":
                with open("user_data.txt", "r") as fh_load:
                    self.users_scores = eval(fh_load.read())
    
            elif action == "save":
                with open("user_data.txt", "w+") as fh_save:
                    txt = str(self.users_scores)
                    fh_save.write(txt)

            elif action == "update":
                self.users_scores[self.user_name] = self.users_scores.get(self.user_name, 0)
                if self.users_scores[self.user_name] < self.score:
                    self.users_scores[self.user_name] = self.score
            
            elif action == "clear":
                with open("user_data.txt", "w") as fh_clear:
                    fh_clear.write("{'defaut': 0}")
            
            else:
                print("The command wasn't clear.")


    # def add_score(self):
    #     self.score += 100

    def collector(self, inventB):
        if inventB == "":
            inventA = choice(range(1800, 2022))
        else:
            inventA = inventB
        while True:
            inventB = choice(range(inventA-self.level, inventA+self.level+1))
            if 1800 <= inventB <= 2021:
                return (inventA, inventB)
    
    def __str__(self, inventA, inventB, condition = "game"):
        A = self.patent_dict[inventA].split()
        B = self.patent_dict[inventB].split()
        if condition == "game":
            print(f"""
**************************PATENT OFFICER**************************
------------------------------------------------------------------
COINS: {self.score}
------------------------------------------------------------------
Invention A: {A[0]}
[{A[1]}]
Invention A: {B[0]}
[{B[1]}]
Which one was invented 1st, A or B:""")
        else:
            highest = max(self.users_scores.values())
            print(
                f"""
*************************** HIGH SCORE ***************************
------------------------------------------------------------------
                    COINS: {self.score}
            HIGHEST COINS: {highest}
                    GAME    OVER
------------------------------------------------------------------""")
            


if __name__ == "__main__":
    B=""; patent.game_data()
    for i in range(10):
        # print(patent.patent_dict)

        # loads, updates and saves the score of a player
        player = patent("Ogyam2")
        # player.user_data("load")
        # for i in range(5):
        #     player.add_score()
        # player.user_data("update")
        # player.user_data("save")

        # print(player.score)
        # print(player.users_scores)
        # player.user_data("clear")
        
        A, B = player.collector(B)
        print(player.patent_dict[A], player.patent_dict[B], sep="\n")
        print()
        pass
