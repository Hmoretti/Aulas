class Mamiferos():
    olhos = 2
    patas = 4

    def __init__(self, pelo, especie, rabo , cor):
       self.pelo = pelo 
       self.especie = especie
       self.rabo = rabo
       self.cor = cor

    def comer(self):
        print('comi')
    def fazer_som(self):
        print('som')

mamifero = Mamiferos('curto', 'doguinhos caninos', True, 'caramelo')
mamifero2 = Mamiferos('longo', 'agrarious monatas', False, 'purple')

mamifero.comer()
mamifero2.fazer_som()

print(mamifero.especie)
print(mamifero2.especie)
