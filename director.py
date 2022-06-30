from card import Card

class Director:

    def __init__(self):
        
        self.dice = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0



    def start_game(self):

        while self.is_playing():
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass 


    def do_updates(self):
        pass

    def do_outputs(self):
        pass

    
