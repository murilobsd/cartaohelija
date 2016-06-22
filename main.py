#!/usr/bin/env python
# coding=utf-8

import argparse
import sys

from cartao import generate, planilha


def get_args():
    parser = argparse.ArgumentParser(
        description=u'Gerar cartões dos funcionários Helija Org. Contábil.')
    parser.add_argument(
        '-i', '--entrada', type=str, help='Arquivo no formato xlsx.',
        required=True)
    parser.add_argument(
        '-o', '--saida', type=str,
        help=u'Pasta na qual será salva as assinaturas.',
        required=True)

    args = parser.parse_args()
    entrada = args.entrada
    saida = args.saida

    return entrada, saida


def main(entrada, saida):
    cartao = generate.FabricaCartao(saida)
    # Aba = Plan1
    # lin_inicio == Onde iniciar a linha 0 igual a primeira 1 segunda ...
    p = planilha.Planilha(entrada, aba='Plan1', lin_inicio=1, colunas=[1, 2])
    dados = p.get_data()
    for funcionario, cargo in dados:
        print "%s --> %s" % (funcionario, cargo)
        cartao.gerar(funcionario, cargo)

if __name__ == '__main__':
    try:
        entrada, saida = get_args()
    except:
        sys.exit(1)
    main(entrada, saida)
