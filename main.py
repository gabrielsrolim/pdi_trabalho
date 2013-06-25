from PIL import Image
from pdi_trabalho import rgb2yuv
import os

def main():
    caminho = raw_input('Digite o nome da imagem: ')
    img = Image.open(os.getcwd()+'/'+caminho)
    #img.show()
    while(True):
        print('*************************MENU*******************');
        print('0 - Converter RGB-YUV');
        print('1 - Converter YUV-RGB');
        print('2 - Mostrar banda R');
        print('3 - Mostrar banda G');
        print('4 - Mostrar banda B');
        print('5 - Mostrar banda R (monocromatica)');
        print('6 - Mostrar banda G (monocromatica)');
        print('7 - Mostrar banda B (monocromatica)');
        print('8 - Negativo');
        print('9 - Brilho Aditivo');
        print('10 - Brilho Multiplicativo');
        print('11 - Media');
        print('12 - Mediana');
        print('13 - Negativo BandaY');
        print('14 - Brilho Aditivo BandaY');
        print('15 - Brilho Multiplicativo BandaY');
        print('16 - Media BandaY');
        print('17 - Mediana BandaY');
        print('18 - Questao 2 (salt & pepper)');
        print('19 - Questao 2 (gaussiano)');
        print('20 - Questao 2 (speckle)');
        print('21 - Combina Imagens');
        print('22 - Abrir imagem');
        print('23 - Sair');

        op = int(raw_input('Operacao: '))
        if(op == 0):
            img2 = rgb2yuv(img)
            img2.show()
            #caminho = img.filename + '.rgb2yuv.jpg'
            #img2.save(img.filename+'.rgb2yuv')

        if(op==23):
            break;
if __name__ == "__main__":
    main()
