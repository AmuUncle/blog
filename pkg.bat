@REM @echo off
set HEXO_DIR=%~dp0

echo "Generating static site..."
cd %HEXO_DIR%
call hexo clean 

echo "Generating static site..."
call hexo generate

echo "copy images"
xcopy %HEXO_DIR%\source\_posts\зЊди\imgs %HEXO_DIR%\public\2021\05\06\зЊди\imgs /e /i /h /k /y

echo "Generating Done!"