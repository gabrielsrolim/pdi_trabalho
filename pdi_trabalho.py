from PIL import Image,ImageFilter


def rgb2yuv(rgb):
    yuv = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,int(rgb.size[1])):
            pixel=rgb.getpixel((row,col))
            y = (0.299*pixel[0]) + (0.587*pixel[1]) + (0.114*pixel[2])
            u = -(0.169*pixel[0]) - (0.331*pixel[1]) + (0.500*pixel[2]) + 128.0
            v = (0.500*pixel[0]) - (0.419*pixel[1]) - (0.081*pixel[2]) + 128.0
            
            yuv.putpixel((row,col),(int(y),int(u),int(v)))

    return yuv

def yuv2rgb(yuv):
    rgb = Image.new(yuv.mode,yuv.size)
    for row in range(0,yuv.size[0]):
        for col in range(0,int(rgb.size[1])):
            pixel = yuv.getpixel((row,col))
            r = 1 * pixel[0] - 0.0009267*(pixel[1]-128) + 1.4016868*(pixel[2]-128)
            g = 1 * pixel[0] - 0.3436954*(pixel[1]-128) - 0.7141690*(pixel[2]-128)
            b = 1 * pixel[0] + 1.7721604*(pixel[1]-128) + 0.0009902*(pixel[2]-128)

            if (r > 255):
                r = 255
            elif(r<0):
                r = 0
            if (g > 255):
                g = 255
            elif(g<0):
                g = 0
            if(b>255):
                b=255
            elif(b<0):
                b=0
            rgb.putpixel((row,col),(int(r),int(g),int(b)))
    return rgb

def onlyR(rgb):
    r = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            r.putpixel((row,col),(int(pixel[0]),0,0)) 
    return r

def onlyG(rgb):
    g = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            g.putpixel((row,col),(0,int(pixel[1]),0))
    return g

def onlyB(rgb):
    b = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            b.putpixel((row,col),(0,0,int(pixel[2])))
    
    return b

def onlyRmono(rgb):
    r = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            r.putpixel((row,col),(int(pixel[0]),int(pixel[0]),int(pixel[0])))

    return r

def onlyGmono(rgb):
    g = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            g.putpixel((row,col),(int(pixel[1]),int(pixel[1]),int(pixel[1])))

    return g

def onlyBmono(rgb):
    b = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            b.putpixel((row,col),(int(pixel[2]),int(pixel[2]),int(pixel[2])))

    return b
def negativo(rgb):
    n = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            rn = 255 - pixel[0]
            gn = 255 - pixel[1]
            bn = 255 - pixel[2]
            if(rn < 0):
                rn = 0
            if(gn < 0):
                gn = 0
            if(bn < 0):
                bn = 0
            n.putpixel((row,col),(rn,gn,bn))

    return n
def brilhoaditivo(rgb,valor):
    n = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            
            rb = int(pixel[0])+valor
            gb = int(pixel[1])+valor
            bb = int(pixel[2])+valor

            if(rb>255):
                rb = 255
            if(gb>255):
                gb = 255
            if(bb>255):
                bb = 255

            n.putpixel((row,col),(rb,gb,bb))

    return n

def brilhomultiplicativo(rgb,valor):
    n = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))

            rm = int(pixel[0]) * valor
            gm = int(pixel[1]) * valor
            bm = int(pixel[2]) * valor

            if (rm > 255):
                rm = 255
            if (gm > 255):
                gm = 255
            if (bm > 255):
                bm = 255

            n.putpixel((row,col),(rm,gm,bm))

    return n

def media(rgb,ordem):
    n = Image.new(rgb.mode,rgb.size)
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = rgb.getpixel((row,col))
            n.putpixel((row,col),(int(pixel[0]),int(pixel[1]),int(pixel[2])))

    n.filter(ImageFilter.MedianFilter(ordem))
    return n

def valueaverage(im,i, j, c,ordem):
    pix = []
    med = 0
    if (ordem == 3):
        pix=[im.getpixel((j,i))[c], im.getpixel((j+1,i))[c], im.getpixel((j-1,i))[c],\
         im.getpixel((j,i+1))[c], im.getpixel((j-1,i+1))[c], im.getpixel((j+1,i+1))[c],\
         im.getpixel((j,i-1))[c], im.getpixel((j-1,i-1))[c], im.getpixel((j+1,i-1))[c]]
    elif(ordem == 5):
        pix=[im.getpixel((j,i))[c], im.getpixel((j+1,i))[c], im.getpixel((j-1,i))[c],\
         im.getpixel((j,i+1))[c], im.getpixel((j-1,i+1))[c], im.getpixel((j+1,i+1))[c],\
         im.getpixel((j,i-1))[c], im.getpixel((j-1,i-1))[c], im.getpixel((j+1,i-1))[c],\
         im.getpixel((j,i+2))[c],im.getpixel((j,i-2))[c],im.getpixel((j+2,i))[c],im.getpixel((j-2,i))[c],\
         im.getpixel((j+2,i+1))[c],im.getpixel((j+2,i-1))[c],im.getpixel((j-2,i+1))[c],im.getpixel((j-2,i-1))[c],\
         im.getpixel((j+1,i+2))[c],im.getpixel((j+1,i-2))[c],im.getpixel((j-1,i+2))[c],im.getpixel((j-1,i-2))[c],\
         im.getpixel((j+2,i+2))[c],im.getpixel((j-2,i+2))[c],im.getpixel((j+2,i-2))[c],im.getpixel((j-2,i-2))[c]]
    
    for k in range(1,(len(pix)+1)):
        med+=int(pix[k-1])

    return float(med)/float(len(pix))

def mediana(rgb,ordem):
    if (ordem == 3):
        ajuste = 1
    elif(ordem == 5):
        ajuste = 2
    out=Image.new(rgb.mode,rgb.size)
    print "\n\nAguarde, processando..."
    for row in range(ajuste,rgb.size[1]-ajuste):#percorre as linhas
        for col in range(ajuste,rgb.size[0]-ajuste):#percorre as colunas
            r = int(round(valueaverage(rgb,row,col,0,ordem)))
            g = int(round(valueaverage(rgb,row,col,1,ordem)))
            b = int(round(valueaverage(rgb,row,col,2,ordem)))
            out.putpixel((col,row), (r,g,b))
    print "\nProcessamento finalizado.\n\n"
    return out

def negativobandaY(rgb):
    #yuv = rgb2yuv(rgb)
    yuv=rgb.convert('YCbCr');
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = yuv.getpixel((row,col))
            y = 1 - pixel[0]
            u = pixel[1]
            v = pixel[2]
            yuv.putpixel((row,col),(y,u,v))

    #rgb2 = yuv2rgb(yuv)
    rgb2 = yuv.convert('RGB')
    return rgb2

def brilhoaditivobandaY(rgb,valor):
    #yuv = rgb2yuv(rgb)
    yuv=rgb.convert('YCbCr');
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = yuv.getpixel((row,col))
            y = pixel[0] + valor
            u = pixel[1]
            v = pixel[2]
            yuv.putpixel((row,col),(y,u,v))

    #rgb2 = yuv2rgb(yuv)
    rgb2 = yuv.convert('RGB')
    return rgb2

def brilhomultiplicativobandaY(rgb,valor):
    #yuv = rgb2yuv(rgb)
    yuv=rgb.convert('YCbCr');
    for row in range(0,rgb.size[0]):
        for col in range(0,rgb.size[1]):
            pixel = yuv.getpixel((row,col))
            y = pixel[0] * valor
            u = pixel[1]
            v = pixel[2]
            yuv.putpixel((row,col),(y,u,v))

    #rgb2 = yuv2rgb(yuv)
    rgb2 = yuv.convert('RGB')
    return rgb2

def medianabandaY(rgb,ordem):
    #yuv = rgb2yuv(rgb)
    yuv=rgb.convert('YCbCr');
    if (ordem == 3):
        ajuste = 1
    elif(ordem == 5):
        ajuste = 2
    yuv2 = Image.new('YCbCr',yuv.size)
    print "\n\nAguarde, processando..."
    for row in range(ajuste,yuv.size[1]-ajuste):#percorre as linhas
        for col in range(ajuste,yuv.size[0]-ajuste):#percorre as colunas
            pixel = yuv.getpixel((col,row))
            y = int(round(valueaverage(yuv,row,col,0,ordem)))
            u = pixel[1]
            v = pixel[2]
            yuv2.putpixel((col,row), (y,u,v))
    print "\nProcessamento finalizado.\n\n"
    #rgb2 = yuv2rgb(yuv)
    rgb2 = yuv2.convert('RGB')
    return rgb2

def controlfilter(rgb1,rgb2):
    n = Image.new(rgb1.mode,rgb1.size)
    for row in range(0,rgb1.size[0]):
        for col in range(0,rgb1.size[1]):
            pixel1 = rgb1.getpixel((row,col))
            pixel2 = rgb2.getpixel((row,col))
            pixel = [int((pixel1[0]+pixel2[0])/2),int((pixel1[1]+pixel2[1])/2),int((pixel1[2]+pixel2[2])/2)]
            n.putpixel((row,col),(int(pixel[0]),int(pixel[1]),int(pixel[2])))

    return n