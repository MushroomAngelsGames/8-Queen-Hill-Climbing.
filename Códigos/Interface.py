from PySimpleGUI import PySimpleGUI as sg
import Queen as qn

NAME_DEFAULT_WINDOWS = "Otimização das 8 Rainhas"
NAME_RESULTS_WINDOWS = "Otimização das 8 Rainhas - Resultados"
NAME_RESULTS_STEPS_BY_STEPS_WINDOWS = "Otimização das 8 Rainhas - Resultados (Passo-A-Passo)"

#Class Controladora Geral da Interface
class UISimulationController:

    #Inicialização da Classe e das Variaveis.
    def __init__(self) -> None:
        sg.theme('Reddit')
        pass
    
    #Criar os Menus da tela Inicial.
    def CreateBasicInterface(self):
       
        #Menu de para Adcionar Simulação.
        addFrameLoyout = [
            [sg.Text("Quantidade de Simulações"),sg.Input(key='KEY_AMOUNT_SIMULATIONS',default_text="100",tooltip="Quantidade de Simulações que o Software vai realizar para calcular o desempenho dos algorítimos de busca.",size=(5,1)),       
            sg.Text("Tamanho do Tabuleiro"),sg.Input(key='KEY_AMOUNT_BOARD',default_text="8",size=(5,1))],
            [sg.Button("INICIALIZAR BUSCAS", key="BUT_START_SIMULE",size=(50,1))]
        ]

        #Menu de Lista com todas as Simulações cadastradas.
        addFrameList= [
           [sg.Text("Objetivo: Encontrar um arranjo de N rainhas em um N×N tabuleiro de xadrez de modo que nenhuma rainha esteja na mesma linha, coluna ou diagonal que qualquer outra rainha.",size=(63,10),font='Any 10',background_color= '#DAE0E6')]
        ]

        #Layout Principal que será inicializado.
        layout = [
            [sg.Frame("Simular",addFrameLoyout,font='Any 14')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Descrição do Problema',addFrameList,font='Any 14')],
            [sg.HorizontalSeparator(pad=None)],
        ]

        return layout

    #Inicializar Interface e App, Ficar Verificando interações do Usuário.
    def StartApp(self):
        GlobalWindons = sg.Window(NAME_DEFAULT_WINDOWS, self.CreateBasicInterface() ,size=(550,250))
        
        while True:
            events,values = GlobalWindons.read()              

            if(events == sg.WINDOW_CLOSED):
                break
            if events == "BUT_START_SIMULE":
                qn.StartSimulation(int(values["KEY_AMOUNT_SIMULATIONS"]),int(values["KEY_AMOUNT_BOARD"]))
                FinalUI = UIFinalResults()
                FinalUI.StartApp()
           
#Class Controladora Geral da Interface
class UIFinalResults:

    #Inicialização da Classe e das Variaveis.
    def __init__(self) -> None:  
        pass
    
    #Gerar Layout da Janela de Resultados
    def GetBasicInterface(self):
   
        dataSimulation= [
             [sg.Button("Visualizar Detalhes do Algorítimo Selecionado",size=(100,2),key="KEY_VIEW_ALGORITHM")]
        ]

        dataResusts= [
             [sg.Button("Gerar Tabela",size=(35,2),key="BUT_PLOT_TABLE"),
              sg.Button("Plotar Grafico",size=(35,2),key="BUT_PLOT_GRAFIC")
            ]
        ]

        addFrameList= [
            [sg.Frame('Mas Detalhes - Passo a Passo',dataSimulation,font='Any 12',border_width=2,visible=False,key="KeyFrameDataSimule")],
            [sg.Listbox(values = qn.Memory.getListName(),
                        size=(350,6),
                        key="KeyListWithSimulations",
                        background_color='#9FB8AD',
                        pad=(5,5),
                        font="italic",
                        enable_events=True)]     
        ]

        #Layout Principal que será inicializado.
        layout = [
            [sg.Frame('Resultados da Busca nas Rainhas',addFrameList,font='Any 12',key="KeyFrameList")],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Resultados',dataResusts,font='Any 10')],
            [sg.HorizontalSeparator(pad=None)],
        ]

        return layout

    #Inicializar Interface e App, Ficar Verificando interações do Usuário.
    def StartApp(self):
        GlobalWindons = sg.Window(NAME_RESULTS_WINDOWS, self.GetBasicInterface() ,size=(550,350))

        while True:
            events,values = GlobalWindons.read()              

            if (events == sg.WINDOW_CLOSED):
                break

            if (events == "BUT_PLOT_TABLE"):
                qn.Memory.setPlotTableGlobal()

            if (events == "BUT_PLOT_GRAFIC"):
                qn.Memory.setPlotGraficGlobal()

            if (events == "KEY_VIEW_ALGORITHM"):
                UIController = UIViewValues(qn.Memory.getWithName(values["KeyListWithSimulations"][0]))
                UIController.StartApp()

            if (events == "KeyListWithSimulations"):
                GlobalWindons["KeyFrameDataSimule"].update(visible = True)

#Class Janela de Detalhes dos Resultados
class UIViewValues():
    #Construtor
    def __init__(self,searchfile) -> None:
        self.Searchfile = searchfile
        pass

    #Gera Layout da Janela de Detalhes dos Resultados
    def GetBasicInterface(self):
     
        addFrameLoyout = [
            [sg.HorizontalSeparator(pad=None)],  
            [sg.Radio('Resultado Final', "RADIO2", default=True,key="isSteps1",background_color='#9FB8AD'),
                sg.Radio('Passo A Passo', "RADIO2",key="isSteps2",background_color='#9FB8AD'),
                sg.Button("Mostra Animação da Busca",key="keyShow",size=(100,1))],
            [sg.HorizontalSeparator(pad=None)],  
        ]

        addFramWithAvarageFinal= [
          [sg.Output(size=(500,5),key="KeyOutput")],
        ]
     
        layout = [
            [sg.Text(f"Algorítimo Selecionado : {self.Searchfile.searchName}",font='Any 12')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Medias Finais',addFramWithAvarageFinal,font='Any 10')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame("Visualizar Animação do Passo-A-Passo da Busca",addFrameLoyout,font='Any 10')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Listbox(values =  self.Searchfile.getListSearchNames(),
                        size=(350,15),
                        key="KeyListWithSimulations",
                        background_color='#9FB8AD',
                        pad=(5,5),
                        font="italic",
                        enable_events=True),]     
        ]

        return layout

    #Iniciar Janela e Controlador de Eventos
    def StartApp(self):
        globalWindons = sg.Window(NAME_RESULTS_STEPS_BY_STEPS_WINDOWS,self.GetBasicInterface(),size=(550,500)) 
        
        for i in range(1):
            events,values = globalWindons.read(timeout=10)  
            self.Searchfile.getValueStr()
        
        while True:         
            events,values = globalWindons.read() 
            if(events == sg.WINDOW_CLOSED):
                break

            if(events =="keyShow"):
                if len(values["KeyListWithSimulations"]) > 0:
                    if(values["isSteps1"] == True):
                        self.Searchfile.getWithName(values["KeyListWithSimulations"][0]).PlotFinalBoard()
                    else:
                        self.Searchfile.getWithName(values["KeyListWithSimulations"][0]).PlotFinalStepsBoard()

UIController = UISimulationController()
UIController.StartApp()