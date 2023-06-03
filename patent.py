from random import choice
import os
class patent():

    def __init__(self, user_name, level = 100, score = 0):
        self.username = user_name
        self.level = level
        self.score = score
        
    @classmethod
    def game_data(cls):
        with open("dict_inventions.txt", "r") as fh_game:  
            cls.patent_dict = eval(fh_game.read())

    # @classmethod
    def user_data(self, action = None):
            if action == "load":
                with open("user_data.txt", "r") as fh_load:
                    self.users_scores = eval(fh_load.read())
    
            elif action == "save":
                with open("user_data.txt", "w+") as fh_save:
                    txt = str(self.users_scores)
                    fh_save.write(txt)

            elif action == "clear":
                with open("user_data.txt", "w") as fh_clear:
                    fh_clear.write("{'defaut': 0}")
            
            else:
                self.users_scores[self.username] = self.users_scores.get(self.username, 0)
                if self.users_scores[self.username] < self.score:
                    self.users_scores[self.username] = self.score

    def collector(self, inventB):
        if inventB == None:
            inventA = choice(range(1800, 2022))
        else:
            inventA = inventB
        while True:
            inventB = choice(range(inventA-self.level, inventA+self.level+1))
            if 1800 <= inventB <= 2021:
                return (inventA, inventB)
    
    def display(self, inventA, inventB, condition):
        os.system("cls")
        A = self.patent_dict[inventA].split(" - ")
        B = self.patent_dict[inventB].split(" - ")
        if condition == "clueless":
            return f"""
************************* PATENT OFFICER *************************
------------------------------------------------------------------
PLAYER: {self.username}
COINS: {self.score}
------------------------------------------------------------------
Invention A: {A[0]}
Invention B: {B[0]}

Which one was invented 1st, A or B:
"""
        if condition == "clue":
            return f"""
************************* PATENT OFFICER *************************
------------------------------------------------------------------
PLAYER: {self.username}
COINS: {self.score}
------------------------------------------------------------------
Invention A: {A[0]}
[{A[1]}]

Invention B: {B[0]}
[{B[1]}]

Which one was invented 1st, A or B:
"""
        else:
            highest = max(self.users_scores.values())
            return f"""
*************************** HIGH SCORE ***************************
------------------------------------------------------------------
                    COINS: {self.score}
                  HIGHEST: {highest}
                    GAME OVER 💔💔💔
------------------------------------------------------------------
"""
    
    def officer(self, inventA, inventB):
        while True:
            ans = input(">> ").lower()
            if (ans == "a" and inventA < inventB) or (ans == "b" and inventA > inventB):
                if self.level == 100: self.score += 10
                elif self.level == 50: self.score += 15
                elif self.level == 25: self.score += 20
                return True
            elif ans == "c":
                return None
            elif ans not in ("a", "b", "c"):
                print("Invalid Input")
            else:
                return False

if __name__ == "__main__":
    patent.game_data()
    player = patent("Ogyam")
    player.user_data("load")
    B = None
    condition = "clueless"
    while True:
        A, B = player.collector(B)

        while True:
            print(player.display(A, B, condition))
            status = player.officer(A, B)
            if status == None:
                condition = "clue"; continue
            condition = "clueless"; break

        if not status:
            print(player.display(A, B, "coins"))
            player.user_data("save")
            break
        player.user_data()

    print("So far so good")

# THE CLASS PATENT HAS BEEN COMPLETED AND IT IS WORKING AS EXPECTED.