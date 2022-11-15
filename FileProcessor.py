import shutil
import os
import cpuinfo

# dictCPU=cpuinfo.get_cpu_info()
# partSize=dictCPU['l3_cache_size']
class FileProcessing:
    def __init__(self, path:str, separator:list= [226, 128, 140]):
        self.filePath=path
        self.separator=separator

        print('input columns name with comma separator')
        columns = input()
        columns = columns.replace(' ', '')
        param_list = columns.split(',')
        self.param_list = param_list

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

    def addDataFunc(self, wr_list:list):
        if len(wr_list)> len(self.param_list):
            message='there is more elements in array then columns'
            return message

        try:
            for wr in wr_list:
                self.fl.write(str(wr).encode('utf-8'))
                self.fl.write(bytearray(self.separator))
            self.fl.write(('\n').encode('utf-8'))

        except:
            print(f'Can t write data: {wr}  to: {self.fl.name}')

    def readFunc(self):

        try:
            self.fl = open(self.filePath, 'rb')
            print(self.fl.readline())
        except:
            print(f'Can t read data from: {self.fl.name}')
    def minElem(self, wr_list:list, minelem:list):
        j = 0
        while j < len(wr_list):
            if wr_list[j] < minelem[j]:
                minelem[j] = wr_list[j]
            j += 1
        return minelem

    def maxElem(self, wr_list:list, maxelem:list):
        j = 0
        while j < len(wr_list):
            if wr_list[j] > maxelem[j]:
                maxelem[j] = wr_list[j]
            j += 1
        return maxelem

    def replaceFileName(self, minelem:list, maxelem:list):
        i=len(self.filePath)-1
        k=0
        while i>0:
            if self.filePath[i]=='/':
                k=i+1
                break
            i-=1
        finalpath=self.filePath[0:k]
        b=0
        while b < len(minelem):
            finalpath+= str(self.param_list[b])+'::' + str(minelem[b]) + '::' + str(maxelem[b]) + ':::'
            b += 1
        shutil.copy(self.filePath, finalpath)
        os.remove(self.filePath)