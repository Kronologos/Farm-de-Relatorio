import sympy as sp 

class Farm():
    def __init__(self,Formula,*args):
        """
        Recebe uma string da fórmula, um dict das variaveis fixas e os argumentos
        """
        self.formula = Formula
        self.Dados = self.get_dados(args)
        self.tornar_simbolica()

    def get_dados(self, lista_de_dados):
        '''
        Essa função transforma os dados inseridos em um dicionário onde o index é a variável e o item são os valores.
        ''' 
        dic_dados = dict()
        for dado in lista_de_dados:
            dic_dados[dado[0]] = dado[1:]
        return dic_dados

    def tornar_simbolica(self):
        self.formula = sp.sympify(self.formula)
        
    def formula_ltx(self):
        return sp.latex(self.formula)
    
    def faz_simb(self, index):
        temp = self.formula.subs({chave:sp.Symbol(str(self.Dados[chave][index])) for chave in self.Dados.keys()})
        temp_num =self.formula.subs({chave:(self.Dados[chave][index]) for chave in self.Dados.keys()})
        temp = sp.latex(self.formula) + " =" +sp.latex(temp)+" = {0}".format(temp_num)
        return temp

    def substitui_ai_pra_nos(self, linhas = 1):
        n = linhas-1#auxiliar
        for i in range(linhas): 
            ltx = self.faz_simb(i)
            print(ltx)

#Testezin ra´pido
s = 's_0 + v_0*t +a*(t/2)^2'

s_in = ['s_0', 1,2,3,4]
v_in = ['v_0', 1.2, 2, 7, 4.5]
a = ['a', 23.4, 31, 15, 69]
t= ['t', 3.6, 4.5,9]

A = Farm(s,s_in,v_in,a,t)
A.substitui_ai_pra_nos(linhas=2)



    

        





