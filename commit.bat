@echo off
set HEXO_DIR=.

echo "Deploying to server..."
git add .
git commit -m "ÐÂÔö²©¿Í"
git push origin blog:blog

echo "Deploying Done!"
