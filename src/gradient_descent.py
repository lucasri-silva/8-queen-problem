import numpy as np
import random
import os

class subject:
    positions = np.zeros(8, dtype=int)
    board = np.zeros((8, 8), dtype=int)
    fitnessboard = np.zeros((8, 8), dtype=int)
    fitness = 0
    
    ## gera posições aleatórias das rainhas
    def generate_random_queens(self):
        
        for i in range(len(self.positions)):
            self.positions[i] = random.randint(1, 8)

    ## retorna vetor posição das rainhas
    def queens_coordinates(self):
        return self.positions

    # Posiciona rainhas (-1) no tabuleiro (matriz)
    def queenspositions(self):
        
        for i in range(len(self.positions)):
            for j in range(len(self.positions)):
                self.board[i][j] = 0

        for i in range(len(self.positions)):
            self.board[self.positions[i] - 1][i] = -1
        return self

    # Determina quantidade de rainhas que se atacam
    def evalboard(self):
        
        self.fitness = 0

        ## Verifica rainhas que se atacam na horizontal
        for qiIndex, qi in enumerate(self.positions):
            coluna = 1
            for qj in range(1, 9):
                if self.board[qi - 1][coluna - 1] == -1 and coluna != qiIndex + 1:
                    self.fitness = self.fitness + 1
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
                posqi = posqi - 1
                posqj = posqj - 1
        
        return self

    # retorna número de rainhas que se atacam
    def getFitness(self):
        return self.fitness / 2
    
    # Determina quantidade de rainhas que se atacam para cada posição do tabuleiro
    def evalsquares(self):
        
        positionsbackup = self.positions.copy()
        
        for i in range(len(self.positions)):
            
            for j in range(len(self.positions)):
                
                self.positions[i] = j + 1
                self.fitnessboard[j][i] = self.queenspositions().evalboard().fitness/2
                self.positions[i] = positionsbackup[i]
        self.queenspositions()
        return self
    
    # Posiciona rainhas no minimo global correspondente a sua coluna
    def gradient_descent(self):

        self.generate_random_queens()
        self.queenspositions()
        self.evalboard()
        self.evalsquares()
        iteracoes = 0

        while self.fitness > 1 and iteracoes < 25:

            ## percorre colunas horizontalmente
            for pos_j in range(len(self.positions)):
                
                self.evalsquares() ## determina h para cada posicao
                pos_i = 0
                min = self.fitnessboard[pos_i][pos_j]
                
                ## percorre coluna atual verticalmente
                for i in range(len(self.positions)):

                    if self.fitnessboard[i][pos_j] < min:
                        min = self.fitnessboard[i][pos_j]
                        pos_i = i

                iteracoes += 1
                os.system('clear')
                print(f'Iterações = {iteracoes}')
                
                self.board[self.positions[pos_j] - 1][pos_j] = 0 # remove rainha do local atual
                self.board[pos_i][pos_j] = -1 # posiciona rainha no minimo local
                self.positions[pos_j] = pos_i + 1
                self.evalboard() ## determina h atual

                if self.fitness == 0 or iteracoes >= 25: break
            
        return self
