Title: Spark 1.6.0 单机安装配置
Date: 2016-02-25 19:08
Category: Blogs
Tags: Spark, Installation, Hadoop
Author: Tom Gou
Summary: 用Ubuntu 14.04.4 LTS当主系统已经有一段时间了，以前在8节点服务器配置过Spark和Hadoop，今天花一点时间在单机部署一下Spark吧，整理好自己的Spark开发环境。

本文将介绍Apache Spark 1.6.0在单机的部署，与在集群中部署的步骤基本一致，只是少了一些master和slave文件的配置。直接安装scala与Spark就可以在单机使用，但如果用到hdfs系统的话hadoop和jdk也要配置，建议全部安装配置好。

###0.Spark的安装准备

Spark官网的文档 [http://spark.apache.org/docs/latest/](http://spark.apache.org/docs/latest/) 里是这样说的：

> 
Spark runs on Java 7+, Python 2.6+ and R 3.1+. For the Scala API, Spark 1.6.0 uses Scala 2.10. You will need to use a compatible Scala version (2.10.x).

我的电脑环境是Ubuntu 14.04.4 LTS，还需要安装：

- [jdk-8u73-linux-x64.tar.gz](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
- [hadoop-2.6.0.tar.gz](http://apache.claz.org/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz)
- [scala-2.10.6.tgz](http://www.scala-lang.org/download/2.10.6.html)
- [spark-1.6.0-bin-hadoop2.6.tgz](http://spark.apache.org/downloads.html)

<br />
- - -

###1.安装jdk
解压jdk安装包到任意目录：

```shell
cd /home/tom
$ tar -xzvf jdk-8u73-linux-x64.tar.gz
$ sudo vim /etc/profile
```

编辑/etc/profile文件，在最后加上java环境变量：

```
export JAVA_HOME=/home/tom/jdk1.8.0_73/
export JRE_HOME=/home/tom/jdk1.8.0_73/jre
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
```

保存并更新`/etc/profile`：

```shell
$ source /etc/profil
```

查看是否成功：

```shell
$ java -version
```

<br />
- - -

###2.配置ssh localhost
确保安装好ssh：

```shell
$ sudo apt-get update
$ sudo apt-get install openssh-server
$ sudo /etc/init.d/ssh start
```

生成并添加密钥：

```shell
$ ssh-keygen -t rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```

如果已经生成过密钥，只需执行后两行命令。
测试ssh localhost

```shell
$ ssh localhost
$ exit
```

<br />
- - -

###3.安装hadoop2.6.0
解压hadoop2.6.0到任意目录：

```shell
$ cd /home/tom
$ wget http://apache.claz.org/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz
$ tar -xzvf hadoop-2.6.0.tar.gz
```

编辑`/etc/profile`文件，在最后加上java环境变量：

```
export HADOOP_HOME=/home/tom/hadoop-2.6.0
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```
编辑`$HADOOP_HOME/etc/hadoop/hadoop-env.sh`文件

```shell
$ vim $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

在最后加上：

```
export JAVA_HOME=/home/tom/jdk1.8.0_73/
```

修改Configuration文件：
```shell
$ cd $HADOOP_HOME/etc/hadoop
```

修改`core-site.xml`：

```
<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>
```

修改`hdfs-site.xml`：

```
<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/tom/hadoopdata/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/tom/hadoopdata/hdfs/datanode</value>
</property>
</configuration>
```

第一个是dfs的备份数目，单机用1份就行，后面两个是namenode和datanode的目录。

修改`mapred-site.xml`：

```
<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>
```

修改`yarn-site.xml`：

```
<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>
```

初始化hadoop：

```shell
$ hdfs namenode -format
```
启动

```shell
$ $HADOOP_HOME/sbin/start-all.sh
```

停止

```shell
$ $HADOOP_HOME/sbin/stop-all.sh
```

检查WebUI，浏览器打开端口：[http://localhost:8088](http://localhost:8088)

- port 8088: cluster and all applications 
- port 50070: Hadoop NameNode
- port 50090: Secondary NameNode 
- port 50075: DataNode 

hadoop运行后可使用`jps`命令查看,得到结果：

```
10057 Jps
9611 ResourceManager
9451 SecondaryNameNode
9260 DataNode
9102 NameNode
9743 NodeManager
```
<br />
- - -

###4.安装scala
解压scala安装包到任意目录：

```shell
$ cd /home/tom
$ tar -xzvf scala-2.10.6.tgz
$ sudo vim /etc/profile
```

在`/etc/profile`文件的末尾添加环境变量：

```
export SCALA_HOME=/home/tom//scala-2.10.6
export PATH=$SCALA_HOME/bin:$PATH
```

保存并更新`/etc/profile`：

```shell
$ source /etc/profil
```

查看是否成功：

```shell
$ scala -version
```

<br />
- - -

###5.安装Spark
解压spark安装包到任意目录：

```shell
$ cd /home/tom
$ tar -xzvf spark-1.6.0-bin-hadoop2.6.tgz
$ mv spark-1.6.0-bin-hadoop2.6 spark-1.6.0
$ sudo vim /etc/profile
```

在`/etc/profile`文件的末尾添加环境变量：

```
export SPARK_HOME=/home/tom/spark-1.6.0
export PATH=$SPARK_HOME/bin:$PATH
```

保存并更新`/etc/profile`：

```
$ source /etc/profil
```

在conf目录下复制并重命名`spark-env.sh.template`为`spark-env.sh`：

```shell
$ cp spark-env.sh.template spark-env.sh
$ vim spark-env.sh
```

在`spark-env.sh`中添加：

```
export JAVA_HOME=/home/tom/jdk1.8.0_73/
export SCALA_HOME=/home/tom//scala-2.10.6
export SPARK_MASTER_IP=localhost
export SPARK_WORKER_MEMORY=4G
```

启动

```shell
$ $SPARK_HOME/sbin/start-all.sh
```

停止

```shell
$ $SPARK_HOME/sbin/stop-all.sh
```

测试Spark是否安装成功：

```shell
$ $SPARK_HOME/bin/run-example SparkPi
```

得到结果：

```
Pi is roughly 3.14716
```
检查WebUI，浏览器打开端口：[http://localhost:8080](http://localhost:8080)





