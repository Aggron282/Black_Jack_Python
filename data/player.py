
import time

class Player:
    def __init__(self,engine,who,is_dealer):
        self.did_win = False;
        self.hand = [];
        self.who = who;
        self.is_dealer = is_dealer;
        self.engine = engine;
        self.opponent = None;
        self.money = 0;
        self.bet = 0;

    def get_saved_money(self):
        if self.is_dealer != True:
            with open("./../saved_data/money.txt") as money_file:
                self.
           
    def set_opponent(self,opponent):
        self.opponent = opponent;
    
    def deal_card(self):
        
        if self.is_dealer == True and self.get_total() >= 17:
            self.check_win();
        else:

            card = self.engine.card_deck.deal_card();
            
            self.hand.append(card);
            print(f"*****{self.who} Cards*****")
            self.display_cards();
            
            total = self.get_total();
                
            if total >= 21: 
                self.check_win();

    def check_win(self):
               
        compare = self.opponent.get_total()
        
        if self.is_dealer == True:
            self.reveal_cards();
        
        self.display_cards()
         
        total = self.get_total();

        if total > 21 or total < compare:
           time.sleep(1 * self.engine.print_speed_multiplier);
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~{self.opponent.who} Win!~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~{self.who} Loses!~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~{self.opponent.who} = {compare} | {self.who} = {total}~~~~~~~~~~~~~~~~~~~~~~~~")
           
           self.did_win = True;
           self.opponent.set_win(False);
        
        elif total == 21 or total > compare:
           time.sleep(1 * self.engine.print_speed_multiplier);
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~ {self.who} Win! ~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~ {self.opponent.who} Loses! ~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {self.who} = {total} | {self.opponent.who} = {compare} ~~~~~~~~~~~~~~~~~~~~~~~~")
           
           self.did_win = True;
           self.opponent.set_win(False);
 
        elif total == compare:
           time.sleep(1 * self.engine.print_speed_multiplier);
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!~~~~~~~~~~~~~~~~~~~~~~~~")
           print(f"-------------------------Its a Tie------------------")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!~~~~~~~~~~~~~~~~~~~~~~~~")
           
           self.did_win = True;
           self.opponent.set_win(True);
        
        time.sleep(1 * self.engine.print_speed_multiplier);
        end = input("Game has ended press q to quit or anything else to play again");
        
        if end != "q":
            self.engine.start_game();
        else:
            quit();
    
    def set_win(self,did_win):
        self.did_win = did_win;
    
    def display_cards(self):
        
        display = "";
        
        for card in self.hand:
              
              if card["isFlipped"] == True:
                  #display += card["icon"];
                  if card["isAce"] == True:
                      display += "|--Ace--|"
                  else:
                      display+= f" |--{card["value"]}--|"
                
              else:
                  display += " |--??--| "
        time.sleep(1 * self.engine.print_speed_multiplier);
        print(display + "\n")
        
    def get_display_total(self):
         
         total = 0;
        
         for card in self.hand:
              if card["isFlipped"]:
                  total += int(card["value"])
         
         return total;

    def get_total(self):
         total = 0;
        
         for card in self.hand:
              
              if card["isAce"] != True:
                  total += int(card["value"])
         
         for card in self.hand:
             
              ace = 0;
              ace = total + 11;
              
              if card["isAce"] == True:
                  if ace <= 21:
                      total+= 11;
                  else:
                      total += 1;

         return total;
                   
    def reveal_cards(self):
        print(f"*****{self.who} Reveals*****")
        self.hand = self.flip_all_cards();
        
    def flip_all_cards(self):
        
        for card in self.hand:
            card["isFlipped"] = True;
         
        return self.hand;
