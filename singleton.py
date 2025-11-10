#
#

class Configuracao:
    _instancia = None  # Armazena a única instância da classe

    def __new__(cls):
        # Verifica se já existe uma instância criada
        if cls._instancia is None:
            # Cria a instância apenas uma vez
            cls._instancia = super().__new__(cls)
            cls._instancia.valor = "Padrão"
        # Retorna sempre a mesma instância
        return cls._instancia


# Testando o Singleton
a = Configuracao()
b = Configuracao()

print(a is b)  # True → a e b apontam para o mesmo objeto
print(a.valor)  # Padrão
b.valor = "Alterado"
print(a.valor)  # Alterado (mesma instância)