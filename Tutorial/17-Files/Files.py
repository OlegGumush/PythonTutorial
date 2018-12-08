import os
import shutil
rootDir = 'C:\\Python27'

for subdir , dirs , files in os.walk(rootDir):
    #print subdir
    #print dirs
    #print files

    for f in files :
        file_name = os.path.join(subdir , f)
        #print file_name
        with open(file_name) as file_handler:
            for index , l in enumerate(file_handler) :
                if ' python ' in l :
                    #print file_name , index
                    pass

#serach all files that their name contains python
for subdir , dirs , files in os.walk(rootDir):
    for f in files :
        file_name = os.path.join(subdir , f)
        #print file_name
        if 'python' in file_name:
            print file_name


#make dir same
if not os.path.exists(r'c:\python'):
    os.mkdir(r'c:\python')

with open(os.path.join('c:\\python','oleg.txt'), 'a') as f :
    f.write("hello world")

#os.remove('c:\\python\\oleg.txt')
#os.rmdir('c:\\python\\')

#os.rename('c:\\python\\oleg.txt' , 'c:\\python\\oleg1.txt')
#os.remove('c:\\python\\oleg1.txt')
#os.rmdir('c:\\python\\')

#shutil.copyfile('src' , 'dest')
#copy folder shutil.copytree()



##########################################################################
print
print
print
print __file__
print os.path.join(os.path.dirname(__file__) , os.pardir , 'hi.txt')
print os.path.normpath(os.path.join(os.path.dirname(__file__) , os.pardir , 'hi.txt'))
print os.path.basename(os.path.join(os.path.dirname(__file__) , os.pardir , 'hi.txt'))
print os.path.exists()