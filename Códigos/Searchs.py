import numpy as np
import random as rd
import UIPlotQueen as pt
import MemoryController as m

#Class de Gerencia as Busca Locais
class Searchs:
    #Construtor da Class
    def __init__(self,EnvSimulation) -> None:
        self.EnvSimulation = EnvSimulation
        self.UIplot =pt.UIPlotQueen(EnvSimulation)
        pass

    #Algoritimo de Busca First Choice Hill Climbing
    def First_Choice_steepest_ascend_hill_climbing(self,n,memory,amountSimulations):
        newMemorySearch = m.MemorySearch("First Choice Steepest Ascent Hill Climbing")
        for i in range(amountSimulations):
            current_board = self.EnvSimulation.random_board(n)
            stepsAfterFinish = [current_board]
            attempt = 0
            stepsAfterAll = [[current_board,(0,0,attempt)]]
            while True: 
                attempt+=1
                current_obj = self.EnvSimulation.conflicts(current_board)
                best_move = None
                best_obj = current_obj
                for col in range(n):
                    for row in range(n):
                        new_board = np.copy(current_board)
                        new_board[col] = row
                        new_obj = self.EnvSimulation.conflicts(new_board)
                        all = np.copy(current_board)
                        all[col]= row 
                        stepsAfterAll.append([all,(col+1,row+1,attempt)])
                        if new_obj < best_obj:
                            best_obj = new_obj
                            best_move = (col, row)
                            break 
                        
             
                if best_move != None:
                    col, row = best_move
                    current_board[col] = row
                else:     
                    stepsAfterAll.append([current_board,(col+1,row+1,attempt)])        
                    newMemorySearch.SetAddNewSearch(m.OnlyMemory(current_board,stepsAfterAll,len(stepsAfterAll),attempt,1 if (self.EnvSimulation.conflicts(current_board)== 0) else 0,UIPlotQueen=  self.UIplot))
                    break

                stepsAfterFinish.append(np.copy(current_board))  
        memory.addNewSearchAlgorithm(newMemorySearch)

    #Algoritimo de Busca Hill Climbing
    def Steepest_ascend_hill_climbing(self,n,memory,amountSimulations):
        newMemorySearch = m.MemorySearch("Steepest Ascent Hill Climbing")
        for i in range(amountSimulations):
            current_board = self.EnvSimulation.random_board(n)
            stepsAfterFinish = [current_board]
            attempt = 0
            stepsAfterAll = [[current_board,(0,0,attempt)]]
            while True: 
                attempt+=1
                current_obj = self.EnvSimulation.conflicts(current_board)
                best_move = None
                best_obj = current_obj
                for col in range(n):
                    for row in range(n):
                        new_board = np.copy(current_board)
                        new_board[col] = row
                        new_obj = self.EnvSimulation.conflicts(new_board)
                   
                        all = np.copy(current_board)
                        all[col]= row 
                        stepsAfterAll.append([all,(col+1,row+1,attempt)])
                        if new_obj < best_obj:
                            best_obj = new_obj
                            best_move = (col, row)
                        

                if best_move != None:
                    col, row = best_move
                    current_board[col] = row
                else:
                    stepsAfterAll.append([current_board,(col+1,row+1,attempt)])
                    newMemorySearch.SetAddNewSearch(m.OnlyMemory(current_board,stepsAfterAll,len(stepsAfterAll),attempt,1 if (self.EnvSimulation.conflicts(current_board)== 0) else 0,UIPlotQueen=  self.UIplot))
                    break
      

                stepsAfterFinish.append(np.copy(current_board))   
        memory.addNewSearchAlgorithm(newMemorySearch)

    #Algoritimo de Busca Random Hill Climbing
    def Random_steepest_ascend_hill_climbing(self,n,memory,amountSimulations):
        newMemorySearch = m.MemorySearch("Random Steepest Ascent Hill Climbing")
        for i in range(amountSimulations):
            current_board = self.EnvSimulation.random_board(n)
            stepsAfterFinish = [current_board]
            attempt = 0
          
            stepsAfterAll = [[current_board,(0,0,attempt)]]
            while True: 
                attempt+=1
                current_obj = self.EnvSimulation.conflicts(current_board)
                best_move = None
                best_obj = current_obj
                for col in range(n):
                    row = rd.randint(0,n-1)
                    new_board = np.copy(current_board)
                    new_board[col] = row
                    new_obj = self.EnvSimulation.conflicts(new_board)
                  
                    all = np.copy(current_board)
                    all[col]= row 
                    stepsAfterAll.append([all,(col+1,row+1,attempt)])

                    if new_obj < best_obj:
                        best_obj = new_obj
                        best_move = (col, row)
                            
                
                if best_move != None:
                    col, row = best_move
                    current_board[col] = row
                else:
                    stepsAfterAll.append([current_board,(col+1,row+1,attempt)])
                    newMemorySearch.SetAddNewSearch(m.OnlyMemory(current_board,stepsAfterAll,len(stepsAfterAll),attempt,1 if (self.EnvSimulation.conflicts(current_board) == 0) else 0,UIPlotQueen=  self.UIplot))
                    break
     

                stepsAfterFinish.append(np.copy(current_board))                
        memory.addNewSearchAlgorithm(newMemorySearch)
                