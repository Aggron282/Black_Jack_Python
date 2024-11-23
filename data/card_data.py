from art.art import art_data;
import random

card_data = [
    {
        "icon":art_data["ace"],
        "isAce":True,
        "name":"ace",
        "isFlipped":True,
        "value":"1"
    },
    {
        "icon":art_data["2"],
        "isAce":False,
        "name":"2",
        "isFlipped":True,
        "value":"2"
    },
    {
        "icon":art_data["3"],
        "isAce":False,
        "name":"3",
        "isFlipped":True,
        "value":"3"
    },
    {
        "icon":art_data["4"],
        "isAce":False,
        "name":"4",
        "isFlipped":True,
        "value":"4"
    },
    {
        "icon":art_data["5"],
         "isAce":False,
         "name":"5",
         "isFlipped":True,
        "value":"5"
    },
    {
        "icon":art_data["6"],
         "isAce":False,
         "name":"6",
         "isFlipped":True,
         "value":"6"
    },
    {
        "icon":art_data["7"],
         "isAce":False,
         "name":"7",
         "isFlipped":True,
        "value":"7"
    },
    {
        "icon":art_data["8"],
        "isAce":False,
        "name":"8",
        "isFlipped":True,
        "value":"8"
    },
    {
       "icon":art_data["9"],
         "isAce":False,
         "name":"9",
         "isFlipped":True,
        "value":"9"
    },
    {
        "icon":art_data["10"],
         "isAce":False,
         "name":"10",
         "isFlipped":True,
        "value":"10"
    },
    {
        "icon":art_data["jack"],
         "isAce":False,
         "name":"jack",
         "isFlipped":True,
        "value":"10"
    },
    {
        "icon":art_data["queen"],
        "isAce":False,
        "name":"queen",
        "isFlipped":True,
        "value":"10"
    },
    {
        "icon":art_data["king"],
        "value":"10",
        "isFlipped":True,
         "isAce":False,
         "name":"king",
    }
]

class CardData:
    def __init__(self,decks):
        self.card_data = card_data;
        self.how_many_cards_each = 4;
        self.decks = decks;
        self.generated_cards = [];
        self.create_cards();
    
   
    def deal_card(self):
        random_card = random.choice(self.generated_cards);
        index = self.generated_cards.index(random_card);
        try:
            self.generated_cards.remove(index);
        except:
          return random_card;
    
    
    def create_cards(self):
        
        for z in range(0, self.decks):
            for i in range(0,self.how_many_cards_each):
                for x in range(0, len(self.card_data)):
                    self.generated_cards.append(card_data[x]);
        random.shuffle(self.generated_cards);
        print(len(self.generated_cards));