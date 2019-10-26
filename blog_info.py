from datetime import date
import json
from shutil import copy

print("请输入文件名：")
fName = input()
File = open(fName,'w')
jsonFile = open("blog_info.json","r") # 在 blog_info.json里添加默认配置
data = json.load(jsonFile)
File.write('---\n')
# 评论开关
print("是否开启评论？(Y/N)")
m=input()
if(m=="Y"):
    File.write("comment: true\n")
else:
    File.write("comment: false\n")
#Mathjax开关
print("是否显示数学公式？(Y/N)")
m=input()
if(m=="Y"):
    File.write("mathjax: true\n")
else:
    File.write("mathjax: false\n")
#文章标题
print("请输入文章的标题：")
m = input()
File.write("title: " + m + "\n")
#文章摘要
print("请输入文章的摘要：")
m = input()
File.write("summary: "+m+"\n")
#日期
today = date.today()
d1 = today.strftime("%y-%m-%d\n")
File.write("date: " + d1)
#作者
File.write("author: "+data['author'][0]+'\n')
#标签
print("请输入序号选择标签, 如果要添加新标签请输入-1")
size = len(data['tags'])
File.write("tags: [\n\t")
for i in range(0,size):
    print(str(i)+'. '+data['tags'][i]) 
while (1): # TODO: 一个更好的循环办法
    m=int(input())
    if(m>=0 and m<size):
        File.write("\""+data['tags'][m]+"\"")
    if(m==-1):
        print("请输入新标签的名称") # TODO: 将新标签写入文件
        m = input()
        File.write("\""+m+"\"")
    print("是否继续输入标签？(Y/N)")
    m = input()
    if(m!='Y'):
        break
    File.write(",")
File.write("\n]\n")
#分类
print("请输入序号选择分类, 如果要添加新分类请输入-1")
size = len(data['categories'])
File.write("categories: [\n\t")
for i in range(0,size):
    print(str(i)+'. '+data['categories'][i]) 
while (1):
    m=int(input())
    if(m>=0 and m<size):
        File.write("\""+data['categories'][m]+"\"")
    if(m==-1):
        print("请输入新分类的名称") # TODO: 将新分类写入文件
        m = input()
        File.write("\""+m+"\"")
    print("是否继续输入分类？(Y/N)")
    m = input()
    if(m!='Y'):
        break
    File.write(",")
File.write("\n]\n")
File.write("---\n")
#写入正文
print("请输入需要插入的文件名")
m = input()
mdFile = open(m,'r')
mdText = mdFile.read()
File.write(mdText)
File.close()
copy(fName,data['path'][0])
jsonFile.close()
mdFile.close()