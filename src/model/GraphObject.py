from abc import ABCMeta, abstractmethod

class GraphObject (metaclass=ABCMeta):

    def draw(self, surface):
        """нарисовать объект"""
    # @abstractmethod
    def update(self):
        """обновить объект"""

    def get_event(self, ev):
       """получить событие"""