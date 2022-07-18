# AutomaticUDiskManager
中文|Chinese
该仓库为作者第一个公开仓库，若有问题，请指教。
希望多多通过拉取请求以及在Issue内反馈是这个程序更完善。
本仓库是一个U盘自动化批处理程序仓库，建议将Release中的压缩文件下载解压后剪切文件（不连外面的文件夹）放入U盘根目录中。
该仓库专为又爱打字又懒得将U盘中的东西打开来打开去复制来复制去的同志。
具体运行时指令请前往Wiki
该仓库的局限性：
    容易出现因访问权限问题而产生的误报。
    
    open指令在程序在有特定的（比如多个）关联运行程序时同样会报“路径错误”,使用该指令打开文件夹或EXE文件更为保险。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
English|英语
This repo is mainly written in Chinese but is still friendly to English users.
This repo is the first public repo of the owner. If there is any problems, please give me some instructions.
This repo is for a U-Disk automatic batching program. It will be better to put the files without the folder outside in the root of your U-Disk after you download the zipped file from Release and unzip it.
This repo is specially made for dudes who love typing and hate keeping opening and moving and copying files from or to the disk.
For the commands, you may go to Wiki of the repo.
The shortcomings of this repo:
    It would probably report by mistake that the command is wrong. It is because of the "Permission Denied" error of the pyfile.

    The "open" command will report "路径错误"(wrong path) if one file have no certain (for example more than one) related app. It will be better to uses the command to open folders or EXE files.

