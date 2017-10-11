import PIL.Image, PIL.ImageTk

class Iconos:
    ##path = "C:\\Users\\pclbu\\PycharmProjects\\HistoriaClinica\\iconos\\"
    path = "/home/pedro/Documentos/pycharmProjects/HistoriaClinica/iconos/"
    pilImagenLookup = PIL.Image.open(path+"Magnifying-Glass-icon.png")
    pilImageLogo = PIL.Image.open(path+"Logo-Editorial.png")
    pilImageExpansion = PIL.Image.open(path+"expansion.png")
    pilImageFirst = PIL.Image.open(path+"first.png")
    pilImagePrev = PIL.Image.open(path+"prev.png")
    pilImageNext = PIL.Image.open(path+"next.png")
    pilImageLast = PIL.Image.open(path+"last.png")



