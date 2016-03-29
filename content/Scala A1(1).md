Title: 快学Scala初级A1整理(1)
Date: 2016-03-27 14:08
Category: Blogs
Tags: Scala, Spark, basic
Author: Tom Gou
Summary: Scala是一门有趣且实用的语言，它以JVM位目标环境，将面向对象和函数式编程有机地结合起来，带来独特的编程体验。本文主要整理《快学Scala》中的初级A1部分，适用于Scala的初级应用开发学习。


Scala是一门有趣且实用的语言，它以JVM位目标环境，将面向对象和函数式编程有机地结合起来，带来独特的编程体验。本文主要整理《快学Scala》中的初级A1部分，适用于Scala的初级应用开发学习。转载请注明博客原文地址：[http://blog.tomgou.xyz/kuai-xue-scalachu-ji-a1zheng-li-1.html](http://blog.tomgou.xyz/kuai-xue-scalachu-ji-a1zheng-li-1.html)


### 0.安装和运行scala
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
建立一个简单的scala程序`scalatest.scala`：
```scala
object scalatest {
  def main(args:Array[String]){
    def box(s:String){
      var border = "-" * s.length + "--\n"
      println(border + "|" + s +"|\n" + border)
    }
    box("Hello Tom!")

  }
}
```
编译程序：
```bash
$  scalac scalatest.scala
```
执行程序：
```bash
$  scala scalatest
```
得到结果：
```
------------
|Hello Tom!|
------------
```


---

### 1.Scala基础
#### 1.1 Scala解释器
Scala解释器读到一个表达式，对它求值，将其打印，接着再继续读下一个表达式。这个过程被称为读取-求值-打印-循环，即REPL。
```
scala> 8 * 5 + 2
res0: Int = 42
```
从技术上讲，scala程序并不是一个解释器。实际发生的过程是，你输入的内容被快速地编译成字节码，然后这段字节码交由Java虚拟机执行。

> REPL在同一时间只能看到一行代码。
> 在REPL粘贴成块代码，需要键入`:paste`，粘贴代码块，然后按下Ctrl+D。

#### 1.2 常量与变量
以val定义常量，以var定义变量：
```scala
val answer = 8 * 5 + 2
var counter = 0
counter = 1
```
在Scala中，我们鼓励使用val。同时，你不需要给出值或者变量的类型，这个信息可以从你初始化它的表达式中判断出来。必要时，可指定类型，如：
```scala
val greeting: String = null
```
在Scala中，无需分号，仅当同一行代码中存在多条语句时才用分号分开。

#### 1.3 常用类型
和Java一样，Scala有7种数据类型：
Byte Char Short Int Long Float Double Boolean
跟Java不同的是，这些类型是类。你可以对数字执行方法，如：
```scala
1.toString() //产出字符串"1"
1.to(5) //产出Range(1,2,3,4,5)
```
Scala用底层的java.lang.String类来表示字符串，不过通过StringOps类给字符串追加了上百种操作，比如：
```scala
"Hello".intersect("World") //输出"lo"
```
Scala还提供了RichInt，RichDouble，RichChar等，提供了Int，Double，Char不具备的便捷方法。比如`1.to(10)`中，Int值1首先被转换成RichInt，然后调用to方法。

#### 1.4 算术和操作符重载
+-*/%等操作符实际上是方法，比如`a+b`是如下方法`a.+(b)`的简写。
通常你可以用`a 方法 b`来简写方法`a.方法(b)`。比如`1.to(5)`可以写成`1 to 5`。
Scala没有提供`++`和`--`操作符，需要使用`+=1`或`-=1`，如`counter += 1`。

#### 1.5 调用函数和方法
在Scala中使用数学函数比Java简单，你不需要从某个类调用它的静态方法。
```scala
sqrt(2)
pow(2, 4)//16.0
min(3, Pi)//3.0
```
这些数学函数在`scala.math`包中定义，可以通过以下语句引入：
```scala
import scala.math._ //在Scala中，_字符是通配符，类似Java中的*
```
引入以scala.开头的包时，可以省去scala前缀。
不带参数的Scala方法通常不使用圆括号，如：
```scala
"Hello".distinct
```

#### 1.6 apply方法
```scala
"Hello"(4)//将产出'o'
```
`"Hello"(4)`是如下方法的简写：
```scala
"Hello".apply(4)
```
`()`操作符可以作为apply方法的重载形式，比如说将字符串或数字转换成BigInt对象的apply方法,`BigInt("123")`是`BigInt.apply("123")`的简写，`Array(1,4,9)`返回一个数组，用的就是Array伴生对象的apply方法。

#### 1.7 Scaladoc
可以在[http://www.scala-lang.org/api](http://www.scala-lang.org/api)在线浏览Scaladoc。
- 类名旁的O和C分别链接到对应的类（C）和伴生对象（O）
- 标记为implicit的方法对应的是自动隐式转换
- 方法可以以函数作为参数

---

### 2.控制流与函数
#### 2.1 条件表达式
Scala中的if/else表达式有值，这个值就是if或else后的值，如：
```scala
val s = if (x > 0) 1 else -1
```
上式将if/else表达式的值赋值给常量。还可以这样写：
```scala
if (x > 0) s = 1 else s = -1
```
不过第一种写法更好，第二种写法中，s必须是变量var。

如下是混合类型的条件表达式：
```scala
if (x > 0) "positive" else -1
```
一个分支是String，另一个是Int，它们的公共超类型叫做Any。

当if语句没有输出值时，引入了Unit类，写做`()`。如下：
```scala
if (x > 0) 1 else ()
```
`()`可以当做是表示“无有用值”的占位符。

#### 2.2 语句终止
Scala与JavaScript等脚本语言类似，行尾位置不需要分号。
如果你在写较长的语句，需要分两行来写的话，确保第一行以一个不能用作语句结尾的符号结尾，如：
```scala
s = s0 + (v - v0) * t +
	0.5 * (a - a0) * t * t
```
Scala程序员倾向使用Kernighan & Ritchie风格的花括号：
```scala
if (n > 0) {
	r = r * n
    n -= 1
}
```
#### 2.3 块表达式与赋值
在Scala中，`{}`块包含一系列表达式。块中最后一个表达式的值就是块的值。如：
```scala
val distance = {val dx=x-x0;val dy=y-y0;sqrt(dx*dx+dy*dy)}
```
赋值动作本身是没有值的，是Unit类型的。一个以赋值语句结束的块，比如：`{r=r*n;n-=1}`的值是Unit类型的。`x=y=1//别这样`中，x被赋的值是Unit类型的。

#### 2.4 输入与输出
打印：
```scala
print("hello")
println(42) //打印内容后会追加一个换行符
```
格式化字符串的printf：
```scala
printf(" %s is %d years old.\n","Fred",42)
```
用readLine函数从控制台读取一行输入：
```scala
val name = readLine("Your name: ")
```

#### 2.5 循环
Scala拥有与Java和C++相同的while和do循环，如：
```scala
while(n > 0){
	r = r * n
    n -= 1
}
```
for循环使用`for(i <- 表达式)`这样的语法结构，让变量i遍历表达式的所有值，如：
```scala
for(i <- 1 to n)
	r = r * i
```
遍历字符串或数组时，通常需要使用0到n-1的区间，until方法返回一个不包含上限的区间：
```scala
val s = "hello"
var sum = 0
for(i <- 0 until s.length)
	sum += s(i)
```
或：
```scala
var sum = 0
for(ch <- 0 "hello") sum += ch
```

> Scala没有提供break或continue语句来退出循环，我们可以：
> 1.使用Boolean型的控制变量。
> 2.嵌套函数，函数中return。
> 3.使用Breaks对象中的break方法。

#### 2.6 高级for循环
多个生成器：
```scala
for(i <- 1 to 3; j <- 1 to 3) print((10*i+j)+" ")
//打印11 12 13 21 22 23 31 32 33
```
生成器可带守卫（注意：if前无分号）：
```scala
for(i <- 1 to 3; j <- 1 to 3 if i!=j) print((10*i+j)+" ")
//打印12 13 21 23 31 32 
```
for推导式（yield），循环会构造出一个集合，集合与第一个生成器的类型兼容：
```scala
for(i <- 1 to 10) yield i%3
//生成Vector(1,2,0,1,2,0,1,2,0,1)
for(c <- "Hello"; i <- 0 to 1) yield (c+i).toChar
//生成"HIeflmlmop"
for(i <- 0 to 1; c <- "Hel") yield (c+i).toChar
//生成Vector('H','e','l','I','f','m')
```

#### 2.7 函数
定义函数需要名称，参数，函数体：
```scala
def abs(x:Double) = if(x >= 0) x else -x
```
函数可以使用代码块，块中最后一个表达式的值是函数的返回值：
```scala
def fac(n: Int) = {
	var r = 1
    for(i <- 1 to n) r = r *i
    r
}
```
对于递归函数，必须指明返回类型：
```scala
def fac(n:Int): Int = if(n <= 0) 1 else n * fac(n - 1)
```
#### 2.8 过程
过程就是不返回值的函数，返回类型为Unit。定义时可以略去'='，如：
```scala
def box(s:String){
	var border = "-" * s.length + "--\n"
    println(border + "|" + s +"|\n" + border)
}
```
也可以显示声明：
```scala
def box(s:String): Unit = {
	var border = "-" * s.length + "--\n"
    println(border + "|" + s +"|\n" + border)
}
```
---

### 3.数组
#### 3.1 定长数组Array
```scala
val nums = new Array[Int](10)
//10个整数的数组，所有元素初始化为0
val a = new Array[String](10)
//10个元素的字符串数组，所有元素初始化为null
val s = Array("Hello","World")
//已提供初始值时不需要new
s(0) = "Goodbye"
//使用()来访问元素
```
在JVM中，Scala的Array以Java数组实现，比如`Array(2,3,5,7,11)`在JVM中就是一个`Int[]`。

#### 3.2 变长数组ArrayBuffer
对于长度按需变化的数组，Java有ArrayList，C++有vector，Scala中的等效数据结构为ArrayBuffer。
```scala
val b = ArrayBuffer[Int]()
//或val b = new ArrayBuffer[Int]
b += 1
//用+=在尾端添加元素
b += (1,2,3,5)
//添加多个元素
b ++= Array(8,13,21)
//用++=追加任何集合
b.trimEnd(5)
//移除最后5个元素
```
有时需要构建一个Array，但不知道最终要装多少元素，可以先构建一个数组缓冲ArrayBuffer，然后转化为Array：
```scala
b.toArray
```
同时，你可以使用`insert`和`remove`来插入或移除元素。

#### 3.3 遍历数组
使用for循环：
```scala
for (i <- 0 until a.length)
    println(i + ": " + a(i))
```
until是RichInt类的方法，`0 until 10`实际上是`0.until(10)`，如果想让区间是每两个元素一跳，可以这样写`0 until (a.length, 2)`，如果从数组尾端开始，可以这样写`(0 until a.length).reverse`。

如果在循环体中不需要用到数组下标，我们可以直接访问数组元素：
```scala
for(elem <- a)
    println(elem)
```

#### 3.4 数组转换
在Scala，从一个数组或变长数组出发，以某种方式对它进行转换是很简单的，这些转换动作不会修改原始数组，而是产生一个全新的数组。
比如使用for yield推倒式：
```scala
val a = Array(2,3,5,7,11)
val result = for (elem <- a) yield 2 * elem
//result是Array(4,6,10,14,22)
```
当你遍历一个集合，只想处理那些满足特定条件的元素时，你可以加入守卫,比如这里对每个偶数元素翻倍，丢到奇数元素：
```scala
for (elem <- a if elem % 2 == 0) yield 2 * elem
```
另一种做法：
```scala
a.filter(_ % 2 == 0).map(2 * _)
```

#### 3.5 数组常用算法
求最小和最大`min`和`max`
求和（数值类型）：
```scala
Array(1,7,2,9).sum
//19
```
排序`sorted`：
```scala
val b = ArrayBuffer(1,7,2,9)
val bSorted = b.sorted //ArrayBuffer(1,2,7,9)
```
排序（提供比较函数）`sortWwith`：
```scala
val bDescending = b.sortWith(_ > _) //ArrayBuffer(9,7,2,1)
```
显示`mkString`：
```scala
b.mkString(" and ")
//"1 and 7 and 2 and 9"
```
显示`toString`：
```scala
b.toString
//"ArrayBuffer(1,7,2,9)"
```

#### 3.6 多维数组
多维数组是通过数组的数组来实现的，举例来说，`Double`的二维数组类型为`Array[Array[Double]]`，构造时可以用ofDim方法：
```scala
val matrix = Array.ofDim[Double](3,4) //3*4
```
访问元素时使用两对圆括号：
```scala
matrix(row)(column) = 42
```

---
### 参考书籍：
- [快学Scala ](http://book.douban.com/subject/19971952/)





