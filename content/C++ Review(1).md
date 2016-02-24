Title: C++ Review(1)
Date: 2016-02-19 12:20
Category: Blogs
Tags: C/C++, basic
Author: Tom Gou
Summary: 决定开始写博客了，留下一些记录，开始一个新起点。最近复习了一些C++的语法，虽然很简单，但就用它开始第一篇博客吧。


###1.数据类型

<br />

|type    	 | byte 		|bit	 |有效数字&nbsp;&nbsp;&nbsp;|
|------------|--------------|----------------------|-------|
|int    	 |    4bytes    |32bits(-2^31 ~ 2^31-1)||
|short     	 |    2bytes    |16bits				   |
|long    	 |    4bytes    |32bits 			   |
|unsigned    |    4bytes    |32bits(0～2^32-1)	  |
|bool    	 |    1byte    	|||
|char    	 |    1byte    	|||
|float   	 |    4bytes    |32bits(-2^128 ~ 2^128)|6~7|
|double   	 | 8bytes|64bits(-2^1024 ~ 2^1024)&nbsp;&nbsp;&nbsp;|15~16|
|long double&nbsp;&nbsp;&nbsp;|16bytes &nbsp;&nbsp;&nbsp;| |18~19|

<br />

注意：

- long int 和 int在16位以上机器相同，均为32位，16位机器int为16位
- bool值有两种true和false，字节值为1或0
- char一个字节，字节中存放的是对应字符的ASCII值，如`'A'`
- 实型数（浮点型）在计算机内不能精确表示。
- 其中float4字节，32位，符号位1位，指数位8位，于是float的指数范围为-127~128。float尾数部分23位，2^23 = 8388608，一共七位，这意味着float最多能有7位有效数字，但绝对能保证的为6位。

可以通过`sizeof()`了解不同类型占用多少内存量（字节）：

```c++
#include <iostream>
int main()
{
    std::cout<<sizeof(float)<<std::endl;
    std::cout<<sizeof(double)<<std::endl;
    std::cout<<sizeof(long double)<<std::endl;
    return 0;
}
```

执行结果：

```
4
8
16
```


- 123e3,123E3(科学计数法 123*10^3 )
- 一维数组 `int a[10];`
- 二维数组 `int a[4][5];//4*5`
- 字符串
`char ch[] = "Hello,world";`或
`char ch[] = {"Hello,world"};`或
`char ch[] = {'H','e','l','l','o',',','w','o','r','l','d','\0'};`

	- ==**以`'\0'`为结束符**==
	- `'a'`与`"a"`：`'a'`为字符常量，一字节（a的ASCII值）；`"a"`为字符串，2字节（a的ASCII值和'\0'）
	- 字符串处理函数
`#include<cstring>` `strcpy(dst, src)` `strlen(s)` `strchr(s, ch)` `strcmp(s1, s2)`

- enum枚举
`enum weekdayT{SUnday, Monday};`

<br />
- - -

###2.基础知识
- 位，比特，bit(二进制的一位)
- 字节，byte，B（8个位组成一个字节）
- 注释

```c++
//一行的注释
```

```c++
/*多行
的注释
*/
```

- 库包含

```c++
#include<iostream>
#include"user.h"	//自己写的库user
```

- 宏定义

```c++
#define PI 3.14159
```

- 转义
`'\n'`换行	`'\t'`Tab	`'\\'`反斜杠

- 内存量`sizeof()`

- 符号常量

```c++
const double PI = 3.1415926
```

- 数学函数库

```c++
#include<cmath>
int abs(int x);
double fabs(double x);
double exp(double x);
double sqrt(double x);
```

- 自增自减运算

```c++
y = x++;	//先 y = x，再x++
y = ++x;
```

- 输入输出

```c++
cin >> a;
cin.get();
cin.getline(ch1, 80, '.');	//字符串输入（,数组长度,结束标记）
cout << a <<endl;
```

- 主程序

```c++
//#include <iostream>
using namespace std;	//名字空间

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
```

- 条件句
`<`小于 `<=`小于等于 `==`==**等于**== `!=`不等于

- 逻辑运算
`&&`与 `||`或 `!`非

<br />
- - -

###3.控制流
- if语句

```c++
if(  ) XXX;
else{	XXX;
		XXX;
}
```

- 条件表达式?:

```c++
max = (x > y)?x:y;
```

- switch语句

```c++
switch(){
	case const1: XXX;break;
    case const2: XXX;break;
    default:	 XXX;break;
}
```

- for循环

```c++
for(i = 0; i < n; ++i){
	XXX;
}
```

- while循环

```c++
while( ){
	XXX;
}
```

- do-while循环

```c++
do{
	XXX;
} while( );
```

- 循环中途退出

```c++
while( ){
	XXX;
    if ( ) break;
}
```

- 随机数

```c++
#include<cstdlib>
#include<ctime>
	srand(time(NULL));	//随机种子初始化
    num1 = rand() * 10/(RAND_MAX + 1);
    num2 = rand() * 4/(RAND_MAX + 1);
```
