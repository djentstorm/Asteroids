class GameStats():
    """Track stats for F*ck Democracy"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start F*ck Democracy in an active state
        self.game_active = True

        #start game in an inactive state
        self.game_active = False

        #High score should never reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

