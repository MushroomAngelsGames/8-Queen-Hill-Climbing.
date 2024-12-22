import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#Class para Plotar as Animações de Busca
class UIPlotQueen:
    #Construtor
    def __init__(self,EnvSimulation) -> None:
        self.EnvSimulation =EnvSimulation
        pass

    #Mostrar Animação da Busca Local Generico
    def show_board(self,board,cols = ['white', 'gray'], fontsize = 48):  
        cmap = colors.ListedColormap(cols)
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 8)
        count = 0

       
        for ss,dataPos in board:
            columnMatriz,rowMatriz,attempt = dataPos
            n = len(ss)
            display = np.zeros([n,n])   
            for i in range(n):
                for j in range(n):
                    if (((i+j) % 2) != 0): 
                        display[i,j] = 1
            
            ax.clear()
            ax.imshow(display, cmap = cmap, norm = colors.BoundaryNorm(range(len(cols)+1), cmap.N))

            ax.set_xticks([])
            ax.set_yticks([])
         
            for j in range(n):
                plt.text(j, ss[j], u"\u265B", fontsize = fontsize/(n/8), 
                        horizontalalignment = 'center',
                        verticalalignment = 'center')
                    
            
            count+=1
            ax.set_title(f"Tentativa {attempt} | Busca Matricial {columnMatriz}x{rowMatriz} | Custo: {count} | Tabuleiro com {self.EnvSimulation.conflicts(ss)} Conflitos Entre Rainhas.")
        
            plt.pause(0.1)
        
    #Mostrar Resultado Final
    def show_boardFinal(self,board,cols = ['white', 'gray'], fontsize = 48):  
        cmap = colors.ListedColormap(cols)
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 8)
        n = len(board)

        display = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                if (((i+j) % 2) != 0): 
                    display[i,j] = 1
            
        ax.imshow(display, cmap = cmap,  norm = colors.BoundaryNorm(range(len(cols)+1), cmap.N))

        ax.set_xticks([])
        ax.set_yticks([])
         
        for j in range(n):
                plt.text(j,board[j], u"\u265B", fontsize = fontsize/(n/8), 
                        horizontalalignment = 'center',
                        verticalalignment = 'center')
                    
        ax.set_title(f"Tabuleiro com {self.EnvSimulation.conflicts(board)} Conflitos Entre Rainhas.")
        plt.show()             
           