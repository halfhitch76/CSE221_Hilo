
from pickle import TRUE
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
        play_again = input("Play again? y/n ")
        if play_again == "y":
            self.is_playing = True       
        else:
            self.is_playing = False


    def do_updates(self):

        if not self.is_playing:
            return 

        card_number = Card.card(Card)
        print(f'The card is {card_number}:')
        user_input = input('Higher or Lower? (h/l) ')
        new_card = Card.card(Card)
        print(f'Next card was {new_card}')

        #compares the input with the card
        if card_number > new_card:
            if user_input == 'l':
                self.score = self.score + 100
            elif user_input == 'h':
                self.score = self.score - 75

        elif card_number < new_card:
            if user_input == 'h':
                self.score = self.score + 100
            elif user_input == 'l':
                self.score = self.score - 75



    def do_outputs(self):

        if not self.is_playing:
            return

        score = self.score
        print(f'Your score is {score}:')

        if score < 0:
            self.is_playing = False

        else:
            self.is_playing = True
        
