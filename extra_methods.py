import os
import json
import csv
def find_paths_enron(basicPath):
    filesHam=[]
    filesSpam=[]
    for r, d, f in os.walk(basicPath):
        for file in f:
            if '.txt' in file:
                typ=os.path.basename(r)
                if typ=='ham':
                    filesHam.append(os.path.join(r, file))
                else:
                    filesSpam.append(os.path.join(r, file))
    return filesHam,filesSpam
def find_paths_pu(basicPath):
    files_path =[]
    files_typ =[]
    for r, d, f in os.walk(basicPath):
        for file in f:
            if '.txt' in file:
                files_path.append(os.path.join(r, file))
                if(file.find('legit')>=0):
                    files_typ.append('ham')
                else:
                    files_typ.append('spam')
    return files_path, files_typ
def write_csv(string,fname,x,y1,y2):
    with open(string+"_res\\"+fname+".csv", 'w', newline='') as employee_file:
        writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['x', 'test', 'training'])
        for k, l, m in zip(x,y1,y2):
            writer.writerow([k,l,m])
