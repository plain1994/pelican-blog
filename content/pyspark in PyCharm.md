Title: 使用PyCharm配置Spark的Python开发环境
Date: 2016-03-4 11:18
Category: Blogs
Tags: Spark, PyCharm, Python, pyspark
Author: Tom Gou
Summary: 在本地搭建好Spark 1.6.0后，除了使用spark-submit提交Python程序外，我们可以使用PyCharm这个IDE在本地进行开发调试,提升我们的开发效率。

在本地搭建好Spark 1.6.0后，除了使用spark-submit提交Python程序外，我们可以使用PyCharm这个IDE在本地进行开发调试,提升我们的开发效率。配置过程也十分简单，在stackoverflow上搜索到的。同时，IntelliJ IDEA加入Python插件后也可以使用Python开发Spark程序，配置步骤一致。转载请注明博客原文地址：[http://blog.tomgou.xyz/shi-yong-pycharmpei-zhi-sparkde-pythonkai-fa-huan-jing.html](http://blog.tomgou.xyz/shi-yong-pycharmpei-zhi-sparkde-pythonkai-fa-huan-jing.html)

###0.安装PyCharm和py4j
我的系统环境（Ubuntu 14.04.4 LTS）

下载安装最新版本的PyCharm，官网地址：[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/) 。

安装步骤：

- Unpack the pycharm-5.0.4.tar.gz using the following command: tar xfz pycharm-5.0.4.tar.gz
- Run pycharm.sh from the bin subdirectory

安装py4j：
```bash
$ sudo pip install py4j
```

<br />
- - -

###1.配置Pycharm
打开PyCharm，创建一个Project。
然后选择“Run” ->“Edit Configurations” ->“Environment variables”
![pycharm_conf1](http://7xra46.com1.z0.glb.clouddn.com/blog4_pycharm/pycharm_conf1.png)
增加SPARK_HOME目录与PYTHONPATH目录。
- SPARK_HOME:Spark安装目录
- PYTHONPATH:Spark安装目录下的Python目录
![pycharm_conf2](http://7xra46.com1.z0.glb.clouddn.com/blog4_pycharm/pycharm_conf2.png)

<br />
- - -

###2.测试Pycharm
运行一个小的Spark程序看看：
```python
"""SimpleApp"""

from pyspark import SparkContext

logFile = "/home/tom/spark-1.6.0/README.md"
sc = SparkContext("local","Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i"%(numAs, numBs))
```
运行结果：
```
Lines with a: 58, lines with b: 26
```
