from PIL import Image,ImageFilter

def resize_fator(img,fator):
    new_img = Image.new(img.mode,(img.size[0]/fator,img.size[1]/fator))

    for row in range(0,int(new_img.size[0])):
        for col in range(0,int(new_img.size[1])):
            # Pega o pixel na imagem original
            try:
                pixel = img.getpixel((row*fator,col*fator))
            except:
                pixel = img.getpixel((row,col))
            
            # Coloca o pixel na nova imagem
            new_img.putpixel((row,col),pixel)
    return new_img

