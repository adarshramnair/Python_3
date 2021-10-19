from random import shuffle
import os

# To clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('_______BlackJack_______\n\n')

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        shuffle(self.deck)

    def remove_card(self):
        return self.deck.pop()

def no_of_ace(ranks):
    count = 0
    for x in ranks:
        if x == 'Ace':
            count += 1

    return count

class Playing_person:

    def __init__(self, name):
        self.name = name
        self.card_list = []
        self.rank_list = []
        self.value_list = []
        self.total_value = 0
        self.display_value = 0

    def add_cards(self, card):
        self.card_list.append(card)
        self.rank_list.append(card.rank)
        self.value_list.append(card.value)

        self.total_value = sum(self.value_list)

        if self.total_value > 21:
            self.aces_count = no_of_ace(self.rank_list)
            for x in range(0,self.aces_count):
                self.total_value -= 10
                if self.total_value <= 21:
                    break
        # For Dealer, in the first turn, the other card should be hid hence only first card value is shown only if it's not a BJ
        # Only for the required condition
        self.dsiplay_value = self.value_list[0]

    def value_of_cards(self, result):
        # For Dealer, in the first turn, the other card should be hid hence only first card value is shown only if it's not a BJ
        if ((self.name == 'Dealer' and self.total_value != 21) and len(self.card_list) == 2 and result.result == None):
            print(f'{self.name}\'s Total Value = {str(self.value_list[0])}')
        else:
            print(f'{self.name}\'s Total Value = {self.total_value}')


    def print_player_cards(self, result):
        print(f'{self.name} has the following cards:')
        # For Dealer, in the first turn, the other card should be hid hence only first card is shown only if it's not a BJ
        if ((self.name == 'Dealer' and self.total_value != 21) and len(self.card_list) == 2 and result.result == None):
            print(self.card_list[0])
        else:
            for card in self.card_list:
                print(card)

class Bet_account:
    def __init__(self, name):
        self.name = name
        self.balance = 100

    def bet(self):
        self.balance -= 10

    def win(self):
        self.balance += 20

    def tie(self):
        self.balance += 10

    def __str__(self):
        return f'{self.name} has {self.balance} chips left.'

class Player_result:
    def __init__(self):
        self.result = None
        self.reason = ''

    def win_or_lose(self, result, reason, chips):
        self.result = result
        self.reason = reason
        if self.result == 'Win':
            chips.win()
        elif self.result == 'Tie':
            chips.tie()
        elif self.result == 'Loose':
            pass

    def printing(self, player):
        print(self.reason + '\n' + f'{player.name} ' + f'{self.result}s' )


def print_info(player, dealer, result):
    for x in [player, dealer]:
        x.print_player_cards(result)
        x.value_of_cards(result)
        print('\n')

def black_jack(player, dealer, chips, result):
    clear_screen()
    #print(chips)
    print_info(player, dealer, result)
    if player.total_value == dealer.total_value == 21:
        result.win_or_lose('Tie', 'Both has 21 points in the first turn, So it\'s a tie', chips)
    elif player.total_value == 21:
        result.win_or_lose('Win', f'{player.name} has a BlackJack !!!', chips)
    elif dealer.total_value == 21:
        result.win_or_lose('Loose', 'Dealer has a BlackJack !!!', chips)


def player_plays(card_deck, player, dealer, chips, result):

    while True:
        if player.total_value > 21:
            result.win_or_lose('Loose', f'{player.name} Busts', chips)
            break
        elif player.total_value == 21:
            break

        while True:
            hit_stand = (input('Hit (h) or Stand (s)?: ')).upper()
            if (hit_stand == 'H' or hit_stand == 'S'):
                break
            else:
                continue

        if hit_stand == 'H':
            player.add_cards(card_deck.remove_card())
            clear_screen()
            #print(chips)
            print_info(player, dealer, result)

        elif hit_stand == 'S':
            break

def dealer_plays(card_deck, player, dealer, chips, result):

    while True:

        if dealer.total_value > 21:
            result.win_or_lose('Win', 'Dealer Busts', chips)
            break
        elif dealer.total_value > 17:
            break

        dealer.add_cards(card_deck.remove_card())
        clear_screen()
        #print(chips)
        print_info(player, dealer, result)

def player_win_1(player, dealer):
    if player.total_value > 21:
        return False
    elif dealer.total_value > 21:
        return True
    else:
        return None

def player_win_2():
    if player.total_value > dealer.total_value:
        return True
    elif player.total_value < dealer.total_value:
        return False
    else:
        return None


def game():
    game_stage_1 = True



    while game_stage_1:

        clear_screen()
        print('Player will have 100 chips to play.\nEach bet cost 10 chips.')
        print('Winning wll earn 20 chips.\nTie games will give back your 10 chips.')
        print('Lost bets will loose the 10 chips.\n')
        player_name = input('Enter the Player\'s name: ')

        player = Playing_person(player_name)
        dealer = Playing_person('Dealer')

        game_stage_2 = True

        while game_stage_2:
            chips = Bet_account(player_name)
            clear_screen()
            #print(chips)
            print('\n')

            game_stage_3 = True

            while game_stage_3:
                result = Player_result()
                card_deck = Deck()
                card_deck.shuffle()
                player = Playing_person(player_name)
                dealer = Playing_person('Dealer')

                clear_screen()
                print(chips)
                chips.bet()
                print('\n')
                if chips.balance < 0:
                    print(f'{player_name} doesn\'t have enough chips to play')
                    while True:
                        reset_bet = (input('RESET (r) chips, PLAY a new game (p) or QUIT (q) game: ')).upper()
                        if reset_bet == 'R':
                            break
                        elif reset_bet == 'P':
                            game_stage_2 = False
                            break
                        elif reset_bet == 'Q':
                            game_stage_2 = False
                            game_stage_1 = False
                            break
                        else:
                            continue
                    break

                # Initial 2 cards
                for x in range(2):
                    player.add_cards(card_deck.remove_card())
                    dealer.add_cards(card_deck.remove_card())

                black_jack(player, dealer, chips, result)
                if result.result != None:
                    clear_screen()
                    #print(chips)
                    print_info(player, dealer, result)
                    result.printing(player)

                    while True:
                        print(chips)
                        continue_game = (input('CONTINUE (c) game, RESET (r) chips, PLAY a new game (p) or QUIT (q) game: ')).upper()
                        if continue_game != 'C' and continue_game != 'R' and continue_game != 'P' and continue_game != 'Q':
                            continue
                        elif continue_game == 'C':
                            break
                        elif continue_game == 'R':
                            game_stage_3 = False
                            break
                        elif continue_game == 'P':
                            game_stage_3 = False
                            game_stage_2 = False
                            break
                        elif continue_game == 'Q':
                            game_stage_3 = False
                            game_stage_2 = False
                            game_stage_1 = False
                            break
                    if continue_game == 'C':
                        continue
                    break

                player_plays(card_deck, player, dealer, chips, result)
                if result.result != None:
                    clear_screen()
                    #print(chips)
                    print_info(player, dealer, result)
                    result.printing(player)

                    while True:
                        print(chips)
                        continue_game = (input('CONTINUE (c) game, RESET (r) chips, PLAY a new game (p) or QUIT (q) game: ')).upper()
                        if continue_game != 'C' and continue_game != 'R' and continue_game != 'P' and continue_game != 'Q':
                            continue
                        elif continue_game == 'C':
                            break
                        elif continue_game == 'R':
                            game_stage_3 = False
                            break
                        elif continue_game == 'P':
                            game_stage_3 = False
                            game_stage_2 = False
                            break
                        elif continue_game == 'Q':
                            game_stage_3 = False
                            game_stage_2 = False
                            game_stage_1 = False
                            break
                    if continue_game == 'C':
                        continue
                    break

                dealer_plays(card_deck, player, dealer, chips, result)
                if result.result != None:
                    clear_screen()
                    #print(chips)
                    print_info(player, dealer, result)
                    result.printing(player)

                    while True:
                        print(chips)
                        continue_game = (input('CONTINUE (c) game, RESET (r) chips, PLAY a new game (p) or QUIT (q) game: ')).upper()
                        if continue_game != 'C' and continue_game != 'R' and continue_game != 'P' and continue_game != 'Q':
                            continue
                        elif continue_game == 'C':
                            break
                        elif continue_game == 'R':
                            game_stage_3 = False
                            break
                        elif continue_game == 'P':
                            game_stage_3 = False
                            game_stage_2 = False
                            break
                        elif continue_game == 'Q':
                            game_stage_3 = False
                            game_stage_2 = False
                            game_stage_1 = False
                            break
                    if continue_game == 'C':
                        continue
                    break

                if player.total_value == dealer.total_value:
                    result.win_or_lose('Tie', f'Both has {player.total_value} points in the first turn, So it\'s a tie', chips)
                elif player.total_value > dealer.total_value:
                    result.win_or_lose('Win', f'{player.name} has more points than Dealer !!!', chips)
                elif player.total_value < dealer.total_value:
                    result.win_or_lose('Loose', f'Dealer has more points than {player.name} !!!', chips)

                clear_screen()
                #print(chips)
                print_info(player, dealer, result)
                result.printing(player)

                while True:
                    print(chips)
                    continue_game = (input('CONTINUE (c) game, RESET (r) chips, PLAY a new game (p) or QUIT (q) game: ')).upper()
                    if continue_game != 'C' and continue_game != 'R' and continue_game != 'P' and continue_game != 'Q':
                        continue
                    elif continue_game == 'C':
                        break
                    elif continue_game == 'R':
                        game_stage_3 = False
                        break
                    elif continue_game == 'P':
                        game_stage_3 = False
                        game_stage_2 = False
                        break
                    elif continue_game == 'Q':
                        game_stage_3 = False
                        game_stage_2 = False
                        game_stage_1 = False
                        break
                if continue_game == 'C':
                    continue
                break


game()
print('Thank you for playing the game !')
