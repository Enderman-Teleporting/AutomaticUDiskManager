chcp 65001
cd /d %~dp0
attrib +s +H .\Disk.py
attrib +s +H .\help.txt
echo 监测运行环境
@for /f "tokens=2" %%h in ('python -h ^| findstr /C:"usage:"') do ^
set PYVER2=%%h
@if "%PYVER2%" == "python" (@echo Python环境正常!) else (@echo 请下载Python && curl https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe --output Downloads\python.exe && explorer Downloads\python.exe)
md .\sorts
md D:\Downloads
copy nul .\directionary.json
attrib +S +H .\directionary.json
python Disk.py