import pygame


class Input_Manager(object):

    def __init__(self):
        self.MOV_UP = False
        self.MOV_UP_KEYS = [pygame.K_w, pygame.K_UP]
        self.MOV_DOWN = False
        self.MOV_DOWN_KEYS = [pygame.K_s, pygame.K_DOWN]
        self.MOV_LEFT = False
        self.MOV_LEFT_KEYS = [pygame.K_a, pygame.K_LEFT]
        self.MOV_RIGHT = False
        self.MOV_RIGHT_KEYS = [pygame.K_d, pygame.K_RIGHT]

        self.ACTION_ATTACK = False
        self.ACTION_ATTACK_KEYS = [pygame.K_SPACE,
                                   pygame.K_KP_ENTER,
                                   pygame.K_RETURN]

    def update_keys(self):
        if pygame.key.get_focused():
            self._clear_input()
            pressed = pygame.key.get_pressed()
            for key in self.MOV_UP_KEYS:
                if pressed[key]:
                    self.MOV_UP = True
            for key in self.MOV_DOWN_KEYS:
                if pressed[key]:
                    self.MOV_DOWN = True
            for key in self.MOV_LEFT_KEYS:
                if pressed[key]:
                    self.MOV_LEFT = True
            for key in self.MOV_RIGHT_KEYS:
                if pressed[key]:
                    self.MOV_RIGHT = True
            for key in self.ACTION_ATTACK_KEYS:
                if pressed[key]:
                    self.ACTION_ATTACK = True

    def _clear_input(self):
        self.MOV_UP = False
        self.MOV_DOWN = False
        self.MOV_LEFT = False
        self.MOV_RIGHT = False

        self.ACTION_ATTACK = False


manager = Input_Manager()
