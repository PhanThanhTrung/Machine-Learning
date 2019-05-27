import json
import Ex1 

Inputfile = open('HomeworkTextFile.txt','r')
pathlist = (Inputfile.read()).split('\n')
namelist = [Ex1.ExtractFileName(i) for i in pathlist]
#pathlist = [{'path': i} for i in pathlist]
#namelist = [{'file_name': i} for i in namelist]
pathlist=[dict(pathlist[i],**namelist[i]) for i in range(len(pathlist))]
with open('path.json','w') as of:
    json.dump(pathlist,of)
