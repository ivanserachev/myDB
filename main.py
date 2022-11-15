import cpuinfo
import datetime
import random
import FileProcessor as fp
import SearchEngine as se

# dictCPU=cpuinfo.get_cpu_info()
# partSize=dictCPU['l3_cache_size']

wr_list = [1,4,21]
fileCollect=[]
param_list=['val1','val2','val3']
minelem=wr_list.copy()
maxelem=wr_list.copy()
path='/home/ivan/Documents/DB/base'
directory='/home/ivan/Documents/DB/'
stt=datetime.datetime.now()

fileProc=fp.FileProcessing(path,wr_list,param_list)
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

param='val3'
search=se.SearchEngine(directory, 1,param)
fileCollect=search.searchFile().copy()
search.searchFile()
search.searchValue()
print(datetime.datetime.now()-stt)
