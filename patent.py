from random import choice
import os
class patent():

    def __init__(self, user_name, level = 100, score = 0):
        self.user_name = user_name
        self.level = level
        self.score = score
    
    @classmethod
    def game_data(cls):
        with open("dict_inventions.txt", "r") as fh_game:  
            cls.patent_dict = eval(fh_game.read())

    @classmethod
    def user_data(cls, action = "load"):
            if action == "load":
                with open("user_data.txt", "r") as fh_load:
                    cls.users_scores = eval(fh_load.read())
    
            elif action == "save":
                with open("user_data.txt", "w+") as fh_save:
                    txt = str(cls.users_scores)
                    fh_save.write(txt)

            elif action == "update":
                cls.users_scores[cls.user_name] = cls.users_scores.get(cls.user_name, 0)
                if cls.users_scores[cls.user_name] < cls.score:
                    cls.users_scores[cls.user_name] = cls.score
            
            elif action == "clear":
                with open("user_data.txt", "w") as fh_clear:
                    fh_clear.write("{'defaut': 0}")
            
            else:
                print("The command wasn't clear.")


    # def add_score(self):
    #     self.score += 100

    def collector(self, inventB):
        if inventB == None:
            inventA = choice(range(1800, 2022))
        else:
            inventA = inventB
        while True:
            inventB = choice(range(inventA-self.level, inventA+self.level+1))
            if 1800 <= inventB <= 2021:
                return (inventA, inventB)
    
    def display(self, inventA, inventB, condition = "game"):
        A = self.patent_dict[inventA].split()
        B = self.patent_dict[inventB].split()
        if condition == "game":
            return f"""
************************* PATENT OFFICER *************************
------------------------------------------------------------------
PLAYER: {self.user_name}
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
            HIGHEST COINS: {highest}
                          GAME    OVER
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
            elif ans not in ("a", "b"):
                print("Invalid Input")
            else:
                return False

if __name__ == "__main__":
    patent.game_data()
    patent.user_data()
    player = patent("Kwabena")
    B = None
    while True:
        os.system("cls")
        A, B = player.collector(B)
        print(player.display(A, B))
        status = player.officer(A, B)
        if not status:
            print(player.display(A, B, "coins"))
            patent.user_data("save")
            break
        patent.user_data("update")

    print("So far so good")
