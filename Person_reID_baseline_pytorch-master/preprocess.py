import os
from shutil import copyfile

import os
path = 'C:/Users/sured/Desktop/data/cam1'
files = os.listdir(path)

for ind, f in enumerate(files):
    print(f)
    p = 'C:/Users/sured/Desktop/data/cam1' + '/'+f
    print(p)
    op = os.listdir(p)
    print(op)
    for index, file in enumerate(op):
        # os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
        print(file)
        os.rename(p+'/'+file, 'C:/Users/sured/Desktop/data'+'/'+f+'_c1_'+file)