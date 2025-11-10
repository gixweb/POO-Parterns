#Desafio
#

class Loja:
    def __init__(self):
        # Lista que armazena os clientes (observadores)
        self.clientes = []

    def adicionar_cliente(self, cliente):
        """Adiciona um cliente à lista de observadores."""
        self.clientes.append(cliente)

    def nova_promocao(self, produto):
        """Notifica todos os clientes sobre uma nova promoção."""
        print(f"\n📢 Nova promoção: {produto}!\nNotificando clientes...\n")
        for cliente in self.clientes:
            cliente.receber_notificacao(produto)


class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def receber_notificacao(self, produto):
        """Recebe a notificação da loja."""
        print(f"✅ {self.nome} recebeu promoção: {produto}")


# Testando o padrão Observer
loja = Loja()

joao = Cliente("João")
maria = Cliente("Maria")
ana = Cliente("Ana")

loja.adicionar_cliente(joao)
loja.adicionar_cliente(maria)
loja.adicionar_cliente(ana)

# Nova promoção
loja.nova_promocao("Notebook Gamer")
