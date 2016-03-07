Title: 使用IntelliJ IDEA配置Spark应用开发环境及源码阅读环境
Date: 2016-02-26 22:40
Category: Blogs
Tags: Spark, IntelliJ IDEA
Author: Tom Gou
Summary: 在本地搭建好Spark 1.6.0后，除了使用官方文档中的sbt命令打包，spark-submit提交程序外，我们可以使用IntelliJ IDEA这个IDE在本地进行开发调试，之后再将作业提交到集群生产环境中运行，使用IDE可以提升我们的开发效率。

在本地搭建好Spark 1.6.0后，除了使用官方文档中的sbt命令打包，spark-submit提交程序外，我们可以使用IntelliJ IDEA这个IDE在本地进行开发调试，之后再将作业提交到集群生产环境中运行，使用IDE可以提升我们的开发效率。转载请注明博客原文地址：[http://blog.tomgou.xyz/shi-yong-intellij-ideapei-zhi-sparkying-yong-kai-fa-huan-jing-ji-yuan-ma-yue-du-huan-jing.html](http://blog.tomgou.xyz/shi-yong-intellij-ideapei-zhi-sparkying-yong-kai-fa-huan-jing-ji-yuan-ma-yue-du-huan-jing.html)

###0.安装IntelliJ IDEA
我的系统环境（Ubuntu 14.04.4 LTS）

下载最新版本的IntelliJ IDEA，官网地址：[https://www.jetbrains.com/idea/download/](https://www.jetbrains.com/idea/download/) 。
最新版本的IntelliJ IDEA支持新建SBT工程，安装scala插件。

安装步骤：

- Unpack the idea idea-15.0.4.tar.gz file using the following command: tar xfz idea-15.0.4.tar.gz
- Run idea.sh from the bin subdirectory.

记得在IntelliJ IDEA的“Configure”菜单中，选择“Plugins”，安装“Scala”插件。

<br />
- - -

###1.以本地local模式运行Spark程序

1）创建“New Project”，选择“Scala”。“Project SDK”选择JDK目录，“Scala SDK”选择Scala目录。
![idea_conf1](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf1.png)


2）选择菜单中的“File” ->“Project Structure” ->“libraries” ->+“java”，导入Spark安装目录`/home/tom/spark-1.6.0/lib`下的“`spark-assembly-1.6.0-hadoop2.6.0.jar`”。


3）运行Scala示例程序SparkPi：
Spark安装目录的examples目录下，可以找到Scala编写的示例程序`SparkPi.scala`，该程序计算Pi值并输出。
在Project的main目录下新建`SparkPitest.scala`，复制Spark示例程序代码。
![idea_conf1](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf2.png)
选择菜单中的“Run” ->“Edit Configurations”，修改“Main class”和“VM options”。
![idea_conf1](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf3.png)

运行结果：
![idea_conf1](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf4.png)

注意：
在我最初运行Spark的测试程序SparkPi时，点击运行，出现了如下错误：
Exception in thread "main" org.apache.spark.SparkException: A master URL must be set in your configuration
从提示中可以看出找不到程序运行的master，此时需要配置环境变量。
搜索引擎查询错误后，了解到传递给spark的master url可以有如下几种，具体可以查看Spark官方文档：

- local 本地单线程
- local[K] 本地多线程（指定K个内核）
- local[*] 本地多线程（指定所有可用内核）
- spark://HOST:PORT 连接到指定的 Spark standalone cluster master，需要指定端口。
- mesos://HOST:PORT 连接到指定的 Mesos 集群，需要指定端口。
- yarn-client客户端模式 连接到 YARN 集群。需要配置 HADOOP_CONF_DIR。
- yarn-cluster集群模式 连接到 YARN 集群。需要配置 HADOOP_CONF_DIR。

在VM options中输入“`-Dspark.master=local`”，指示本程序本地单线程运行。

<br />
- - -

###2.生成jar包提交到集群
1）和本地local模式运行Spark相同，我们建立起project。

2）选择菜单中的“File” ->“Project Structure” ->“Artifact” ->“jar” ->“From Modules with dependencies”，之后选择Main Class和输出jar的Directory。
![idea_conf6](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf6.png)
![idea_conf5](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf5.png)
3）在主菜单选择“Build” ->“Build Artifact”，编译生成jar包。
4）将jar包使用`spark-submit`提交：
```bash
$SPARK_HOME/bin/spark-submit --class "SimpleApp" --master local[4] simple.jar 
```
<br />
- - -

###3.配置Spark源码阅读环境
克隆Spark源码：
```bash
$ git clone https://github.com/apache/spark
```
然后在IntelliJ IDEA中即可通过“Import Project”，选择sbt项目，选择“Use auto-import”，即可生成IntelliJ项目文件。

![idea_conf7](http://7xra46.com1.z0.glb.clouddn.com/blog3_idea/idea_conf7.png)