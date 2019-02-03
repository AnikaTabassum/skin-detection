from PIL import Image


# we just use an empty image for the purpose of this MCVE
class mask:

    def __init__(self):
        "do "

    def readRationFIle(self):
        n = 256
        ratio = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        with open("ratio.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")

                ratio[int(x[0])][int(x[1])][int(x[2])] = float(x[3])

        #print(ratio)
        self.makeMask(ratio)

    def makeMask(self, ratio):
        im = Image.open('0050.jpg')
        pixelMap = im.load()

        width = im.size[0]
        height =im.size[1]

        img = Image.new(im.mode, im.size)
        pixelsNew = img.load()
        for i in range(width):
            for j in range(height):
                temp=pixelMap[i, j]
                r=temp[0]
                g=temp[1]
                b=temp[2]
                if ratio[r][g][b]<=0.4:
                    pixelsNew[i, j]=(255,255,255)
                else:
                    pixelsNew[i, j] =temp
        img.save("new.bmp", "BMP")
        #img.show()
                    

mask().readRationFIle()