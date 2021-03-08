import sympy as sp 

class Farm():
    def __init__(self,Formula: str,var: str,*args,linhas=1):
        """
        Recebe uma string da fórmula, uma string com a variável final e um número
        variável de listas no qual o primeiro elemento é a variável a ser substituída
        e o restante é o valor a substituir. Um parâmetro opcional é o número de linhas a serem computadas.
        Ex: A = Farm('(4/3)*pi*(r^3)', 'V', [ ['r', 1,2,3,4] ])
        """
        self.formula = Formula
        self.var = var
        self.Dados = self.get_dados(args)
        self.tornar_simbolica()
        self.faz(linhas)

    def get_dados(self, lista_de_dados: list):
        '''
        Essa função transforma os dados inseridos em um dicionário onde o index é a variável e o item são os valores.
        ''' 
        dic_dados = dict()
        for dado in lista_de_dados:
            dic_dados[dado[0]] = dado[1:]
        return dic_dados

    def tornar_simbolica(self):
        '''
        Essa função transforma a fórmula inserida em uma fórmula Sympy.
        '''
        self.formula = sp.sympify(self.formula)
        
    def formula_ltx(self):
        '''
        Essa função retorna a fómula inserida em linguagem LaTeX.
        '''
        return sp.latex(self.formula)
    
    def faz_simb(self, index):
        '''
        Essa função substitui simbolicamente os valores inseridos na fórmula de acordo
        com seus índices na list de dados, depois iguala ao resultado da substituição.
        '''
        temp = self.formula.subs({chave:sp.Symbol(str(self.Dados[chave][index])) for chave in self.Dados.keys()})
        temp_num =self.formula.subs({chave:(self.Dados[chave][index]) for chave in self.Dados.keys()})
        temp =sp.latex(temp)+"= {0}".format(temp_num)+r'\\'+'\n'
        return temp

    def substitui_ai_pra_nos(self, linhas = 1):
        '''
        Essa função faz a substituição para um número declarado de linhas.
        ex: substitui_ai_pra_nos(linhas = 4)
        '''
        my_str = ''
        n = linhas-1#auxiliar
        my_str+= self.var +" &= "+ self.formula_ltx()+'\n'
        for i in range(linhas): 
            ltx = self.faz_simb(i)
            my_str+= self.var+'&='+ltx
        return my_str
    
    def faz(self,linhas=1):
        print(r'\begin{align}'+'\n')
        print(self.substitui_ai_pra_nos(linhas=linhas))
        print(r'\end{align}')
        





    

        





