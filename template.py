import sys
import pygame as pg
import constants
import player
import ball
import brick


class Game(object):
    """
    A single instance of this class is responsible for
    managing which individual game state is active
    and keeping it updated. It also handles many of
    pygame's nuts and bolts (managing the event
    queue, framerate, updating the display, etc.).
    and its run method serves as the "game loop".
    """
    def __init__(self, screen, states, start_state):
        """
        Initialize the Game object.

        screen: the pygame display surface
        states: a dict mapping state-names to GameState objects
        start_state: name of the first active game state
        """
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        """
        Check for state flip and update active state.

        dt: milliseconds since last frame
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font("vgafix.fon", 50)

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit = True

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass


class SplashScreen(GameState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.main_font = pg.font.Font("vgafix.fon", 50)
        self.title_text = self.main_font.render("Breakout", 0, (50, 50, 25))
        self.persist["screen_color"] = constants.BLACK
        self.next_state = "GAMEPLAY"

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.persist["screen_color"] = constants.BLACK
            self.done = True

    def draw(self, surface):
        surface.fill(constants.BLUE)
        surface.blit(self.title_text, (5, 10))


class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.player = player.Player()
        self.ball = ball.Ball(self.player)
        self.all_sprites = constants.all_sprites
        self.brick_sprites = constants.brick_sprites
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ball)
        self.level_1()

    def startup(self, persistent):
        self.persist = persistent
        color = self.persist["screen_color"]
        self.screen_color = color

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        self.all_sprites.update()
        self.brick_sprites.update()

    def draw(self, surface):
        surface.fill(self.screen_color)
        self.all_sprites.draw(screen)
        self.brick_sprites.draw(screen)

    def level_1(self):
        for r in range(3):
            for i in range(20):
                brick_img = brick.Brick((i * 64) + 10, (r * 32 + 20), img_path=constants.BLUE_DIR)
                self.brick_sprites.add(brick_img)

if __name__ == "__main__":
    pg.init()
    screen = constants.SCREEN
    states = {"SPLASH": SplashScreen(),
              "GAMEPLAY": Gameplay()}
    game = Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()
