from art.art import title as art_title;
from art.art import art_data;
from data.card_data import CardData;
from data.player import Player;
import time;
class Engine:
    def __init__(self):
        self.title = art_title
        self.card_deck = None;
        self.player = None;
        self.dealer = None;
        self.print_speed_multiplier = 1;
        self.start_game();
        
    
    def shuffle(self):
        decks = input("How many decks will you use? \n");
        decks = int(decks);
        
        self.card_deck = CardData(decks);
        print(".")
        time.sleep(.3 * self.print_speed_multiplier);
        print("...")
        time.sleep(.3 * self.print_speed_multiplier);
        print(".....")
        time.sleep(.3 * self.print_speed_multiplier);
        print("......Done")
        time.sleep(1 * self.print_speed_multiplier);
        print(f"You have made a stack of {decks} decks with {len(self.card_deck.generated_cards)} cards \n");
        time.sleep(1 * self.print_speed_multiplier);
   
    def print_cards_in_deck(self):
        print(f"--------- There are {len(self.card_deck.generated_cards)} left in the deck -------") 
    
    def change_print_speed(self):
        
        speed = input(
    """
    Choose Speed of Printing
    s : Slow
    n : Normal
    f : Fast
    v : Very Fast                 
    \n""");
        speed = speed.lower().strip();
        if speed == "s":
            self.print_speed_multiplier = 2;
        elif speed == "n":
                self.print_speed_multiplier = 1;
        elif speed == "f":
                self.print_speed_multiplier = .5;
        elif speed == "v":
                self.print_speed_multiplier = .35;
        else:
            self.print_speed_multiplier = self.print_speed_multiplier;
        time.sleep(1 * self.print_speed_multiplier);
        print("Changed Speed \n");
        self.next_deal();

    def start_game(self):
        
        print(self.title);
        
        if self.card_deck == None or len(self.card_deck.generated_cards) < 60:
            self.shuffle();
       
        self.player = Player(self,"Player",False);
        self.dealer = Player(self,"Dealer",True);
        self.player.set_opponent(self.dealer);
        self.dealer.set_opponent(self.player);

        self.start_deal();
           
    def get_print_speed_multiplier(self):
         return self.print_speed_multiplier;

    def print_score(self, only_return = False):
        player_total = self.player.get_total();
        dealer_total = self.dealer.get_display_total(); 
        time.sleep(1 * self.print_speed_multiplier);
        feedback = f"---Dealer Score: {str(dealer_total)} -- | --- Player Score: {str(player_total)} ---- \n";
        if only_return  == False:
            print(feedback);
        return feedback;
 
    def next_deal(self):
        print(" ___________________ What will you do? __________________ ")
        time.sleep(.3* self.print_speed_multiplier);

        next_step = input(f"""
     d : draw  | s : stand  | c : see cards left in deck \n
    dd : double bet and draw  | ss : split (only when two cards of same value are present) \n
    q : quit (lose money)  | ps: change print speed \n   
    {self.print_score(True)} \n"""
                          );
     
        next_step = next_step.lower().strip();
        print(next_step)
        
        if(next_step == "d"):
            
            self.player.deal_card();
            self.dealer.deal_card();        
            self.display_score();
            self.next_deal()
        
        elif next_step == "s" :
            while self.dealer.get_total() < 17:
                 self.dealer.deal_card();
                 self.display_score();
        elif next_step == "c" :
            self.print_cards_in_deck();
        elif next_step == "q":
            quit();
        elif next_step == "ps":
             self.change_print_speed();
        else:
            self.next_deal();
          
    def display_score(self):
          player_total = self.player.get_total();
          dealer_total = self.dealer.get_display_total();     
          time.sleep(1 * self.print_speed_multiplier);    
          print(f"---Dealer Score: {str(dealer_total)} -- | --- Player Score: {str(player_total)} ---- \n"); 
    
    def start_deal(self):
           
        for x in range(2):
            
            self.player.deal_card();
            self.dealer.deal_card();
            self.display_score();
           
        self.next_deal()