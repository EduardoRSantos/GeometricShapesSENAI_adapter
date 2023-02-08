from quadrado import Quadrado
from circulo import Circulo
from quadrado_circulo import QuadradoParaCirculo

quadrado = Quadrado(5)
quadrado_para_circulo = QuadradoParaCirculo(quadrado)

print(f"Resultado do calculo do Quadrado: {quadrado.calcular_area()}")
print(f"Resultado do calculo do Circulo: {Circulo().raio(quadrado_para_circulo):.2f}")