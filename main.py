import os

while True:
    a=input("")
    a=a.strip()
    if "function" in a :
        print ("暂未开发")
        continue
    m=""
    n=""
    o=""
    for word in a:
        m+=word
        if len(m)==len(a):
            if m=="file" or m=="help":
                print("出错：代码不完整")
                break
            elif m=="list":
                with open ("list.txt","r") as f:
                    data=f.read()
                    print (data)
                    break
            else:
                print("错误，无此功能")
                break
        elif word==" ":
            if m=="file ":
                a=a.lstrip(m)
                for i in a:
                    n+=i
                    if len(n)==len(a):
                        print("出错：代码不完整")
                        break
                    elif i==" ":
                        if n=="add ":
                            m=""
                            a=a.lstrip(n)
                            for mu in a:
                                m+=mu
                                if len(m)==len(a):
                                    print("出错：代码不完整")
                                    break
                                elif mu==" ":
                                    if m=="sort ":
                                        a=a.lstrip(m)
                                        for lo in a:
                                            o+=lo
                                            if len(a)==len(o):
                                                try:
                                                    os.mkdir("./sorts/"+a+"/")
                                                    print("创建了新的文件夹")
                                                    break
                                                except:
                                                    print("文件夹生成失败,请查看是否路径有误或同名文件夹已存在")
                                                    break
                                                       
