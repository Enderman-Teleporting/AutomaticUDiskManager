//
// Created by wyh on 2022/8/10.
//

#ifndef AUTOMATICUDISKMANAGER_ADDSORT_H
#define AUTOMATICUDISKMANAGER_ADDSORT_H
using namespace std;
void addsort(string path){
    try{
        mkdir(path.c_str());
        printf("成功创建文件夹");
    }catch {
        printf("创建失败,请检查路径或权限");
    }
}

#endif //AUTOMATICUDISKMANAGER_ADDSORT_H
