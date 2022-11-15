import os

class SearchEngine:
    def __init__(self, directory:str,paramname:str, separator:list= [226, 128, 140]):
        self.directory=directory
        print('input search value')
        search_value=input()
        self.s_value=search_value
        self.paramname=paramname
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

    def searchValue(self, fileCollect:list):

        for file in fileCollect:
            fl=open(f'/home/ivan/Documents/DB/{file}','rb')
            lines=fl.readlines()
            for l in lines:
                ln = l.split(bytearray(self.separator))
                if str(self.s_value).encode('utf-8')==ln[0]:
                    print(ln)
            fl.close()