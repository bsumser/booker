from abc import ABC, abstractmethod
import pygame

class State(ABC):
    @abstractmethod
    def handle1(self):
        pass
    def handle2(self):
        pass

class MainMenuState(State):
    def handle1(self) -> None:
        print("MainMenuState handles request1.")
        print("MainMenuState wants to change the state of the context.")
        self.context.transition_to(SelectBookState())

    def handle2(self) -> None:
        print("MainMenuState handles request2.")

class SelectBookState(State):
    def handle1(self) -> None:
        print("SelectBookState handles request1.")
        print("SelectBookState wants to change the state of the context.")
        #self.context.transition_to(PlayBookState())

    def handle2(self) -> None:
        print("SelectBookState handles request2.")

# Context class:
class Context(ABC):
    _state = None
    def __init__(self, state):
        self.transition_to(state)
        self.stateLoop(state)
    
    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    def stateLoop(self, state):
        for event in pygame.event.get():
            if event.key in (pygame.K_j, pygame.K_k, pygame.K_l):
                f(event.key)

    def inputLoop(self):
        self._state.loop()
    def request1(self):
        self._state.handle1()
    def request2(self):
        self._state.handle2()

if __name__ == "__main__":
    pygame.init()
    pygame.display.iconify()
    context = Context(MainMenuState())
    context.request1()
    context.request2()