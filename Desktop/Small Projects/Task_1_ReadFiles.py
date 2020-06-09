import os, fnmatch
def find(pattern, path):
    pattern=input("Enter the name of the file to find  : ")
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    print(result,"\n")
    s=input("Above are the name of files which are having same name so please choose yours to see the data : ")
    print()
    x=open(s,'r')
    y=x.readlines()
    for i in y:
        print(i,end='')
    x.close()
find('pattern', '/Users')


