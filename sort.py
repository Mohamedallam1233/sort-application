import os , shutil
def find_extension(path):
    filelist = os.listdir(path)
    extensionn=[]
    for i in filelist :
        extension = os.path.splitext(i)[1]
        extensionn.append(extension)
    extensionn=set(extensionn)
    extensionn=list(extensionn)
    for i in extensionn:
        if i==''or i ==' ':
            del extensionn[extensionn.index(i)]
    for i in extensionn:
        os.mkdir(path+'\\'+i)
    filelist = os.listdir(path)
    for fichier in filelist[:]:  # filelist[:] makes a copy of filelist.
        for i in extensionn :
          if  (fichier.endswith(i)):
              dest = shutil.move('.\\'+fichier, '.\\'+i, copy_function=shutil.copytree)
find_extension('.')