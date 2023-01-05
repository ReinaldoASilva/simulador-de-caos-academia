import random
import seaborn as sns

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 100) if i % 2 == 0]
        #criação dos halteres
        self.porta_halteres = {}
        #criação dos porta halteres
        self.reiniciar_o_dia()
        #toda vez que chamar essa função a academia volta ao normal

    def reiniciar_o_dia(self):
        #toda vez que chamar essa função a academia volta ao normal
        self.porta_halteres = {i:i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
        #retornar uma lista dos halteres que podem ser utilizados

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]
        #mostrar os espaços vazios
    
    def pegar_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        #pra saber qual o indice do valor no dicionário
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        #saber qual a chave 
        self.porta_halteres[key_halt] = 0
        #quando a pessoa pegar o peso ela transforma aquele espaço em 0
        return peso
    
    def devolver_halter(self, pos, peso):
        #saber qual a posição e qual peso estou devolvendo 
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        # mostrar os valores que estão fora do lugar
        return len(num_caos) / len(self.porta_halteres)
        #retornar quantos estão fora do lugar

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0
        #mostrar qual peso ele está segurando
        # criar dois tipos de elementos, um normal e o outro bagunçeiro

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        #lista de pesos na academia
        self.peso = random.choice(lista_pesos)
        #pegar os pesos de forma aleatória
        self.academia.pegar_haltere(self.peso)
        #pego o peso da academia

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            #usuário tipo 1 - normal
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
                #se o local do valor estiver vazio ele coloca no mesmo lugar
            else:
                #senão escolhe um local aleatório
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        
        if self.tipo == 2:
            # usuário tipo 2 - bagunçeiro
            pos = random.choice(espacos)
            #ele sempre devolve em espaços aleatórios
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0

academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
# 10 usuários normais
usuarios += [Usuario(2, academia) for i in range(1)]
# 1 usuário normal
random.shuffle(usuarios)
# bagunça a minha lista de usuários pra eu não saber em qual posição cada um está

list_chaos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
            #iniciar o treino de forma aleatória
        for user in usuarios:
            user.finalizar_treino()
             #finalizar o treino de forma aleatória
    list_chaos += [academia.calcular_caos()]
    #calcular quantos esão fora do lugar
    
        
#academia.porta_halteres
#academia.calcular_caos()

sns.displot(list_chaos)
#visualizar em um gráfico com a porcentagem do caos