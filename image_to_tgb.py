from PIL import Image
class image_to_rgb:
    def __init__(self):
        "do "


    def read_files(self, fileNameBMP, fileNameJPG):
        im = Image.open(fileNameJPG)
        rgb_im = im.convert('RGB')
        im2 = Image.open(fileNameBMP)
        rgb_im2 = im2.convert('RGB')
        width = rgb_im.size[0]
        height = rgb_im.size[1]

        row=1
        col=1
        pix=0
        while row < height + 1:
            #print("")
            rowdata=""
            #print("Row number: " + str(row))
            while col < width + 1:
                r, g, b = rgb_im.getpixel((col - 1, row - 1))
                r1, g1, b1 = rgb_im2.getpixel((col - 1, row - 1))

                if int(r1) >= 230 and int(g1) >= 230 and int(b1) >= 230:
                    #rowdata+=(str(r),str(g),str(b))
                    #reading from jpg
                    rowdata = str(r) + "," + str(g) + "," + str(b) + ","+"0" +"\n"



                else:
                    # reading from bmp
                    rowdata = str(r1) + "," + str(g1) + "," + str(b1) +","+"1"+ "\n"

                with open('newFile2.txt', 'a') as the_file:
                    the_file.write(str(rowdata))

                col = col + 1
                pix = pix + 1

            # clear out rowdata variable
            rowdata = ""
            rowdata2 = ""
            # increment the row...
            row = row + 1
            # reset the column count
            col = 1

        # output for proof!
        print("")
        print("Width = " + str(width) + " pixels")
        print("Height = " + str(height) + " pixels")
        print("Total Pixels = " + str(pix) + ".")

    def Process_all_files(self):
        i=0
        temp=""

        while i<555:
            maskPath = "E:\\skin_detection\\ibtd\\ibtd\\Mask\\"
            imagePath= "E:\\skin_detection\\ibtd\\ibtd\\"
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