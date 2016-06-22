# coding=utf-8

import sys
import slugify
import os
from PIL import Image, ImageFont, ImageDraw


class FabricaCartao(object):
    """
    Classe Gera Cartoes
    """

    app_folder = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, saida, w_saida=434, h_saida=160,
                 nome_tam=18, cargo_tam=13, font="Gidole-Regular.otf",
                 cargo_cor=(147, 149, 151, 255), logo="logo.jpg",
                 footer="footer.jpg",
                 cor_bg=(255, 255, 255, 255)):
        self.w_saida = w_saida  # largura da imagem que sera gerada
        self.h_saida = h_saida  # altura da imagem que ser gerada
        self.saida = saida  # pasta onde sera salvo o arquivo gerado
        self.nome_tam = nome_tam  # Tamanho em pt para nome do funcionario
        self.cargo_tam = cargo_tam  # Tamanho em pt para o cargo_tam
        self.font = font  # tipo de fonte utilizada para cartao
        self.cargo_cor = cargo_cor
        self.logo = logo
        self.footer = footer
        self.cor_bg = cor_bg  # cor de fundo do cartao
        self.tipo_img = 'RGBA'

        self.check_files()

    def check_files(self):
        print "** Checando Arquivos ***"
        """ simples checagem dos arquivos principais """
        if not os.path.exists(self.saida):
            print u"Não existe o arquivo de saida %s" % self.saida
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, self.font)):
            print u"Não existe o arquivo de fonte. %s" % self.font
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, self.footer)):
            print u"Não existe o arquivo do footer: %s" % self.footer
            sys.exit(1)
        elif not os.path.exists(os.path.join(self.app_folder, self.logo)):
            print u"Não existe o arquivo da logo: %s" % self.footer
            sys.exit(1)
        else:
            print u"Checagem concluida.\n\n"
            return True

    def _get_fonts(self):
        """ return fonts """
        font_fun = ImageFont.truetype(os.path.join(self.app_folder, self.font),
                                      self.nome_tam)
        font_car = ImageFont.truetype(os.path.join(self.app_folder, self.font),
                                      self.cargo_tam)
        return font_fun, font_car

    def _get_logo(self):
        """ retorna logo img """
        im = Image.open(os.path.join(self.app_folder, self.logo))
        im = im.resize((121, 158), Image.ANTIALIAS)
        return im

    def _get_footer(self):
        """ retorn footer e a font """
        im = Image.open(os.path.join(self.app_folder, self.footer))
        im = im.resize((309, 76), Image.ANTIALIAS)
        return im

    def nome_saida(self, filename):
        """ gera o nome da saida com o nome do funcionario """
        new_filename = slugify.slugify(filename)+'.jpg'
        return os.path.join(self.saida, new_filename)

    def gerar(self, funcionario, cargo):
        """ gerar o arquivo """
        print "Gerando Assinatura..."
        canvas = Image.new(self.tipo_img, (self.w_saida, self.h_saida),
                           self.cor_bg)
        draw = ImageDraw.Draw(canvas)

        # Imagens
        logo, footer = self._get_logo(), self._get_footer()
        canvas.paste(logo, (0, 0))
        canvas.paste(footer, (123, 81))

        # Textos
        fn_func, fn_cargo = self._get_fonts()
        draw.text((129, 41), funcionario, font=fn_func, fill=(0, 0, 0, 255))
        draw.text((129, 59), cargo, font=fn_cargo, fill=self.cargo_cor)

        filename = self.nome_saida(funcionario)
        canvas.save(filename)
        print u"Assinatura de: %s gerada com sucesso." % filename
        return True
