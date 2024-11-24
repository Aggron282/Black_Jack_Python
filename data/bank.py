import math;

class Bank:
    def __init__(self):
        self.money = self.get_saved_money();
        self.bet = 0;
    
    def get_saved_money(self):
            with open("saved_data/money.txt") as money_file:
                money = money_file.read()
                self.money = float(money.strip())
                money_rounded = round(self.money, 2)
                self.money = money_rounded;
                print(f"You have ${self.money:.2f} left \n")
                return money_rounded;
    
    def set_bet(self,bet):
        if(bet <= self.money):
            self.bet = bet;
            print(f"You bet ${self.bet:.2f} \n You have ${self.money:.2f} left");
            return True;
        else:
             print("You have insufficient funds \n");
             return False;

    def double_bet(self):
         if(self.bet * 2 < self.money):
             self.bet *= 2;
             return True;
         else:
            print("You have insufficent funds");
            return False;              

    def get_bet(self):
         return self.bet;

    def get_money(self):
         return self.money;

    def bet_check(self,multiplier):
         bet = self.bet;
         self.money += abs(self.bet) * (abs(multiplier) / multiplier);
         self.bet = 0;
         self.print_gamble_data(bet);

    def print_gamble_data(self,bet):
         print(f"""
            Your bet ${bet:.2f} >> Money Left: ${self.money:.2f}
         """);

    def save_money(self):
            with open("saved_data/money.txt",mode="w") as money_file:
                money_file.write(str(self.money));