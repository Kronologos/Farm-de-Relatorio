import itertools
class ltx_table():
    def __init__(self,*args,fillvalue=0):
        self.columns = list(args)
        num_cols = len(self.columns)
        lines = []
        for tuples in itertools.zip_longest(*self.columns, fillvalue=fillvalue):
            lst = list(tuples)
            str_lst = " & ".join(str(x) for x in lst)
            lines.append(str_lst)
        self.table_body = " \\\\ \\hline \n".join(lines)
        self.table_head = "\\begin{table}[h] \n \\begin{center} \n" 
        self.table_sub_head = "\n \\begin{tabular}{"+"|".join('c' for x in self.columns)+"} \n \\hline"
        self.table_tail = "\\\\ \\hline \n \\end{tabular} \n"
        self.table_sub_tail = "\\end{center} \n \\end{table}"
    
    def capt(self,caption,pos_top=True):
        if (pos_top):
            self.table_head+="\\caption{"+caption+'}\n \\vspace{0.1cm}\n'
        else:
            self.table_sub_tail = "\\caption{"+caption+'}\n'+self.table_sub_tail

    def table(self):
        table = self.table_head+'\n'+self.table_sub_head+'\n'+self.table_body+'\n'+self.table_tail+self.table_sub_tail
        print(table)



A = ["A", 1, 2, 3, 4, 5]