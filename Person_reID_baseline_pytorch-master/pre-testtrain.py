file = open('C:/Users/sured/Desktop/exp/available_id.txt', 'r')
# This will print every line one by one in the file
av_ids = file.read().strip().split(',')
print(len(av_ids))
file = open('C:/Users/sured/Desktop/exp/train_id.txt', 'r')
# This will print every line one by one in the file
train_ids = file.read().strip().split(',')
# print(train_ids)
file = open('C:/Users/sured/Desktop/exp/test_id.txt', 'r')
# This will print every line one by one in the file
test_ids = file.read().strip().split(',')
print(test_ids)
file = open('C:/Users/sured/Desktop/exp/val_id.txt', 'r')
# This will print every line one by one in the file
val_ids = file.read().strip().split(',')
# print(val_ids)

train_ids.extend(val_ids)
print(train_ids)
train_ids = [int(x) for x in train_ids ]
test_ids = [int(x) for x in test_ids ]
print(len(train_ids))
print(len(test_ids))

import os
from shutil import copyfile

import os
path = 'C:/Users/sured/Desktop/data'
files = os.listdir(path)

'''
save_path = path + '/bounding_box_train'
if not os.path.isdir(save_path):
    os.mkdir(save_path)

for ind, f in enumerate(files):
    
    check = str(f)
    check = check[:4]
    
    src_path = path + '/' + f
    dst_path = save_path + '/' + f
    if int(check) in train_ids:
        # os.rename(path+'/'+f, 'C:/Users/sured/Desktop/data/'+f+'_c1_'+file)
        print(check)
        copyfile(src_path, dst_path)
    # print(f)
    # p = 'C:/Users/sured/Desktop/data'
    # print(p)
    # op = os.listdir(p)
    # print(op)
    # for index, file in enumerate(op):
    #     # os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
    #     print(file)
    #     os.rename(p+'/'+file, 'C:/Users/sured/Desktop/data'+'/'+f+'_c1_'+file)
    '''
save_path = path + '/bounding_box_test'
save_path2 = path + '/query'
if not os.path.isdir(save_path):
    os.mkdir(save_path)
if not os.path.isdir(save_path2):
    os.mkdir(save_path2)

for ind, f in enumerate(files):
    
    ck = str(f)
    check = ck[:4]
    src_path = path + '/' + f
    dst_path = save_path + '/' + f
    src_path2 = path + '/' + f
    dst_path2 = save_path2 + '/' + f
    if int(check) in test_ids:
        if (ck[5:7]=="c3"):
        # os.rename(path+'/'+f, 'C:/Users/sured/Desktop/data/'+f+'_c1_'+file)
            print(check)
            copyfile(src_path2, dst_path2)
            
        elif (ck[5:7]=="c6"):
            copyfile(src_path2, dst_path2)
        else:
            copyfile(src_path, dst_path)
            