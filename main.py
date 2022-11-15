import datetime
import random
import FileProcessor as fp
import SearchEngine as se


wr_list = [1,4,21]
fileCollect=[]


minelem=wr_list.copy()
maxelem=wr_list.copy()

directory='/home/ivan/Documents/DB/'
stt=datetime.datetime.now()
path='/home/ivan/Documents/DB/base'

# fileProc=fp.FileProcessing(param_list,path)
# fileProc.openFileWrite()
#
# i=0
# while i<1000000:
#     wr_list=[random.randint(1,1000), random.randint(1,1000000),random.randint(1,1000000)]
#     fileProc.addDataFunc(wr_list)
#     fileProc.maxElem(wr_list,maxelem)
#     fileProc.minElem(wr_list, minelem)
#     i+=1
# fileProc.closeFile()
# fileProc.replaceFileName(minelem, maxelem)
#
param='val3'
search=se.SearchEngine(directory, param)
fileCollect=search.searchFile().copy()
search.searchFile()
search.searchValue(fileCollect)
print(datetime.datetime.now()-stt)


