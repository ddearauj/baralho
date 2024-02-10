import pygame
import settings as sett

def transformScaleKeepRatio(image, scale):
    iwidth, iheight = image.get_size()
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.smoothscale(image, new_size) 
    return scaled_image

class Card(pygame.sprite.Sprite):
    """
    The card will be a simple class that contains the card info and the sprite
    Later on it will be selectable and playable

    TODO: think of pathing
    """

    def __init__(self, suit, value, group, pos):
        super().__init__(group)

        self.image = pygame.image.load(f"./assets/cards/{suit}_{value}.png").convert_alpha()
        self.image = transformScaleKeepRatio(self.image, 3)
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(pos[0], pos[1])
        self.initial_y = pos[1]
        self.rect.center = self.pos
        self.is_clicked = False
        self.value_number = sett.card_values_dict[value]
        self.suit = suit

    def handle_event(self, event):
        """
        Check if it was clicked
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("clicked")
                if self.is_clicked == False:
                    self.pos[1] = self.initial_y - 20
                    self.rect.center = self.pos
                    self.is_clicked = True

            else:
                if self.is_clicked == True:
                    self.pos[1] = self.initial_y
                    self.rect.center = self.pos
                    self.is_clicked = False
                

    def update_colision(self):
        pass

    def update(self, dt):
        pass

    def update_position(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = self.initial_y
        self.rect.center = self.pos


# # Do we need a class for the hand? Maybe just a list?
# class Hand