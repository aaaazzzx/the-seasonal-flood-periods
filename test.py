import os


#查找当前文件夹下的指定文件，同时返回文件目录
def eachFile(filename): 
    file = os.getcwd()    
    for root,dirs,files in os.walk(file):
        if filename in files:
            filePath = os.path.join(str(root),str(dirs))
            filePath = filePath[:-2]+filename
            return filePath

if __name__ == '__main__':
    fileName = 'data_m.txt'
    filePath = eachFile(fileName)
    print (filePath)

