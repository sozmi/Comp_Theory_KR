from abc import ABCMeta, abstractmethod

class AlgObject(metaclass=ABCMeta):
    @abstractmethod
    def translate(self, gr):
        """Перевод графа"""
