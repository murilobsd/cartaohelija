# coding=utf-8

import sys
import openpyxl as px


class Planilha(object):
    """
    Classe para ler conteudo da planilha
    """

    def __init__(self, entrada, aba='Plan1', lin_inicio=1, colunas=[1, 2],
                 lin_fim=None):
        self.entrada = entrada
        self.aba = aba
        self.lin_inicio = lin_inicio
        self.colunas = colunas
        self.lin_fim = lin_fim

        if len(colunas) != 2:
            print "Necessita de uma coluna do funcionario e do cargo."
            sys.exit(1)

    def _read(self, iterar=True):
        """ lendo planinha """
        try:
            W = px.load_workbook(self.entrada, use_iterators=iterar)
            p = W.get_sheet_by_name(name=self.aba)
            return p
        except:
            print u"Não foi possível ler a planilha: %s " % self.entrada
            sys.exit(1)

    def get_data(self):
        """ recuperando valores """
        print "*** Recuperando valores da planilha ***"
        data = []
        p = self._read()
        funcionario, cargo = [], []

        # TODO: Que zoado!, Preguica de ler a documentacao
        count = 0
        for num, row in enumerate(p.iter_rows()):
            if num >= self.lin_inicio:
                funcionario.append(row[self.colunas[0]])
                cargo.append(row[self.colunas[1]])
            else:
                count += 1

        for x, y in zip(funcionario, cargo):
            if x.value and y.value:
                data.append((x.value, y.value))

        return data
