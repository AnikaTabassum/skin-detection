from PIL import Image
# we just use an empty image for the purpose of this MCVE
class mask:

    def __init__(self):
        "do "

    def readRationFIle(self):
        n=256
        ratio = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        with open("ratio.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")
                ratio[int(x[0])][int(x[1])][int(x[2])]=float(x[3])

        print(ratio)

    def makeMask(self, ratio):
        im = Image.open("0001.jpg")
        rgb_im = im.convert('RGB')
        width = rgb_im.size[0]
        height = rgb_im.size[1]

        row = 1
        col = 1
        pix = 0
        while row < height + 1:
            # print("")
            rowdata = ""
            # print("Row number: " + str(row))
            while col < width + 1:
                r, g, b = rgb_im.getpixel((col - 1, row - 1))

                if ratio[r][g][b]<=0.04:
                    




mask().readRationFIle()