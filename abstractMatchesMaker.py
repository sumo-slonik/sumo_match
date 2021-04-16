from abc import ABC, abstractmethod


class AbstractMatchesMaker(ABC):
    @abstractmethod
    def make_match(self):
        pass

    @abstractmethod
    def go_to_next_round(self):
        pass

    @abstractmethod
    def go_to_prev_round(self):
        pass

    @abstractmethod
    def get_actual_match_id(self):
        pass
