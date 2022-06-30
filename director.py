
from card import Card

class Director:

    def __init__(self):
        
        self.is_playing = True
        self.score = 300


    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        roll_dice = input("Play again? y/n ")
        self.is_playing = (roll_dice == "y")

        user_input = ('Higher or Lower? (h/l')


        pass 


    def do_updates(self,user_input):
        card_number = Card.card()
        new_card = Card.card()
        
        if card_number > new_card:
            if user_input == 'l':
                self.score = self.score + 100
            else:
                self.score = self.score - 75

        elif card_number < new_card:
            if user_input == 'l':
                self.score = self.score + 100
            else:
                self.score = self.score - 75

        if not self.is_playing:
            return 



    def do_outputs(self):
        if not self.is_playing:
            return 

        #display score 

        self.is_playing == (self.score > 0)


    
