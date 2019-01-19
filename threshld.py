from PIL import Image
im = Image.open("testFile.jpg")
rgb_im = im.convert('RGB')

row=1
col=1
pix=0
while row < height + 1:
    #print("")
    rowdata=""
    #print("Row number: " + str(row))
    while col < width + 1:
		r, g, b = rgb_im.getpixel((col - 1, row - 1))
		#r1, g1, b1 = rgb_im2.getpixel((col - 1, row - 1))

		
		with open('output.txt', 'w+') as the_file:
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

