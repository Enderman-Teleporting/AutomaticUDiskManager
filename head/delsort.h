//
// Created by wyh on 2022/8/10.
//

#ifndef AUTOMATICUDISKMANAGER_DELSORT_H
#define AUTOMATICUDISKMANAGER_DELSORT_H
using namespace std;
void delsort(string path){
    try{
        rmdir(path.c_str());
        cout<<"删除成功"<<endl;
    }catch{
        cout<<"删除失败,请检查路径或权限"<<endl;
    }
}

#endif //AUTOMATICUDISKMANAGER_DELSORT_H
