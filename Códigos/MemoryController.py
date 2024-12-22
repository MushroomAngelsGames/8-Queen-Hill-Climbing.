import PlotTableAndGrafic as pt

#Class Controladora de Memoria
class MemoryController:
    #Construtor
    def __init__(self) -> None:
        self.listWithAllSearchs = []
        self.Plot = pt.PlotTableAndGrafic()
        pass

    #Adcionar Nova Simulação de Um Arquivo
    def addNewSearchAlgorithm(self,newSearch):
        self.listWithAllSearchs.append(newSearch)

    #Recupera Nome das Memorias das Simulações Salvas
    def getListName(self):
        nameTemp = []
        for ss in self.listWithAllSearchs:
            nameTemp.append(ss.searchName)
        return nameTemp
    
    #Recuperar um Memoria de um Arquivo Pelo Nome
    def getWithName(self,name):
        for ss in self.listWithAllSearchs:
            if(ss.searchName == name):
                return ss

    #Plotar Grafico das Médias Gerais
    def setPlotGraficGlobal(self):

        self.listWithAllSearchs[0].getValueStr()
        self.listWithAllSearchs[1].getValueStr()
        self.listWithAllSearchs[2].getValueStr()

        names = ("Hill Climbing", "Random Hill Climbing", "First Hill Climbing")
        values = {
            'Custo': (self.listWithAllSearchs[0].AvarageCost, float(self.listWithAllSearchs[1].AvarageCost),float(self.listWithAllSearchs[2].AvarageCost)),
            'Tentativas': (self.listWithAllSearchs[0].AvarageAttempt, float(self.listWithAllSearchs[1].AvarageAttempt),float(self.listWithAllSearchs[2].AvarageAttempt)),
            'Chegou no (Máximos Global) em %': (self.listWithAllSearchs[0].AvarageCanSolve, float(self.listWithAllSearchs[1].AvarageCanSolve),float(self.listWithAllSearchs[2].AvarageCanSolve))
        }

        self.Plot.setCreateGrafic("Comparação de Algorítimos de Busca Local",values,names,self.listWithAllSearchs[0].AvarageCost)

    #Plotar Tabela das Médias Gerais
    def setPlotTableGlobal(self):
        valueFinal= {}
        valueFinal["Quantificadores de Desempenho dos Algarismos de Busca"] = [self.listWithAllSearchs[0].getValueStr(),
                                                                               self.listWithAllSearchs[1].getValueStr(),
                                                                               self.listWithAllSearchs[2].getValueStr()]
        
        self.Plot.setPlotTable("Comparação de Algorítimos de Busca Local",valueFinal,["HC","RHC","FHC"])

#Mémoria Search
class MemorySearch:

    #Construtor
    def __init__(self,searchName) -> None:
        self.searchName = searchName
        self.listWithAllSearchInThisAlgorithm = []
        self.AvarageCost = 0
        self.AvarageAttempt = 0
        self.AvarageCanSolve = 0        
        pass

    #Calcular Médias
    def getValueStr(self):
        self.AvarageCost = 0
        self.AvarageAttempt = 0
        self.AvarageCanSolve = 0

        for ss in self.listWithAllSearchInThisAlgorithm:
            self.AvarageCost +=ss.cost
            self.AvarageAttempt +=ss.attempt
            self.AvarageCanSolve +=ss.canSolve

        
        amount = len(self.listWithAllSearchInThisAlgorithm)
        self.AvarageCost = round(self.AvarageCost/amount,2)
        self.AvarageAttempt = round(self.AvarageAttempt/amount,2)
        self.AvarageCanSolve = round((self.AvarageCanSolve*100)/amount,2)
        print("*Média Final*")
        print(f"Média de Tentativas: {self.AvarageAttempt} | Custo Médio: {self.AvarageCost}")
        print(f"Porcentagem de Sucessos (Máximo Global): {self.AvarageCanSolve}%")
        return (f"Média de Tentativas: {self.AvarageAttempt} | Custo Médio: {self.AvarageCost} | (Máximo Global): {self.AvarageCanSolve}%")
        
    #Gerar Nomes para a Lista de Searchs
    def getListSearchNames(self):
        nameTemp = []
        count = 1
        for ss in self.listWithAllSearchInThisAlgorithm:
            nameTemp.append(f"{count}º | Busca | Tentativas: {ss.attempt} | Custo: {ss.cost} | Sucesso: { True if (ss.canSolve == 1) else False}")
            count+=1
        return nameTemp

    #Recuperar um Memoria de um Arquivo Pelo Nome
    def getWithName(self,name):     
        return self.listWithAllSearchInThisAlgorithm[int(name[0])-1]

    #Adcionar Nova Busca
    def SetAddNewSearch(self, newSearch):
        self.listWithAllSearchInThisAlgorithm.append(newSearch)

#Memoria Individual para Memory
class OnlyMemory:
    #Construtor
    def __init__(self,finalBoard,stepsBoard,cost,attempt,canSolve,UIPlotQueen) -> None:
        self.finalBoard = finalBoard
        self.stepsBoard = stepsBoard
        self.cost = cost
        self.attempt = attempt
        self.canSolve = canSolve
        self.UIPlotQueen = UIPlotQueen
        pass

    #Mostrar Animação Final
    def PlotFinalBoard(self):
        self.UIPlotQueen.show_boardFinal(self.finalBoard)

    #Mostrar Animação Passo-A-Passo
    def PlotFinalStepsBoard(self):
        self.UIPlotQueen.show_board(self.stepsBoard)