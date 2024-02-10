import random
import settings as sett
from card import Card
import pygame

class Player:
    """
    The player class will have a hand a control the logic of playing and drawing cards
    """

    def __init__(self, group: pygame.sprite.Group) -> None:
        
        self.hand = list()
        self.pos = (150, 900)
        self.initial_hand_size = 10
        self.group = group
        self.draw_initial_hand()

    def draw_initial_hand(self):
        # for now lets just randomly get some cards
        for i in range(self.initial_hand_size):
            suit = random.choice(sett.suits)
            value = random.choice(list(sett.card_values_dict.keys()))
            card_pos = (self.pos[0]+110*i, self.pos[1])
            self.hand.append(Card(suit, value, self.group, pos=card_pos))


    def sort_hand(self):
        """
        Orders players hand, first by suit and then by value
        """

        print("SORTING")

        #TODO optimize later, clean go-horse
        #TODO the z-index remains the same as in creation and must either be changed or add more breathing room
        ordered_hand = list()
        for suit in sett.suits:
            suits_hand = list()
            for card in self.hand:
                if card.suit == suit:
                    suits_hand.append(card)

            # order by value
            suits_hand = sorted(suits_hand, key=lambda x: x.value_number)
            ordered_hand.extend(suits_hand)

        self.hand = ordered_hand
        for idx, card in enumerate(self.hand):
            card_pos = (self.pos[0]+110*idx, self.pos[1])
            card.update_position(card_pos)
            card.is_clicked = False




    # def display_hand(self):
    #     for card in self.hand:
            
    
    def update(self, event_list):
        for event in event_list:
            for card in self.hand:
                card.handle_event(event)

            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_LEFT:
                    self.sort_hand()