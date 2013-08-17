from PIL import Image
from pdi_trabalho3 import resize_fator

import os

def main():
    caminho = raw_input('Digite o nome da Imagem: ')
    img = Image.open(os.getcwd()+'/'+caminho)
    while(True):
        print('Digite o fator de reducao da imagem:')
        fator = int(raw_input('fator: '))
        if(fator <= 0 ):
            break;
        else:
            img_nova = resize_fator(img,fator)
            img_nova.show()
    

if __name__ == "__main__":
    main()
