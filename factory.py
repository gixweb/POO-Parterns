#Desafio
#Criar uma fábrica de motos e carros
#Criar uma fábrica de pagamentos

class Veiculo:
    def ronco(self):
        pass

class Carro(Veiculo):
    def ronco(self):
        return "Vrum Vrum"

class Moto(Veiculo):
    def ronco(self):
        return "Randandandan"

class VeiculoFactory:
    @staticmethod
    def criar(tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "moto":
            return Moto()
        else:
            raise ValueError("Tipo desconhecido")

# Exemplo de uso
Veiculo = VeiculoFactory.criar("cachorro")
print(Veiculo.ronco())