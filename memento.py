

class Memento:
    def __init__(self, texto):
        self.texto = texto

class Editor:
    def __init__(self):
        self.texto = ""

    def escrever(self, novo):
        self.texto += novo

    def salvar(self):
        return Memento(self.texto)

    def restaurar(self, memento):
        self.texto = memento.texto

editor = Editor()
editor.escrever("X: -923 ")
salvo = editor.salvar()
editor.escrever("Y: 000")
print(editor.texto)
editor.restaurar(salvo)
print(editor.texto)