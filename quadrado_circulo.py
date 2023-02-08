from quadrado import Quadrado

class QuadradoParaCirculo:
    def __init__(self, quadrado: Quadrado) -> None:
        self.quadrado = quadrado
    
    def calcular_area(self):
        return 2 * 3.14 * self.quadrado.lado