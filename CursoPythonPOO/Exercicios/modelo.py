#########################################################
#               CURSO PYTHON 3 - ALURA
#
#   Curso: Python Orientação a objetos.
#   Assunto: Classes, getters, setters, property
#
#
#########################################################

class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano 
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
       self.__likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano}: {self.likes}'

class Filme(Programa): 
    def __init__(self, nome, ano, duracao):
        self.duracao = duracao
        super().__init__(nome, ano)
   
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao}  Likes: {self.likes}'

class Serie(Programa):    
    def __init__(self, nome, ano, temporadas):
        self.temporadas = temporadas
        super().__init__(nome, ano)
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}'


class Playlist(list): #Herdando a classe de list
    def __init__(self, nome, programas):
        self.nome = nome 
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2019, 2)
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for item in playlist_fim_de_semana.listagem:
    print(item)