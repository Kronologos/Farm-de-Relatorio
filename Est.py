import numpy as np
from math import log10,floor
#Classe para uso Exclusivo de Nício Murilo da Silva no curso de Química Analítica Experimental
class Estat():
    #Inicia o objeto com os atributos estatísticos, calculando-os e ajustando-os.
    def __init__(self,values,variable,unids,ref_val=0,conf=95):
        self.values = values
        self.ref_val = ref_val
        self.unidades = unids
        self.variavel = variable
        #Cálculos
        self.media = np.average(self.values)
        self.s = np.std(self.values,ddof=1)
        self.cv = 100*self.s/self.media
        if(ref_val != 0):
            self.err_rel = round(100*abs((self.media-self.ref_val)/self.ref_val),2)
        else:
            self.err_rel = False
        self.ic_termo = self.inc_conf(conf)
        #Método para consertar as casas decimais
        if (self.ic_termo<1):
            self.casas()
        else:
            self.casas(menor=True)
        
        
    #Avalia o valor de t conforme dados da vídeoaula 1
    def t(self,n,conf=95):
        if(conf == 95):
            di = {1:12.71, 2:4.30 , 3:3.18, 4:2.78, 5: 2.57}
            return di[n-1]
        if(conf == 99):
            di = {1:63.66, 2:9.92, 3:5.84, 4:4.60, 5: 4.03}
            return di[n-1]
        else:
            raise Exception('Confiança de {0} não reconhecida'.format(conf))

    #Computa a variação no Intervalo de confiança
    def inc_conf(self,conf):
        return self.s*self.t(len(self.values),conf)/np.sqrt(len(self.values))
    
    #Conserta as casas decimais de todas as variáveis com base na variação do IC
    def casas(self,menor=False):
        #Esse método calcula em qual casa decimal está o significativo, se ele é maior q 1
        num_signif = -int(floor(log10(abs(self.ic_termo))))
        f = lambda x:round(x,num_signif)
        self.media = f(self.media)
        self.s = f(self.s)
        self.cv = f(self.cv)
        self.ic_termo = f(self.ic_termo)
    
    #Método para tabela
    def table(self):
        print(r"\begin{table}[h] \label{tabEstat}"+'\n')
        print(r"\begin{center}"+'\n')
        print(r"\caption{Dados estatísticos experimentais.}"+'\n')
        print(r"\begin{tabular}{c|c}"+'\n')
        print(r"\hline Variável & Valor \\ \hline "+'\n')
        print(r"$"+self.variavel+r"_{media}$ & "+"{0} {1}".format(self.media,self.unidades)+r'\\ \hline'+'\n')
        print(r"s & "+"{0} {1}".format(self.s,self.unidades)+r" \\ \hline"+'\n')
        print(r"CV & "+"{0}".format(self.cv)+r" \\ \hline"+'\n')
        if (self.err_rel!=0):
            print(r"E(\%) & "+"{0}".format(self.err_rel)+r" \\ \hline"+'\n')
        print(r"IC & "+"({0} $\pm$ {1}) {2}".format(self.media,self.ic_termo,self.unidades)+'\n'+r" \\ \hline")
        print("\\end{tabular} \n \\end{center} \n \\end{table}")

