import os
import glob

path_dir = os.getcwd() #  path_dir + dir = full path 
list = glob.glob(f'{path_dir}/*/')

for folder in list:
    source_file = ','.join(glob.glob(folder + 'result.txt')) 

    target_file = ','.join(glob.glob(path_dir + '/result.txt'))
    with open(source_file,'r') as f1:
        content = f1.read()
    with open(target_file, 'a') as f2:
        f2.write(content + "\n")
    print(source_file) 
print(list)  




