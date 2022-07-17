import os,json,re
import shutil as shut
##############################################################
def create_sort(path):
    try:
        os.makedirs(path)
        print("成功创建文件夹")
    except:
        print("生成文件夹失败，请检查是否路径有误或同名文件夹已存在")
#e.g.:file addsort sort a
#     file addsort ./sorts/a/b
##############################################################
def create_file(path):
    try:
        with open(os.path.join(path))as file:
            file.close()
        print("成功创建文件")
    except:
        print("创建文件失败")
#e.g.:file add sort a x.log
#     file add ./sorts/a/x.txt
##############################################################
def autorun(filepath):
    f=open("./autorun/autorun.inf","a+")
    if not "[autorun]" in f:
        f.write("[autorun]")
    try:
        shut.move(filepath,"./autorun/")
        f.write("open="+os.path.basename(filepath)+"\n\n")
        print("成功创建了新的自启动文件")
    except:
        print("无法创建，请检查路径或文件是否已存在")
#e.g.:file autorun C:/Users/Administrator/Desktop/a.jar
##############################################################
def directionary(name,source,directionary):
    with open ("./directionary.json","a+") as outfile:
        outfile.write('{\"name\":'+name+', \"source\":'+source+', \"directionary\":'+directionary+'}')
        outfile.close()
    print("成功创建路径")
#e.g.:file dir name a C:/Users/Administrator/Desktop/a.jar sort a 
#     file dir name a C:/Users/Administrator/Desktop/a.jar ./sorts/a/ 
##############################################################
def copy_file(from_,to_):
    try:
        shut.copyfile(from_,to_)
        print("成功复制文件")
    except:
        print("复制失败，请检查文件路径或是否同名文件已存在")
#e.g.:file copy ./sorts/a/a.txt ./sorts/b
##############################################################
def cut_file(from_,to_):
    try:
        shut.move(from_,to_)
        print("成功剪切文件")
    except:
        print("剪切失败，请检查文件路径或是否同名文件已存在")
#e.g.:file cut ./sorts/a ./sorts/b
###############################################################
def from_System_to_UDisk_All():
    with open("./directionary.json","r") as jasonfile:
        for jasonstr in jasonfile.readlines():
            data=json.loads(jasonstr)
            copy_file(data[1],data[2])
        jasonfile.close()
#e.g.:file toDisk all
###############################################################
def from_Udisk_to_System_All():
    with open("./directionary.json","r") as jsonfile:
        for jsonstr in jsonfile.readlines():
            data1=json.loads(jsonstr)
            copy_file(data1[2],data1[1])
        jsonfile.close()
#e.g.:file fromDisk all
###############################################################
def from_System_to_UDisk(filename):
    with open("directionary.json","r") as jsonfilea:
        for jsonstr in jsonfilea.readlines():
            data2=json.loads(jsonstr)
            if data2[0]==filename:
                copy_file(data2[1],data2[2])
        jsonfilea.close()
#e.g.file toDisk a.txt
###############################################################
def from_UDisk_to_System(filename):
    with open("directionary.json","r") as jsonfileb:
        for jsonstr in jsonfileb.readlines():
            data3=json.loads(jsonstr)
            if data3[0]==filename:
                copy_file(data3[2],data3[1])
        jsonfileb.close
#e.g.file fromDisk a.txt
###############################################################
def delete_sort(path):
    try:
        os.removedirs(path)
        print("成功删除文件夹")
    except:
        print("无法删除文件夹，请检查权限以及路径")
#e.g.file delsort sort a
#    file delsort ./sorts/a
################################################################
def delete_file(path):
    try:
        os.remove(path)
        print("成功删除文件")
    except:
        print("删除文件失败，请查看权限以及路径")
#e.g.file del sort a a.txt
#    file del ./sorts/a/a.txt
################################################################
def delete_directionary(name):
    with open("directionary.json","r+") as fileagain:
        rec=re.compile(name)  
        lines=[line for line in fileagain.readlines() if rec.search(line) is None]
        fileagain.seek(0)
        fileagain.truncate(0)
        fileagain.writelines(lines)
#e.g.file deldir a.txt
################################################################
def open_file(path):
    try:
        os.startfile(path)
        print("打开了文件")
    except:
        print("请检查文件路径")
#e.g.file open sort a a.txt
#    file open ./sorts/a/a.log
################################################################
def setup_add_System(path):
    try:
        if not os.path.exists("./sorts/setup"):
            create_sort("./sorts/setup")
        shut.move(path,"./sorts/setup/")
        print("成功加入文件")
    except:
        print("错误，请检查文件路径")
#e.g.file uploadpkg C:\Users\Administrator\a.exe
################################################################
def setup_add_URL(URL):
    if not os.path.exists("./sorts/setup"):
        create_sort("./sorts/setup")
    if not os.path.exists("./sorts/setup/setup.py"):
        create_file("./sorts/setup/setup.py")
    with open ("./sorts/setup/setup.py","a+") as newpy:
        if not ("import wget,shutil"in newpy):
            newpy.write("import wget,os\nshutil.rmtree(os.getenv(\"SystemDrive\")+\"/%Username%/Download)\"")
        newpy.write("file_name = wget.filename_from_url(url)\nwget.download("+URL+",out=file_name")
        print("搞定")
        newpy.close()
#e.g.file seturl https://github.com/huanghongxun/HMCL/releases/download/v3.5.3.221/HMCL-3.5.3.221.exe
################################################################
def setup_():
    file  = os.listdir("./sorts/setup")
    for f in file:
        real_url = os.path.join ("./sorts/setup" , f)
        open_file(real_url)
    file  = os.listdir("%SystemDrive%/Users/%Username%/Downloads/")
    for f in file:
        real_url = os.path.join ("%SystemDrive%/Users/%Username%/Downloads/", f)
        open_file(real_url)
    print("打开了文件")
#e.g.file setup
################################################################
def list_file(path):
    try:
        os.system("tree "+path)
    except:
        print("无法找到目录，请检查路径")
#e.g.list
#    list sort a
#    list ./sorts
################################################################
while True:
    a=input("")
    a=a.strip()
    a=a.split()
    if a[0]=="list":
        if len(a)==1:
            list_file("./")
        else:
            if a[1]=="sort":
                if len[a]==2:
                    print("代码不完整")
                else:
                    list_file("./sorts/"+a[2])
            else:
                try:
                    list_file(a[1])
                except:
                    print("无法找到目录，请检查路径")
    elif a[0]=="help":
        with open("./help.txt","r")as help_file:
            file_content=help_file.read()
            print(file_content)
            help_file.close()
    elif a[0]=="function":
        print("待开发")
    elif a[0]=="file":
        if len(a)==1:
            print("代码不完整")
        elif a[1]=="addsort":
            if len(a)==2:
                print("代码不完整")
            elif a[2]=="sort":
                if len(a)==3:
                    print("代码不完整")
                else:
                    create_sort("./sorts/"+a[3])
            else:
                create_sort(a[2])
        elif a[1]=="add":
            if len(a)==2:
                print("代码不完整")
            elif a[2]=="sort":
                if len(a)==3 or len(a)==4:
                    print("代码不完整")
                else:
                    create_file("./sorts/"+a[3]+"/"+a[4])
            else:
                create_file(a[2])
        elif a[1]=="autorun":
            if len(a)==2:
                print("代码不完整")
            else:
                autorun(a[2])
        elif a[1]=="dir":
            if not (len(a)==6 or len(a)==7):
                print("代码不完整")
            else:
                if a[5]=="sort":
                    directionary(a[3],a[4],"./sorts/"+a[6])
                else:
                    directionary(a[3],a[4],a[5])
        elif a[1]=="copy":
            if not(len(a)==4):
                print("代码不完整")
            else:
                copy_file(a[2],a[3])
        elif a[1]=="cut":
            if not(len(a)==4):
                print("代码不完整")
            else:
                cut_file(a[2],a[3])
        elif a[1]=="toDisk":
            if len(a)!=3:
                print("代码不完整")
            else:
                if a[2]=="all":
                    from_System_to_UDisk_All()
                else:
                    from_System_to_UDisk(a[2])
        elif a[1]=="fromDisk":
            if len(a)!=3:
                print("代码不完整")
            else:
                if a[2]=="all":
                    from_Udisk_to_System_All()
                else:
                    from_UDisk_to_System(a[2])
        elif a[1]=="delsort":
            if len(a)!=4 and len(a)!=3:
                print("代码不完整")
            else:
                if a[2]=="sort":
                    delete_sort("./sorts/"+a[3])
                else:
                    delete_sort(a[2])
        elif a[1]=="del":
            if len(a)!=5 and len(a)!=3:
                print("代码不完整")
            else:
                if a[2]=="sort":
                    delete_file("./sorts/"+a[3]+"/"+a[4])
                else:
                    delete_file(a[2])
        elif a[1]=="deldir":
            if len[a]!=3:
                print("代码不完整")
            else:
                delete_directionary(a[2])
        elif a[1]=="open":
            if len(a)!=5 and len(a)!=3:
                print("代码不完整")
            else:
                if a[2]=="sort":
                    open_file("./sorts/"+a[3]+"/"+a[4])
                else:
                    open_file(a[2])
        elif a[1]=="uploadpkg":
            if len(a)!=3:
                print("代码不完整")
            else:
                setup_add_System(a[2])
        elif a[1]=="seturl":
            if len(a)!=3:
                print("代码不完整")
            else:
                setup_add_URL(a[2])
        elif a[1]=="setup":
            setup_()
        else:
            print("无此功能，若需帮助，请输入help")
    else:
        print("无此功能，若需帮助，请输入help")
    