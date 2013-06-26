import sys
import os
from PIL import Image
class filter_average:
    def __init__(self, path,ordem):
        self.im=Image.open(os.getcwd()+'/'+path)
        if(ordem != 3 and ordem != 5):
            raise NameError('Apenas e aceitado ordem 3 e 6')
        self.ordem = ordem

    
    def valueaverage(self,im,i, j, c,ordem):
        pix = []
        med = 0
        if (self.ordem == 3):
            pix=[im.getpixel((j,i))[c], im.getpixel((j+1,i))[c], im.getpixel((j-1,i))[c],\
             im.getpixel((j,i+1))[c], im.getpixel((j-1,i+1))[c], im.getpixel((j+1,i+1))[c],\
             im.getpixel((j,i-1))[c], im.getpixel((j-1,i-1))[c], im.getpixel((j+1,i-1))[c]]
        elif(self.ordem == 5):
            pix=[im.getpixel((j,i))[c], im.getpixel((j+1,i))[c], im.getpixel((j-1,i))[c],\
             im.getpixel((j,i+1))[c], im.getpixel((j-1,i+1))[c], im.getpixel((j+1,i+1))[c],\
             im.getpixel((j,i-1))[c], im.getpixel((j-1,i-1))[c], im.getpixel((j+1,i-1))[c],\
             im.getpixel((j,i+2))[c],im.getpixel((j,i-2))[c],im.getpixel((j+2,i))[c],im.getpixel((j-2,i))[c],\
             im.getpixel((j+2,i+1))[c],im.getpixel((j+2,i-1))[c],im.getpixel((j-2,i+1))[c],im.getpixel((j-2,i-1))[c],\
             im.getpixel((j+1,i+2))[c],im.getpixel((j+1,i-2))[c],im.getpixel((j-1,i+2))[c],im.getpixel((j-1,i-2))[c],\
             im.getpixel((j+2,i+2))[c],im.getpixel((j-2,i+2))[c],im.getpixel((j+2,i-2))[c],im.getpixel((j-2,i-2))[c]]
        #print(len(pix))
        for k in range(1,(len(pix)+1)):
            med+=int(pix[k-1])

        return float(med)/float(len(pix))
    def aplicar_filtro(self):
        if (self.ordem == 3):
            ajuste = 1
        elif(self.ordem == 5):
            ajuste = 2
        out=Image.new("RGB",self.im.size)
        print "\n\nAguarde, processando..."
        for i in range(ajuste,self.im.size[1]-ajuste):#percorre as linhas
            for j in range(ajuste,self.im.size[0]-ajuste):#percorre as colunas
                r = int(round(self.valueaverage(self.im,i,j,0,self.ordem)))
                g = int(round(self.valueaverage(self.im,i,j,1,self.ordem)))
                b = int(round(self.valueaverage(self.im,i,j,2,self.ordem)))
                out.putpixel((j,i), (r,g,b))
        print "\nProcessamento finalizado.\n\n"
        try:
            out.show() #mostra a imagem
        except:
            print "Nao foi possivel mostrar a imagem resultante. Visualizador nao encontrado."
            outpath=raw_input("Informe o caminho onde deseja salvar a saida: ")
        try:
            out.save(outpath)
        except:
            print "A imagem nao foi salva."
            out.putpixel((j,i), (r,g,b))
 
    
     
 
caminho=raw_input("\n\nEntre com o caminho da imagem: ")
print(caminho)
#try:
f = filter_average(caminho,5)
f.aplicar_filtro()
#except:
#    print "\n\nNao foi possivel abrir a imagem. O programa sera encerrado."
#    sys.exit()