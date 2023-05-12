import pygame
import sys


class PongGame():
    def __init__(self):
        # Initializes pygame library
        pygame.init()
        self.clock = pygame.time.Clock()

        # Screen settings configuration
        self.screen_width = 800
        self.screen_height = 600
        self.__screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong Game")

        # Game entities shapes
        self.__game_ball = pygame.Rect(self.screen_width / 2 - 15,
                                       self.screen_height / 2 - 15, 30, 30)

        # Rectangles belonging to current player right and bottom
        self.__player_rec_one = pygame.Rect(
            self.screen_width - 20, self.screen_height / 2 - 70, 10, 140)
        self.__player_rec_two = pygame.Rect(
            self.screen_width / 2 - 70, self.screen_height - 20, 140, 10)

        # Rectangles belonging to opponent Left and Top
        self.__opponent_rec_one = pygame.Rect(
            10, self.screen_height / 2 - 70, 10, 140)
        self.__opponent_rec_two = pygame.Rect(
            self.screen_width / 2 - 70, 10, 140, 10)

        # screen and rectangle color settings
        self.__bg_color = pygame.Color("grey12")
        self.__light_grey = (200, 200, 200)

        self.game_ball_speed_x = 7
        self.game_ball_speed_y = 7
        self.__PLAYERSPEEDCONSTANT = 7
        self.__player_rec_one_speed = 0  # speed used for both players
        self.__player_rec_two_speed = 0  # speed used for both players
        self.__opponent_rec_one_speed = 7  # speed used for both players
        self.__opponent_rec_two_speed = 7  # speed used for both players

        self.__player_score = 0
        self.__opponent_score = 0
        self.game_font = pygame.font.Font("freesansbold.ttf", 14)

    def start_game(self):
        # Starts game
        while True:
            # Event handler
            for event in pygame.event.get():
                # Ends and close game window when user clicks button to close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Up and Down arrow key movements
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.__player_rec_one_speed += self.__PLAYERSPEEDCONSTANT
                    if event.key == pygame.K_UP:
                        self.__player_rec_one_speed -= self.__PLAYERSPEEDCONSTANT

                    if event.key == pygame.K_RIGHT:
                        self.__player_rec_two_speed += self.__PLAYERSPEEDCONSTANT
                    if event.key == pygame.K_LEFT:
                        self.__player_rec_two_speed -= self.__PLAYERSPEEDCONSTANT

                # Left and Right arrow key movements
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.__player_rec_one_speed -= self.__PLAYERSPEEDCONSTANT
                    if event.key == pygame.K_UP:
                        self.__player_rec_one_speed += self.__PLAYERSPEEDCONSTANT

                    if event.key == pygame.K_RIGHT:
                        self.__player_rec_two_speed -= self.__PLAYERSPEEDCONSTANT
                    if event.key == pygame.K_LEFT:
                        self.__player_rec_two_speed += self.__PLAYERSPEEDCONSTANT

            # Game ball animations
            self.ball_animations()
            # Player movement animation
            self.player_animations()
            # Opponent movement animation
            self.opponent_animarions()
            # Render game window
            self.render_pong_game()

            player_text = self.game_font.render(
                f"{self.__player_score}", False, self.__light_grey)
            self.__screen.blit(player_text, (410, 285))
            opponent_text = self.game_font.render(
                f"{self.__opponent_score}", False, self.__light_grey)
            self.__screen.blit(opponent_text, (375, 285))
            # updates window
            pygame.display.flip()
            self.clock.tick(60)

    def render_pong_game(self):
        # Render game entities
        self.__screen.fill(self.__bg_color)
        # renders player one
        pygame.draw.rect(self.__screen, self.__light_grey,
                         self.__player_rec_one)
        # renders player one
        pygame.draw.rect(self.__screen, self.__light_grey,
                         self.__player_rec_two)
        # renders opponent
        pygame.draw.rect(self.__screen, self.__light_grey,
                         self.__opponent_rec_one)
        # renders opponent
        pygame.draw.rect(self.__screen, self.__light_grey,
                         self.__opponent_rec_two)
        pygame.draw.ellipse(self.__screen, self.__light_grey,
                            self.__game_ball)  # render ball
        pygame.draw.aaline(self.__screen, self.__light_grey, (self.screen_width / 2,
                                                              0), (self.screen_width / 2, self.screen_height))  # renders horizontal middle line
        pygame.draw.aaline(self.__screen, self.__light_grey, (0, self.screen_height / 2),
                           (self.screen_width, self.screen_height / 2))  # renders vertical middle line

    def player_animations(self):
        # Updates value for player rectangle speed movement
        self.__player_rec_one.y += self.__player_rec_one_speed
        self.__player_rec_two.x += self.__player_rec_two_speed

        # Handles make suring player rectangle one does not go out of game screen size
        if self.__player_rec_one.top <= 0:
            self.__player_rec_one.top = 0
        if self.__player_rec_one.bottom >= self.screen_height:
            self.__player_rec_one.bottom = self.screen_height
        # Handles make suring player rectangle two does not go out of game screen size
        if self.__player_rec_two.left <= 0:
            self.__player_rec_two.left = 0
        if self.__player_rec_two.right >= self.screen_width:
            self.__player_rec_two.right = self.screen_width

    def opponent_animarions(self):
        # Set speed of left moving opponent rectangle
        if self.__opponent_rec_one.top < self.__game_ball.y:
            self.__opponent_rec_one.top += self.__opponent_rec_one_speed
        if self.__opponent_rec_one.bottom > self.__game_ball.y:
            self.__opponent_rec_one.bottom -= self.__opponent_rec_one_speed
        # Handles make suring opponent left rectangle does not go out of game screen size
        if self.__opponent_rec_one.top <= 0:
            self.__opponent_rec_one.top = 0
        if self.__opponent_rec_one.bottom >= self.screen_height:
            self.__opponent_rec_one.bottom = self.screen_height
        # Set speed of top moving opponent rectangle
        if self.__opponent_rec_two.left < self.__game_ball.x:
            self.__opponent_rec_two.left += self.__opponent_rec_two_speed
        if self.__opponent_rec_two.right > self.__game_ball.x:
            self.__opponent_rec_two.right -= self.__opponent_rec_two_speed
        # Handles make suring opponent top rectangle does not go out of game screen size
        if self.__opponent_rec_two.left <= 0:
            self.__opponent_rec_two.left = 0
        if self.__opponent_rec_two.right >= self.screen_width:
            self.__opponent_rec_two.right = self.screen_width

    def ball_animations(self):
        # Update ball speed
        self.__game_ball.x += self.game_ball_speed_x
        self.__game_ball.y += self.game_ball_speed_y

        # Reverse ball for vertical axis
        if self.__game_ball.top <= 0 or self.__game_ball.bottom >= self.screen_height:
            self.game_ball_speed_y *= -1
        # Update player score and restarts ball at center
        if self.__game_ball.left <= 0:
            self.__player_score += 1
            self.ball_restart()
        # Update opponent score and restart ball at center
        if self.__game_ball.right >= self.screen_width:
            self.__opponent_score += 1
            self.ball_restart()
        # Handles rectangle collisions with ball
        if self.__game_ball.colliderect(self.__player_rec_one) or self.__game_ball.colliderect(self.__opponent_rec_one):
            self.game_ball_speed_x *= -1
        if self.__game_ball.colliderect(self.__player_rec_two) or self.__game_ball.colliderect(self.__opponent_rec_two):
            self.game_ball_speed_y *= -1

    def ball_restart(self):
        # Game ball restarts to the center
        self.__game_ball.center = (
            self.screen_width / 2, self.screen_height / 2)


game = PongGame()
game.start_game()
