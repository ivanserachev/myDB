import shutil
import main
import os

class FileProcessing:
    def __init__(self, path:str, param_list:list, separator:list= [226, 128, 140]):
        self.filePath=path
        self.separator=separator
        self.param_list=param_list

    def openFileWrite(self):
        try:
            self.fl = open(self.filePath, 'wb')
        except:
            print(f'Error. Cant create or open file. Check file path: {self.filePath}')

    def openFileAdd(self):
        try:
            self.fl = open(self.filePath, 'ab')
        except:
            print(f'Error. Cant create or open file. Check file path: {self.filePath}')
    def closeFile(self):
        self.fl.close()

    def addDataFunc(self):

        try:
            for wr in main.wr_list:
                self.fl.write(str(wr).encode('utf-8'))
                self.fl.write(bytearray(self.separator))
            self.fl.write(('\n').encode('utf-8'))

        except:
            print(f'Can t write data: {wr} to: {self.fl.name}')


    def readFunc(self):

        try:
            self.fl = open(self.filePath, 'rb')
            print(self.fl.readline())
        except:
            print(f'Can t read data from: {self.fl.name}')
    def minElem(self):
        j = 0
        while j < len(main.wr_list):
            if main.wr_list[j] < main.minelem[j]:
                main.minelem[j] = main.wr_list[j]
            j += 1
        return main.minelem

    def maxElem(self):
        j = 0
        while j < len(main.wr_list):
            if main.wr_list[j] > main.maxelem[j]:
                main.maxelem[j] = main.wr_list[j]
            j += 1
        return main.maxelem

    def replaceFileName(self):
        i=len(self.filePath)-1
        k=0
        while i>0:
            if self.filePath[i]=='/':
                k=i+1
                break
            i-=1
        finalpath=self.filePath[0:k]
        b=0
        while b < len(main.minelem):
            finalpath+= str(self.param_list[b])+'::' + str(main.minelem[b]) + '::' + str(main.maxelem[b]) + ':::'
            b += 1
        shutil.copy(self.filePath, finalpath)
        os.remove(self.filePath)