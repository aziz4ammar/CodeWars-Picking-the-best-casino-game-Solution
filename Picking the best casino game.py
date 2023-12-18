from collections import namedtuple
Game = namedtuple("Game", ["name", "outcomes"])
def expected_value(outcomes):
    return sum(prob * reward for prob, reward in outcomes)
def find_best_game(games):
    best_game = None
    best_ev = float('-inf')
    for game in games:
        ev = expected_value(game.outcomes)
        if ev > best_ev:
            best_ev = ev
            best_game = game.name
    return best_game