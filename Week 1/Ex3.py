import os
import json
class Path:
    __path=''
    __file_name=''
    def __init__(self,pstring,nstring):
        self.path=pstring
        self.file_name=nstring
    def Input(self):
        a=input('nhap path:')
        b=input('nhap file_name:')
        return Path(a,b)
    def Output(self):
        print('path:',self.path)
        print('file_name:', self.file_name)
    def check(self):
        return os.path.isfile(self.path)
    def ThemVaoFileJson(self):
        my_dict={'path':self.path,'file_name':self.file_name,'exist':os.path.isfile(self.path)}
        with open('path.json','r') as r:
            mylist=json.load(r)
        mylist.append(my_dict)
        with open('path.json','w') as w:
            json.dump(mylist,w)



#check
my_path=Path('/home/phanthanhtrung/course-v3/nbs/dl1/00_notebook_tutorial.ipynb','00_notebook_tutorial.ipynb')
my_path.Output()
my_path.check()
my_path.ThemVaoFileJson()
#test khác
my_path=Path('/home/phanthanhtrung/course-v3/nbs/dl1/floyd_requirements.txt','floyd_requirements.txt')
my_path.Output()
my_path.check()
my_path.ThemVaoFileJson()