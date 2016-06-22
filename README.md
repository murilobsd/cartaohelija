# crawlercps lab804

![](exemplo_saida.png)
![](murilo.jpg)

## Introdução

Criador de cartões para os funcionários **Helija Org. Contábil**

O gerador foi desenvolvido na versão **2.7.11** do python.

## Instalando python

### Linux
```bash
$ sudo apt-get update
$ sudo apt-get install python-dev python-setuptools
```

### Windows
- [https://www.python.org/ftp/python/2.7.11/python-2.7.11.amd64.msi](Download)
- [http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7](Adicionando ao Path)
- Abra o cmd e digite **python**


## Instalando as dependências


### Linux
```bash
# diretorio do projeto
$ pip install -r req.txt
```

### Windows
```bash
pip install -r req.txt
```

## Exemplos

### Linux
```bash
$ python main.py -i funcionario.xlsx -o data/
```

### Windows
```bash
python main.py -i funcionario.xlsx -o data/
```

## Dúvidas
```bash
python main.py -h

usage: main.py [-h] -i ENTRADA -o SAIDA

Gerar cartões dos funcionários Helija Org. Contábil.

optional arguments:
  -h, --help            show this help message and exit
  -i ENTRADA, --entrada ENTRADA
                        Arquivo no formato xlsx.
  -o SAIDA, --saida SAIDA
                        Pasta na qual será salva as assinaturas.
```
