import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Plotar Graficos e Tabelas
class PlotTableAndGrafic:
    def __init__(self) -> None:
        pass

    #Plotar Tabela 
    def setPlotTable(self,nameTable,collums, rows):
        genericDateFrame = pd.DataFrame(collums,index=rows)
        fig, tableS = plt.subplots()
        fig.patch.set_visible(False)
        tableS.axis('off')
        tableS.axis('tight')
        tableOpened = tableS.table(cellText=genericDateFrame.values,colLabels=genericDateFrame.columns,rowLabels=rows,loc='center')
        tableOpened.auto_set_font_size(False)
        tableOpened.set_fontsize(14)
        fig.set_size_inches(12, 8)
        plt.title(nameTable)
        plt.show()

    #Criar Grafico
    def setCreateGrafic(self,nameTable,values,names,maxValue,ylabel = "Desempenho"):
        # names = ("2 Ruas Por Via", "3 Ruas Por Via", "2 Ruas Por Via / Semáforo","3 Ruas Por Via/Semáforo")
        # values = {
        #     'Média de Tempo na Rotatória (Segundos)': (float(timeInRound[0]), float(timeInRound[1]),float(timeInRound[2]),float(timeInRound[3])),
        #     'Média de Tempo por Veículo (Minutos)': (float(timePerCar[0]), float(timePerCar[1]),float(timePerCar[2]),float(timePerCar[3])),
        #     'Tempo Total (Minutos)': (float(totalTime[0]), float(totalTime[1]),float(totalTime[2]),float(totalTime[3])),
        # }

        x = np.arange(len(names))  
        width = 0.25  
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')
        fig.set_size_inches(10.5, 5.5)

        for attribute, measurement in values.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
 
        ax.set_ylabel('Desempenho')
        ax.set_title(nameTable)
        ax.set_xticks(x + width, names)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, float(maxValue) + float(maxValue)/5)

        plt.show()