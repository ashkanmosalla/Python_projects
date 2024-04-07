import random


class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.name = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f'Invalid choice!, please select one of ({self.choices})')
        return self.get_player_choice()
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        win_combination = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
        for win_comb in win_combination:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congrats! You Won"
            
            return "Oh no! Computer Won the Game"
        
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_mesg = self.decide_winner(user_choice, computer_choice)
        print(f'Computer_choice: {computer_choice}')
        print(winner_mesg)

if __name__ == '__main__':
    game = RockPaperScissors('ashkan')

while True:
    game.play()

    continue_game = input('Press any key to play again!, Enter Q/q to exit')
    if continue_game.lower() == 'q':
        break
