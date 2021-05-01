from dlgo import goboard
from dlgo.agent.base import Agent
from dlgo import scoring

class TerminationStrategy:
    def __init__(self):
        pass

    def should_pass(self, game_state):
        return False

    def should_resign(self, game_state):
        return False

class PassWhenOpponentPasses(TerminationStrategy):
    def should_pass(self, game_state):
        if game_state.last_move is not None:
            return True if game_state.last_move.is_pass else False

class ResignLargeMargin(TerminationStrategy):
    def should_resign:
        pass
        #implement later

def get(termination):
    if termination == 'opponent_passes':
        return PassWhenOpponentPasses()
    else:
        raise ValueError("Unsupported termination strategy: {}".format(termination))

class TerminationAgent(Agent):
    def __init__(self, agent, strategy=None):
        Agent.__init__(self)
        self.agent = agent
        self.strategy = strategy if strategy is not None else TerminationStrategy()