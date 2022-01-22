
from typing import Text
from PIL import Image, ImageDraw, ImageFont
import textwrap


def gerarImagem(vagas):
    for item in vagas:
        print(item)
        with Image.open('modeloEspecifico.jpg') as img:
            d = ImageDraw.Draw(img)
            TituloVaga(item, img, d)
            DescriaoVaga(item, img, d)
            img.save('pil_text_font.png')

    return 'salvo imagem'


def TituloVaga(vaga, img, draw):
    font = ImageFont.truetype('fonts/verdana-font-family/verdana.ttf', 36)
    texto = textwrap.wrap(str(vaga.cargo), width=20)
    texto = formataTexto(texto)
    tituloTamanho = int(img.size[1]/2.65)
    tituloLargura = int(img.size[0]/10)
    draw.text((tituloLargura, tituloTamanho), texto, spacing=10, font=font, fill="white", align="left")


def DescriaoVaga(vaga, img, draw):
    font = ImageFont.truetype('fonts/Avenir-LT-Std-45.ttf', 18)
    texto = textwrap.wrap(vaga.descricao, width=25)
    texto = formataTexto(texto)
    tituloTamanho = int(img.size[1]/1.5)
    tituloLargura = int(img.size[0]/9)
    draw.text((tituloLargura, tituloTamanho), texto , spacing=5, font=font, fill="black", align="left")


def formataTexto(texto):
    if len(texto) > 1:
        return texto[0]+'\n'+texto[1]
    else:
        return texto[0]
