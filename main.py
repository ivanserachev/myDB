import cpuinfo
import datetime
import random
import shutil
import os

# dictCPU=cpuinfo.get_cpu_info()
# partSize=dictCPU['l3_cache_size']
class FileProcessing:
    def __init__(self, path:str, wr_list:list, param_list:list, separator:list= [226, 128, 140]):
        self.filePath=path
        self.wr_list=wr_list
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
            for wr in wr_list:
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
        while j < len(wr_list):
            if wr_list[j] < minelem[j]:
                minelem[j] = wr_list[j]
            j += 1
        return minelem

    def maxElem(self):
        j = 0
        while j < len(wr_list):
            if wr_list[j] > maxelem[j]:
                maxelem[j] = wr_list[j]
            j += 1
        return maxelem

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
        while b < len(minelem):
            finalpath+= str(self.param_list[b])+'::' + str(minelem[b]) + '::' + str(maxelem[b]) + ':::'
            b += 1
        shutil.copy(self.filePath, finalpath)
        os.remove(self.filePath)

class SearchEngine:
    def __init__(self, directory:str, search_value, paramname:str, separator:list= [226, 128, 140]):
        self.directory=directory
        self.s_value=search_value
        self.paramname=paramname
        self.fileCollect=fileCollect
        self.separator=separator

    def searchFile(self):
        file_list=os.listdir(self.directory)
        fileCollection=[]
        for file in file_list:
            if ':::' in file:
                try:
                    c = file.index(self.paramname)
                except:
                    print(f'There is no files with this column: {self.paramname} in this folder: {self.directory}')
                    break
                c+=len(self.paramname)+2
                start_range = ''
                finish_range = ''
                while c < len(file) - 1:
                    if file[c] != ':':
                        start_range += file[c]
                    elif file[c] == ':' and file[c + 1] == ':':
                        break
                    c+=1
                c += 2
                while c < len(file) - 1:
                    if file[c] != ':':
                        finish_range += file[c]
                    elif file[c] == ':' and file[c + 1] == ':' and file[c + 2] == ':':
                        break
                    c+=1

                val_type=type(self.s_value)
                if val_type(self.s_value) >= val_type(start_range) and val_type(self.s_value) <= val_type(finish_range):
                    fileCollection.append(file)

        return fileCollection

    def searchValue(self):

        for file in fileCollect:
            fl=open(f'/home/ivan/Documents/DB/{file}','rb')
            lines=fl.readlines()
            for l in lines:
                ln = l.split(bytearray(self.separator))
                if str(self.s_value).encode('utf-8')==ln[0]:
                    print(ln)
            fl.close()


wr_list = [1,4,21]
fileCollect=[]
param_list=['val1','val2','val3']
minelem=wr_list.copy()
maxelem=wr_list.copy()
path='/home/ivan/Documents/DB/base'
directory='/home/ivan/Documents/DB/'
stt=datetime.datetime.now()

fileProc=FileProcessing(path,wr_list,param_list)
fileProc.openFileWrite()
i=0
while i<1000000:
    wr_list=[random.randint(1,1000), random.randint(1,1000000),random.randint(1,1000000)]
    fileProc.addDataFunc()
    fileProc.maxElem()
    fileProc.minElem()
    i+=1
fileProc.closeFile()
fileProc.replaceFileName()

param='val1'
search=SearchEngine(directory, 1,param)
fileCollect=search.searchFile().copy()
search.searchFile()
search.searchValue()
print(datetime.datetime.now()-stt)
