import os,json
import shutil as shut
def create_sort(path):
    try:
        os.makedirs(path)
        print("成功创建文件夹")
    except:
        print("生成文件夹失败，请检查是否路径有误或同名文件夹已存在")
def create_file(path):
    try:
        with open(os.path.join(path))as file:
            file.close()
        print("成功创建文件")
    except:
        print("创建文件失败")
def autorun(filepath,path):
    f=open("./autorun/autorun.inf","a+")
    if not "[autorun]" in f:
        f.write("[autorun]")
    f.write("open="+path+"\n\n")
    shut.move(filepath,"./autorun/")
def directionary(source,directionary):
    json_string='{"source":'+source+', "directionary":'+directionary+'}'
    with open ("./directionary.json","a+") as outfile:
        json.dump(json_string,outfile)
while True:
    a=input("")
