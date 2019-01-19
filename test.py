import numpy
import pprint
class calculate_ratio:
    def __init__(self):
        "do "

    def calculate(self):

        #skindataSet= numpy.zeros((256,256,256))
        #nonskindataSet=numpy.zeros((256,256,256))

        #i=j=k=0
        #nonskindataSet=[[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        n = 256
        ratio = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        skindataSet =[[[0 for k in range(n)] for j in range(n)] for i in range(n)] 
        nonskindataSet = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        cnt=0
        with open("newFile.txt", 'r') as f:
            for txt in f:
                x=txt.split(",")
                
                if int(x[3])==0:
                    #print("mmm")
                    nonskindataSet[int(x[0])][int(x[1])][int(x[2])]+=1
                    #print("i "+str(i))
                    '''
                    print("0"+x[0])
                    print("1"+x[1])
                    print("2"+x[2])
                    print(skindataSet[int(x[0])][int(x[1])][int(x[2])])
                    '''
                elif int(x[3])==1:
                    #print("mkmk")
                    skindataSet[int(x[0])][int(x[1])][int(x[2])]+=1
        '''        #data.insert
        pprint.pprint(nonskindataSet[112][120][83])
        print(skindataSet[112][120][83])
        print(cnt)
        '''
        self.calculate_ratio_for(skindataSet,nonskindataSet,ratio)
    def calculate_ratio_for(self,skindataSet,nonskindataSet, ratio):
        i=200
        while i<256:
            j=200
            while j<256:
                k=200
                total=0
                while k<256:

                    total=int(skindataSet[i][j][k]+nonskindataSet[i][j][k])
                    s=float(skindataSet[i][j][k])
                    ns=float(nonskindataSet[i][j][k])
                    if ns==0.0 :
                        
                        ratio[i][j][k]=0
                        

                    else:
                        
                        #print("S "+ str(skindataSet[i][j][k]))
                        ratio[i][j][k]=float(s/ns)
                    string=str(i)+","+str(j)+","+str(k)+","+str(ratio[i][j][k])+"\n"
                    with open("heb.txt", 'a') as fil:
                        fil.write(string)
                        
                    #print(total)

                    k+=1
                j+=1
            i+=1
        print("printing")
        #print(skindataSet)

calculate_ratio().calculate()
#calculate_ratio().calculate_ratio_for()

