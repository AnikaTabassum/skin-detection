from PIL import Image
import pprint
class image_to_rgb:
    def __init__(self):
        "do "


    def read_files(self, fileNameBMP, fileNameJPG):
        im = Image.open(fileNameJPG)
        pixelMap = im.load()
        rgb_im = im.convert('RGB')
        im2 = Image.open(fileNameBMP)
        pixelMapBMP=im2.load()
        rgb_im2 = im2.convert('RGB')
        width = rgb_im.size[0]
        height = rgb_im.size[1]
        n=256
        ratio = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        skindataSet = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        nonskindataSet = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]

        row=0

        pix=0
        for i in range(width):
            for j in range(height):
                temp = pixelMap[i, j]
                temp2= pixelMapBMP[i,j]
                r = temp[0]
                g = temp[1]
                b = temp[2]

                r1 = temp[0]
                g1 = temp[1]
                b1 = temp[2]


                ##r, g, b = rgb_im.getpixel((col - 1, row - 1))
                #r1, g1, b1 = rgb_im2.getpixel((col - 1, row - 1))

                if int(r1) >= 230 and int(g1) >= 230 and int(b1) >= 230:
                    #rowdata+=(str(r),str(g),str(b))
                    #reading from jpg
                    nonskindataSet[int(r)][int(g)][int(b)] += 1
                    rowdata = str(r) + "," + str(g) + "," + str(b) + ","+"0" +"\n"



                else:
                    # reading from bmp
                    skindataSet[int(r1)][int(g1)][int(b1)] += 1
                    rowdata = str(r1) + "," + str(g1) + "," + str(b1) +","+"1"+ "\n"

                #col = col + 1
                pix = pix + 1

            # clear out rowdata variable
            rowdata = ""
            rowdata2 = ""
            # increment the row...
            #row = row + 1
            # reset the column count


        # output for proof!
        print("")
        print("Width = " + str(width) + " pixels")
        print("Height = " + str(height) + " pixels")
        print("Total Pixels = " + str(pix) + ".")

        self.calculate_ratio_for(skindataSet, nonskindataSet, ratio)

    def calculate_ratio_for(self, skindataSet, nonskindataSet, ratio):
        pprint.pprint(nonskindataSet[112][120][83])
        i = 0
        while i < 256:
            j = 0
            while j < 256:
                k = 0

                while k < 256:
                    #total = 0.0
                    s = float(skindataSet[i][j][k])
                    ns = float(nonskindataSet[i][j][k])
                    #print(ns)
                    if nonskindataSet[i][j][k] != 0:
                        total = float(s/ns)
                        #print(s)
                    elif skindataSet[i][j][k] == nonskindataSet[i][j][k] == 0:
                        total = 0.0
                    else:
                        total = 1.0

                    string = str(i) + "," + str(j) + "," + str(k) + "," + str(total) + "\n"
                    with open("ratio2.txt", 'a') as fil:
                        fil.write(string)

                    # file1.write(str(skin[x][y][z])+ " "+ str(nonSkin[x][y][z])+ "\n")

                    ratio[i][j][k] = total

                    k += 1
                j += 1
            i += 1
        print("printing")

    def Process_all_files(self):
        i=0
        temp=""

        while i<555:
            maskPath = "D:\\SkinDetection\\ibtd\\Mask\\"
            imagePath= "D:\\SkinDetection\\ibtd\\"
            #print(maskPath)
            bmp=""
            img=""
            if i<10:

                ttt="000"+str(i)
                bmp=img=ttt
                bmp+=".bmp"
                img+=".jpg"
                maskPath+=bmp
                imagePath+=img
                print(maskPath)
                print(imagePath)
            elif i>=10 and i<100:
                ttt = "00" + str(i)
                bmp = img = ttt
                bmp += ".bmp"
                img += ".jpg"
                maskPath += bmp
                imagePath += img
                print(maskPath)
                print(imagePath)

            else:
                ttt = "0" + str(i)
                bmp = img = ttt
                bmp += ".bmp"
                img += ".jpg"
                maskPath += bmp
                imagePath += img
                print(maskPath)
                print(imagePath)

            i+=1
            self.read_files(maskPath,imagePath)


    # create an empty output row
rowdata = ""
rowdata2 = ""

#image_to_rgb().read_files()
image_to_rgb().Process_all_files()