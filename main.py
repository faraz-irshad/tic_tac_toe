import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HIEGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
pygame.display.set_caption('TIC TAC TOE')

icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

zero_icon = pygame.image.load('Images/zero.png')
cross_icon = pygame.image.load('Images/cross.png')

zero_w, zero_h = 100, 100
cross_w, cross_h = 100, 100

zero = pygame.transform.scale(zero_icon, (zero_w, zero_h))
cross = pygame.transform.scale(cross_icon, (cross_w, cross_h))

class Board:

    def __init__(self, user_obj, computer_obj):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.user = user_obj
        self.computer = computer_obj

    def display_grid(self):
        blockSize = 150
        for x in range(75, SCREEN_WIDTH - 75, blockSize):
            for y in range(75, SCREEN_HIEGHT - 225, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
        pygame.display.update()

    def mark(self, symbol, n):
        if (n == None):
            return

        self.board[n - 1] = symbol

        x, y = 0, 0

        if (n == 1):
            x, y = 100, 100
        elif (n == 2):
            x, y = 250, 100
        elif (n == 3):
            x, y = 400, 100
        elif (n == 4):
            x, y = 100, 250
        elif (n == 5):
            x, y = 250, 250
        elif (n == 6):
            x, y = 400, 250
        elif (n == 7):
            x, y = 100, 400
        elif (n == 8):
            x, y = 250, 400
        elif (n == 9):
            x, y = 400, 400

        if (symbol == 'X'):
            screen.blit(cross, (x, y))
        elif (symbol == "0"):
            screen.blit(zero, (x, y))
        
        pygame.display.update()

    def is_draw(self):
        for i in self.board:
            if (str(type(i)) == "<class 'int'>"):
                return False
        
        self.winner_declaration("Draw")
        return True

    def winning_condition(self):

        symbol = '0'

        if self.board[0] == self.board[1] == self.board[2] == symbol:
            self.winner_declaration("Computer")
            return
        if self.board[3] == self.board[4] == self.board[5] == symbol:
            self.winner_declaration("Computer")
            return
        if self.board[6] == self.board[7] == self.board[8] == symbol:
            self.winner_declaration("Computer")
            return
        
        if self.board[0] == self.board[3] == self.board[6] == symbol:
            self.winner_declaration("Computer")
            return
        if self.board[1] == self.board[4] == self.board[7] == symbol:
            self.winner_declaration("Computer")
            return
        if self.board[2] == self.board[5] == self.board[8] == symbol:
            self.winner_declaration("Computer")
            return

        if self.board[0] == self.board[4] == self.board[8] == symbol:
            self.winner_declaration("Computer")
            return
        if self.board[2] == self.board[4] == self.board[6] == symbol:
            self.winner_declaration("Computer")
            return
        
        symbol = 'X'

        if self.board[0] == self.board[1] == self.board[2] == symbol:
            self.winner_declaration("You")
            return
        if self.board[3] == self.board[4] == self.board[5] == symbol:
            self.winner_declaration("You")
            return
        if self.board[6] == self.board[7] == self.board[8] == symbol:
            self.winner_declaration("You")
            return
        
        if self.board[0] == self.board[3] == self.board[6] == symbol:
            self.winner_declaration("You")
            return
        if self.board[1] == self.board[4] == self.board[7] == symbol:
            self.winner_declaration("You")
            return
        if self.board[2] == self.board[5] == self.board[8] == symbol:
            self.winner_declaration("You")
            return

        if self.board[0] == self.board[4] == self.board[8] == symbol:
            self.winner_declaration("You")
            return
        if self.board[2] == self.board[4] == self.board[6] == symbol:
            self.winner_declaration("You")
            return
        
    def winner_declaration(self, winner):
        for alpha in range(0, 255, 10):  
            fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HIEGHT))
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(alpha) 
            screen.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(30) 

        screen.fill((0, 0, 0))  

        font = pygame.font.Font(None, 74)

        if (winner == "Draw"):
            msg = "It's a Draw!!!"
        else:
            msg = f"{winner} won!!!"

        text_surface = font.render(msg, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HIEGHT // 3))
        screen.blit(text_surface, text_rect)

        button_font = pygame.font.Font(None, 50)
        button_text = button_font.render("Restart", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HIEGHT // 1.5))
        screen.blit(button_text, button_rect)
        
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        self.reset_game()
                        return

    def user_turn(self):
        self.mark('X', self.user.turn(self.board))

    def computer_turn(self):
        self.mark('0', self.computer.turn(self.board))

    def toss(self):
        return random.randrange(0, 2)
    
    def game_play(self):
        if (self.toss() == 0):
            while True:
                self.computer_turn()

                if (self.winning_condition()):
                    sys.exit()
                elif (self.is_draw()):
                    sys.exit()

                self.user_turn()

                if (self.winning_condition()):
                    sys.exit()
                elif (self.is_draw()):
                    sys.exit()        
        else:
            while True:
                self.user_turn()

                if (self.winning_condition()):
                    sys.exit()
                elif (self.is_draw()):
                    sys.exit()

                self.computer_turn()

                if (self.winning_condition()):
                    sys.exit()
                elif (self.is_draw()):
                    sys.exit()        
            
    def reset_game(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        screen.fill((0, 0, 0))  
        self.display_grid()
        pygame.display.update()
        self.game_play()

class User:

    def __init__(self):
        self.sign = cross_icon

    def quadrantClicked(self, x, y):
        if (y > 75 and y < 225):
            if (x > 75 and x < 225):
                return 1
            elif (x > 225 and x < 375):
                return 2
            elif (x > 375 and x < 525):
                return 3 
        elif (y > 225 and y < 375):
            if (x > 75 and x < 225):
                return 4
            elif (x > 225 and x < 375):
                return 5
            elif (x > 375 and x < 525):
                return 6
        elif (y > 375 and y < 525):
            if (x > 75 and x < 225):
                return 7
            elif (x > 225 and x < 375):
                return 8
            elif (x > 375 and x < 525):
                return 9
        
        return None

    def turn(self, board):
        turnDone = False

        while (not turnDone):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    q = self.quadrantClicked(x, y)
                    if (q != None):
                        if (board[q - 1] == q):
                            board[q - 1] = 'X'
                            turnDone = True
        
        return q

class Computer:

    def __init__(self):
        self.sign = zero_icon

    def check_win(self, symbol, board):
        if board[0] == board[1] == board[2] == symbol:
            return True
        if board[3] == board[4] == board[5] == symbol:
            return True
        if board[6] == board[7] == board[8] == symbol:
            return True
        
        if board[0] == board[3] == board[6] == symbol:
            return True
        if board[1] == board[4] == board[7] == symbol:
            return True
        if board[2] == board[5] == board[8] == symbol:
            return True

        if board[0] == board[4] == board[8] == symbol:
            return True
        if board[2] == board[4] == board[6] == symbol:
            return True
        
        return False

    def turn(self, board):
        for i in range(1, 10):
            if board[i - 1] not in ['X', '0']:  
                board[i - 1] = '0'  
                if self.check_win('0', board): 
                    return i
                else:
                    board[i - 1] = i  
        
        for i in range(1, 10):
            if board[i - 1] not in ['X', '0']:  
                board[i - 1] = 'X'  
                if self.check_win('X', board):  
                    return i
                else:
                    board[i - 1] = i 

        empty_positions = [element for element in board if isinstance(element, int)]

        if empty_positions:
            return random.choice(empty_positions)

user = User()
computer = Computer()

board = Board(user, computer)
board.display_grid()
board.game_play()

pygame.quit()