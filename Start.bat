::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAxNRDimM2ivC7AS/PvHyOOTilgfaMMqbIDW26CHI9U341bvWJcj131fivcKDQ1RfR2lIAY3pg4=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAxNRDimOXixEroM1Mnu++WKo1kUV9c7cZzQ97WAIecW+HnFYIIi23tOkcg5CBJLdT+qYA4zrHwMs3yAVw==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
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