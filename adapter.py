#Desafio
#Criar uma calculadora antiga que usa a função soma e depois aderir


class ImpressoraAntiga:
    """Classe antiga que imprime textos usando o método 'imprimir_texto'."""
    def imprimir_texto(self, texto):
        print(f"🖨️ Impressora Antiga: Imprimindo -> {texto}")


class ImpressoraNova:
    """Nova classe de impressora, com método diferente ('print_texto')."""
    def print_texto(self, texto):
        print(f"🖨️ Impressora Nova: Impressão moderna -> {texto}")


class AdaptadorImpressora:
    """Adapta a ImpressoraNova para ser compatível com o método da ImpressoraAntiga."""
    def __init__(self, impressora_nova):
        self.impressora_nova = impressora_nova

    def imprimir_texto(self, texto):
        # Redireciona a chamada para o método da ImpressoraNova
        self.impressora_nova.print_texto(texto)


# Testando o padrão Adapter
nova = ImpressoraNova()
adaptador = AdaptadorImpressora(nova)

# O adaptador permite usar a ImpressoraNova como se fosse a Antiga
adaptador.imprimir_texto("Olá, mundo!")
