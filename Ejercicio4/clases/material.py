from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def puntos(self, kg):
        pass

    @abstractmethod
    def max_kg_por_bolsa(self):
        pass

class Plastico(Material):
    def puntos(self, kg):
        return kg * 5

    def max_kg_por_bolsa(self):
        return 8

class Vidrio(Material):
    def puntos(self, kg):
        return kg * 2

    def max_kg_por_bolsa(self):
        return 5

class PapelCarton(Material):
    def puntos(self, kg):
        return kg * 3
