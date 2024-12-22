import numpy as np
import Searchs as sh
import MemoryController as m

#Inciarlizar Class de Memoria
Memory = m.MemoryController()

class EnvSimulation:
    #Construtor
    def __init__(self) -> None:
        np.random.seed(1234)
        pass

    #Gerar Tabuleiro Aleatorio
    def random_board(self,n): return(np.random.randint(0,n, size = n))

    #Calculo
    def comb2(self,n): return n*(n-1)//2 

    #Somar Conflitos
    def conflicts(self,board):
        n = len(board)
        
        horizontal_cnt = [0] * n
        diagonal1_cnt = [0] * 2 * n
        diagonal2_cnt = [0] * 2 * n
        
        for i in range(n):
            horizontal_cnt[board[i]] += 1
            diagonal1_cnt[i + board[i]] += 1
            diagonal2_cnt[i - board[i] + n] += 1
        
        return sum(map(self.comb2, horizontal_cnt + diagonal1_cnt + diagonal2_cnt))

#Class Controlladora da Execução
class ExecuteSimulation:
    #Construtor
    def __init__(self) -> None:
        pass

    #Void Inciar Simulação
    def StartSimule(self , amountSimulations, nBoard,memory):
        newEnvSimule = EnvSimulation()
        searchsFile = sh.Searchs(newEnvSimule)
        searchsFile.Steepest_ascend_hill_climbing(n=nBoard,memory= memory,amountSimulations=amountSimulations)
        searchsFile.Random_steepest_ascend_hill_climbing(n=nBoard,memory= memory,amountSimulations=amountSimulations)
        searchsFile.First_Choice_steepest_ascend_hill_climbing(n=nBoard,memory= memory,amountSimulations=amountSimulations)

#Inicializar Simulação de Busca
def StartSimulation(amountSimulations, nBoard):
    Memory.listWithAllSearchs.clear()
    searchController = ExecuteSimulation()
    searchController.StartSimule(amountSimulations,nBoard,Memory)
