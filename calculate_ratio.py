import numpy
import pprint


class calculate_ratio:
    def __init__(self):
        "do "

    def calculate(self):

        # skindataSet= numpy.zeros((256,256,256))
        # nonskindataSet=numpy.zeros((256,256,256))

        # i=j=k=0
        # nonskindataSet=[[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        n = 256
        ratio = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        skindataSet = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        nonskindataSet = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        cnt = 0
        with open("newFile2.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")
                # i kept 0 for jpg files
                if int(x[3]) == 0:
                    # print("mmm")
                    nonskindataSet[int(x[0])][int(x[1])][int(x[2])] += 1
                    # print("i "+str(i))
                    '''
                    print("0"+x[0])
                    print("1"+x[1])
                    print("2"+x[2])
                    print(skindataSet[int(x[0])][int(x[1])][int(x[2])])

                    '''
                    # i kept 1 for bmp files
                elif int(x[3]) == 1:
                    # print("mkmk")
                    skindataSet[int(x[0])][int(x[1])][int(x[2])] += 1
                #data.insert
        pprint.pprint(skindataSet[244][217][188])
        '''
        print(skindataSet[112][120][83])
        print(cnt)
        '''
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
                    with open("ratio.txt", 'a') as fil:
                        fil.write(string)

                    # file1.write(str(skin[x][y][z])+ " "+ str(nonSkin[x][y][z])+ "\n")

                    ratio[i][j][k] = total

                    k += 1
                j += 1
            i += 1
        print("printing")
# print(skindataSet)


calculate_ratio().calculate()
# calculate_ratio().calculate_ratio_for()