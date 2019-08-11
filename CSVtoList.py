#author:myq
#this script will be committed to github,20190811
#work for RDD
import os

#workingDirectory = "D:\\exercise\\python\\(ok)1. Aarti IJSAEM 2017\\(final)data"
#workingDirectory = "D:\\exercise\python\\(ok)13. Cao ICRSE 2015\\(final)data"
#workingDirectory = "D:\\exercise\python\\(ok)14. Catal TJEECS 2016\\(final)data"
#workingDirectory = "D:\\exercise\\python\\(ok)35. Herbold TSE 2017\\(final)data"
workingDirectory = "E:\\gittorrent\\mysql-2019-06-01\\mysql-2019-06-01"
fileName = "\\List.txt"

print(workingDirectory)

root = os.getcwd()
print(root)


def file_name(file_dir):
#    line = 0
    for root, dirs, files in os.walk(file_dir):
#        print(line)
#        line = line + 1
        if root == workingDirectory:
            print(files)
            print(len(files))
            with open(workingDirectory + fileName, 'a') as f:
                for i in range(len(files)):
                    print(files[i])
                    f.write(files[i]+'\n')
                f.close()
        else:
            continue
        print(root)    #os.walk()所在目录
        print(workingDirectory)
#        print(dirs)    #os.walk()所在目录的所有目录名
#        print(files)    #os.walk()所在目录的所有非目录文件名
        print(" ")

#file_name(root)
file_name(workingDirectory)

if __name__ == '__main__':
    file_name(workingDirectory)
    pass