import numpy as np
import random


class subject:
    positions = np.zeros(8, dtype=int)
    board = np.zeros((8, 8), dtype=int)
    fitness = 0

    def __init__(self):
        for i in range(len(self.positions)):
            self.positions[i] = random.randint(1, 8)

    def queenspositions(self):

        for i in range(len(self.positions)):
            self.board[self.positions[i] - 1][i] = -1
        return self

    def evalboard(self):

        ## Verifica rainhas que se atacam na horizontal
        for qiIndex, qi in enumerate(self.positions): # qiIndex: coluna da rainha ; qi: linha que se encontra a rainha
            coluna = 1
            for qj in range(1, 9): # linha de uma rainha fixa -> percorre colunas
                if self.board[qi - 1][coluna - 1] == -1 and coluna != qiIndex + 1: #self.board|positions starts at index 1
                    self.fitness = self.fitness + 1
                    #print(f"HORIZONTAL -> col {coluna} qi {qi} qj {qj}")
                coluna = coluna + 1
            coluna = 1
        
        ## Verifica rainhas que se atacam na diagonal secundaria
        for qiIndex, qi in enumerate(self.positions):
            posqi = qi
            posqj = qiIndex + 1
            while posqi > 1 and posqj < 8:
                posqi = posqi - 1
                posqj = posqj + 1

            while posqi <= 8 and posqj >= 1:
                if self.board[posqi - 1][posqj - 1] == -1 and posqi != qi and posqj != qiIndex + 1:
                    self.fitness = self.fitness + 1
                    #print(f'posqi {posqi} posqj {posqj}')
                posqi = posqi + 1
                posqj = posqj - 1

        ## Verifica rainhas que se atacam na diagonal primaria
        for qiIndex, qi in enumerate(self.positions):
            posqi = qi
            posqj = qiIndex + 1
            while posqi < 8 and posqj < 8:
                posqi = posqi + 1
                posqj = posqj + 1

            while posqi >= 1 and posqj >= 1:
                if self.board[posqi - 1][posqj - 1] == -1 and posqi != qi and posqj != qiIndex + 1:
                    self.fitness = self.fitness + 1
                    #print(f'posqi {posqi} posqj {posqj}')
                posqi = posqi - 1
                posqj = posqj - 1

        return self

    def getFitness(self):
        return f'Número de ataques (h) = {self.fitness / 2}'
    
test = subject()

test.queenspositions()
print(test.board)
test.evalboard()
print(test.getFitness())