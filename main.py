from PIL import Image
from pdi_trabalho import onlyR,onlyRmono,onlyG,onlyGmono,onlyB,onlyBmono,yuv2rgb,rgb2yuv,negativo,brilhoaditivo,brilhomultiplicativo,media,\
                         mediana,negativobandaY,brilhoaditivobandaY,brilhomultiplicativobandaY,medianabandaY,controlfilter
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
        print('19 - Combina Imagens');
        print('20 - Abrir imagem');
        print('21 - Sair');

        op = int(raw_input('Operacao: '))
        if(op == 0):
            img2 = rgb2yuv(img)
            img2.show()
            caminho = os.getcwd()+'/rgb-yuv.jpg'
            img2.save(caminho)
        if(op == 1):
            img2 = yuv2rgb(img)
            img2.show()
            caminho = os.getcwd()+'/yuv-rgb.jpg'
            img2.save(caminho)
        if(op == 2):
            img2 = onlyR(img)
            img2.show()
            caminho = os.getcwd()+'/onlyR.jpg'
            img2.save(caminho)
        if(op == 3):
            img2 = onlyG(img)
            img2.show()
            caminho = os.getcwd()+'/onlyG.jpg'
            img2.save(caminho)
        if(op == 4):
            img2 = onlyB(img)
            img2.show()
            caminho = os.getcwd()+'/onlyB.jpg'
            img2.save(caminho)
        if(op == 5):
            img2 = onlyRmono(img)
            img2.show()
            caminho = os.getcwd()+'/onlyRmono.jpg'
            img2.save(caminho)
        if(op == 6):
            img2 = onlyGmono(img)
            img2.show()
            caminho = os.getcwd()+'/onlyGmono.jpg'
            img2.save(caminho)
        if(op == 7):
            img2 = onlyBmono(img)
            img2.show()
            caminho = os.getcwd()+'/onlyBmono.jpg'
            img2.save(caminho)
        if(op == 8):
            img2 = negativo(img)
            img2.show()
            caminho = os.getcwd()+'/negativo.jpg'
            img2.save(caminho)
        if(op == 9):
            valor = int(raw_input('Digite o valor: '))
            img2 = brilhoaditivo(img,valor)
            img2.show()
            caminho = os.getcwd()+'/brilhoaditivo'+str(valor)+'.jpg'
            img2.save(caminho)
        if(op == 10):
            valor = int(raw_input('Digite o valor: '))
            img2 = brilhomultiplicativo(img,valor)
            img2.show()
            caminho = os.getcwd()+'/brilhomultiplicativo'+str(valor)+'.jpg'
            img2.save(caminho)
        if(op == 11):
            print('ainda nao implementado!')
            continue
            #valor = int(raw_input('Digite o valor da ordem da matrix: '))
            #img2 = media(img,valor)
            #img2.show()
            #caminhos = os.getcwd()+'/media_'+str(valor)+'.jpg'
            #img2.save(caminho)
        if(op == 12):
            valor = int(raw_input('Digite o valor da ordem da matrix(3 ou 5): '))
            if(valor == 3 or valor == 5):
                img2 = mediana(img,valor)
                img2.show()
                caminho = os.getcwd()+'/mediana_'+str(valor)+'.jpg'
                img2.save(caminho)
            else:
                continue
        if(op == 13):
            img2=negativobandaY(img)
            img2.show()
            caminho = os.getcwd()+'/negativobanday.jpg'
            img2.save(caminho)
        if(op == 14):
            valor = int(raw_input('Digite o valor: '))
            img2 = brilhoaditivobandaY(img,valor)
            img2.show()
            caminho = os.getcwd()+'/brilhoaditivobandaY_'+str(valor)+'.jpg'
            img2.save(caminho)
        if(op == 15):
            valor = int(raw_input('Digite o valor: '))
            img2 = brilhomultiplicativobandaY(img,valor)
            img2.show()
            caminho = os.getcwd()+'/brilhomultiplicativobandaY_'+str(valor)+'.jpg'
            img2.save(caminho)
        if(op == 16):
            print('ainda nao implementado!')
            continue
        if(op == 17):
            valor = int(raw_input('Digite o valor da ordem da matrix(3 ou 5): '))
            if(valor == 3 or valor == 5):
                img2=medianabandaY(img,valor)
                img2.show()
                caminho = os.getcwd()+'/medianabandaY_'+str(valor)+'.jpg'
                img2.save(caminho)
            else:
                continue
        if(op == 18):
            print('ainda nao implementado!')
            continue
        if(op == 19):
            caminho = raw_input('Digite o nome da segunda imagem: ')
            img2 = Image.open(os.getcwd()+'/'+caminho)
            img3 = controlfilter(img,img2)
            img3.show()
            caminho = os.getcwd()+'/controlfilter.jpg'
            img3.save(caminho)
        if(op == 20):
            caminho = raw_input('Digite o nome da imagem: ')
            img = Image.open(os.getcwd()+'/'+caminho)
        if(op==21):
            break;
if __name__ == "__main__":
    main()
