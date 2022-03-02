from django.contrib import messages
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from RETHI.settings import MEDIA_ROOT
import textwrap
import os

def gerarImagem(request, vagas):
    for item in vagas:
        with Image.open(os.path.join(MEDIA_ROOT, 'Modelo/modeloEspecifico.jpg'), "r") as img:
            d = ImageDraw.Draw(img)
            TituloVaga(item, img, d)
            DescriaoVaga(item, img, d)
            img.save(f'{MEDIA_ROOT}/download/{str(item.id)}.jpg')
            return downloadImageVaga(request, item)

def TituloVaga(vaga, img, draw):
    font = ImageFont.truetype('fonts/verdana-font-family/verdana.ttf', 36)
    texto = textwrap.wrap(str(vaga.cargo), width=20)
    texto = formataTexto(texto)
    tituloTamanho = int(img.size[1]/2.65)
    tituloLargura = int(img.size[0]/10)
    draw.rectangle(((tituloLargura-40, tituloTamanho-5),(470, 580)), fill="#013E7F")
    draw.text((tituloLargura, tituloTamanho), texto, spacing=10,font=font, fill="#FBFBFB", align="left")

def DescriaoVaga(vaga, img, draw):
    font = ImageFont.truetype('fonts/Avenir-LT-Std-45.ttf', 18)
    texto = textwrap.wrap(vaga.descricao, width=25)
    texto = formataTexto(texto)
    tituloTamanho = int(img.size[1]/1.5)
    tituloLargura = int(img.size[0]/9)
    draw.text((tituloLargura, tituloTamanho), texto, spacing=5, font=font, fill="black", align="left")

def formataTexto(texto):
    if len(texto) > 1:
        return texto[0]+'\n'+texto[1]
    else:
        return texto[0]

def downloadImageVaga(request, item):
    image_buffer = open(os.path.join(MEDIA_ROOT, f'download/{str(item.id)}.jpg'), "rb").read()
    response = HttpResponse(image_buffer, content_type='image/jpeg');
    response['Content-Disposition'] = 'attachment; filename="%s.jpg"' % str(item)
    messages.info(request, f'Download da image divugação do cargo {item}')
    return response