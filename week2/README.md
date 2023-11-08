# Introduction to Data Science and Engineering Week 2

## Author: Chenxu Han@ArcueidType
## Student ID: 10225101440

## Week 2 practices:

### Practice 1:

`(1): `[3, 3, $\cdots$ , 3] 共667个3

`(2): `通过观察，发现：

`1, 2, 3`最大对应最大为自身`1, 2, 3`

`4`最大不论是`2*2`还是`4`本身，结果都是`4`

而从`5`开始，`5 = 2+3`且`2*3 = 6 > 5`

所以我们应该尽量考虑分解为更多的`2`或`3`或`4`，那么这三个数究竟选哪个数最好呢？

一个不严谨的证明：

`3和4`: 假设一个数可以表示为$c * 3^p * 4^q$，我们尝试将`3`减少以获得更多`4`，得到$c * 3^p$ $^-$ $^4$ $* 4^q$ $^+$ $^3$，后者与前者比值为$\frac{64}{81} < 1$，故更多的4会使数变小

同理，`2和3`中，更多的2会导致数字变小，因此我们可以发现，当剩余的数字大于`4`时，我们从其中分割出尽可能多的`3`，当 **$剩余数字 \leq 4$** 时，停止分割，保留这个数字

`(3): `如图

![prac1 code](/week2/img/prac1code.png)

![prac1](/week2/img/prac1.png)

### Practice 2: 

![prac2](/week2/img/prac2.png)

如图，增长速度很快(指数爆炸)，指数每增加`10`会提高`3个数量级`

### Practice 3:

![prac3](/week2/img/prac3.png)

采用了邻接表表示图，采用`dfs(深度优先搜索)`算法探索所有可能路径，最后得出了上图结果

### Practice 4:

![prac4](/week2/img/prac4.png)

* 精确度为`1e-4`的结果

### Practice 5:

![prac5-1](/week2/img/prac5-1.png)

![prac5-2](/week2/img/prac5-2.png)

![prac5-3](/week2/img/prac5-3.png)

![prac5-4](/week2/img/prac5-4.png)

### Practice 6:

* $g = c$ : 

![prac6-1](/week2/img/prac6-1.png)

![prac6-2](/week2/img/prac6-2.png)

* $g = \frac{c}{4}$ :

![prac6-3](/week2/img/prac6-3.png)

容易发现，初始的`g`的取值对循环的次数是有一些影响的

### Practice 7:

![prac7](/week2/img/prac7.png)

* 精确度`1e-11`

### Practice 8:

* Monte Carlo方法

![prac8-1](/week2/img/prac8-1.png)

* $\arctan x$的泰勒展开: 

![prac8-2](/week2/img/prac8-2.png)

* 由`会田安明`发现的一个无穷级数: 

### $$\displaystyle \sum^{\infty}_{k = 0} \frac{k!}{\displaystyle \prod^{k}_{i=0}2i+1} = \frac{\pi}{2} $$ 

![prac8-3](/week2/img/prac8-3.png)

* 三种方法的准确度越来越高，尤其是最后一个级数，仅`10000`项和精度就至少达到了10位小数

# Practice 9:

取区间$[2, 3] \times [0, 21]$，用Monte Carlo法进行估计：

![prac9](/week2/img/prac9.png)

* 可以发现，在数据量为`10,000,000`时，估计的结果和数学方法直接计算的结果的误差已经非常小了