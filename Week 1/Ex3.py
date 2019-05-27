import os
import json
class Path:
    __path=''
    __file_name=''


    def __init__(self,pstring,nstring):
        self.__path=pstring
        self.__file_name=nstring

    def Input(self):
        self.__path=input('nhap path:')
        self.__file_name=input('nhap file_name:')

    def Output(self):
        print('path:',self.__path)
        print('file_name:', self.__file_name)

    def check(self):
        return os.path.isfile(self.__path)

    def ThemVaoFileJson(self):
        my_dict={'path':self.__path,'file_name':self.__file_name,'exist':os.path.isfile(self.__path)}
        with open('path.json','r') as r:
            mylist=json.load(r)
        mylist.append(my_dict)
        with open('path.json','w') as w:
            json.dump(mylist,w)



#check
my_path=Path('/home/phanthanhtrung/course-v3/nbs/dl1/00_notebook_tutorial.ipynb','00_notebook_tutorial.ipynb')
my_path.Output()
print(my_path.check())
my_path.ThemVaoFileJson()

my_path.Input()
my_path.Output()
#test khác
my_path=Path('/home/phanthanhtrung/course-v3/nbs/dl1/floyd_requirements.txt','floyd_requirements.txt')
my_path.Output()
my_path.ThemVaoFileJson()