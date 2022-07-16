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
#e.g.:file dir C:/Users/Administrator/Desktop/a.jar sort a 
#     file dir C:/Users/Administrator/Desktop/a.jar ./sorts/a/
##############################################################
def copy_file(from_,to_):
    try:
        copy_file(from_,to_)
        print("成功复制文件")
    except:
        print("复制失败，请检查文件路径或是否同名文件已存在")
#e.g.:file copy ./sorts/a sort b
#     file copy sort a sort b
#     file copy ./sorts/a ./sorts/b
#     file copy sort a ./sorts/b
##############################################################
def cut_file(from_,to_):
    try:
        shut.move(from_,to_)
        print("成功剪切文件")
    except:
        print("剪切失败，请检查文件路径或是否同名文件已存在")
#e.g.:file cut ./sorts/a sort b
#     file cut sort a sort b
#     file cut ./sorts/a ./sorts/b
#     file cut sort a ./sorts/b
###############################################################
def from_System_to_UDisk_All():
    with open("./directionary.json","r") as jasonfile:
        for jasonstr in jasonfile.readlines():
            data=json.loads(jasonstr)
            copy_file(data[1],data[2])
        jasonfile.close()
#e.g.:file toDisk all
###############################################################
def from_Udisk_tk_System_all():
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
while True:
    a=input("")
