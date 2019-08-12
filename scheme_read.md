## scheme 的一种实现 guile （gnu's extension language)

**基本概念**

```
单行注释用;

多行注释

#！
aa
bb
!#


form（块), scheme程序最小单元, ()包围

(define x 123) ; 变量定义
(set! x "hello")  ; 变量修改
(+ 1 2)  ; 加法运算, 波兰式, 前缀表达式
(* 4 5 6) ; 乘法运算
(display "hello world")  ; 过程
```

**数据类型**

```
逻辑型(boolean)
#f #t 分别代表false和true

数字型(number), 包括 整型(integer)，有理数型(rational)，实型(real)，复数型(complex)
(define c 3+2i)  ; 复数
(define d 22/7)  ; 实数
(define e 10)    ; 整数
(define f 3.1414)  ; 有理数

 #b1010 ; 二进制
 #o56   ; 八进制
 #d98   ; 十进制, 前缀#d可省略
 #x1afc ; 十六进制
 
 字符型(char)
 字符型数据均以符号组合 "#\" 开始，表示单个字符，只接受Ascii字符
 #\A 字符A
 #\0 字符0
 #\space 空格符
 #\newline 换行符
 
 符号型(symbol), 可以是单个字符或括号里的多个字符
 define a (quote xyz)) ; 定义变量a为符号类型, 值为xyz
 define xyz 'a   ; 定义变量xyz为符号类型，值为a
 单引号和'等价
 
 
字符串(string)
(define name "tomson")
(string-length name)  ; 取字符串的长度
(string-set! name 0 #\g)  ; 更改字符串首字母(第0个字符)为小写字母g (#\g)
(string-ref name 3)  ; 取得字符串左侧第3个字符（从0开始）
(define other (string #\h #\e #\l #\l #\o ))  ; 同 (define other "hello")


点对(pair)
(define p (cons 4 5)) ; (4 . 5)
(car p)  ; 4
(cdr p)  ; 5
(set-car! p "hello")
(set-cdr! p "good")


列表(list)
(define la (list 1 2 3 4 ))
(length la)   ; 列表长度, 4
(list-ref la 2)  ; 索引为2的项, 3
(list-set! la 2 99)  ; 索引为2的项的值设为99
(define y (make-list 5 6))  ; 创建列表y, 5个6组成


list是pair的子类型
(define a (cons 1 (cons 2 (cons 3 '()))))   ; a (1 2 3), '()是特殊值, 等同null
(define ls (list 1 2 3 4))
(list? ls)   ; #t
(pair? ls)   ; #t
(car ls) ; 1
(cdr ls) ; (2 3 4)
(cadr ls) ; ls的cdr的car, 2
(cddr ls)  ; ls的cdr的cdr, (3 4)
(caddr ls)  ; ls的cdr的cdr的car, 3
(cddddr ls)  ; ls的cdr的cdr的cdr, 4
最多支持c[\a\d]{4}r, 也就是中间最多四个


向量(vector)
(define v (vector 3 4 5)) 
(define v #(3 4 5))
(vector-ref v 0)  ; 求第1个变量的值, 3
vector-length v)  ; 求vector的长度, 3
(vector-set! v 2 "abc")  ; 设定vector第3个元素的值
(define x (make-vector 5 6))  ; 创建向量表, #(6 6 6 6 6)


类型判断  (类型? 变量)
(boolean? 0)  ; #f
(char? #\space)  ; #t
(number? 22/7)  ; #t
(rational? 22/7) ; #t
(null? '())  ; #t
(symbol? 'x)  ; #t

(define x 5)
(symbol? x)   ; #f

比较运算
(eqv? 34 34)  ; 比较值, #t
(define x 0)
(= x 0)  ; #t
(>= x 0) ; #t

(define v (vector 3 4 5))
(define w #(3 4 5))
(eq? v w)   ; #f, 此时v和w是两个对象, eq比较两个参数是否指向同一个对象
(eqv? v w)  ; #f, 同eq
(equal? v w) ; #t, equal比较两个对象的结构和内容
(equal? v w)  ; #t, 比较两个对象的值


算术运算
(- 4)  ; -4
(/ 4)  ; 1/4
(max 1 0 5 3)  ; 求最大
(min 1 0 5 3)  ; 求最小
(abs -7)  ; 绝对值
此外还支持很多数学公式, 如三角函数sin/cos, 


类型转换
(number->string 123)  ; 数字转换为字符串
(string->number "456")  ; 字符串转换为数字
(char->integer #\a)   ; 字符转换为整型数，小写字母a的ASCII码值为96
(char->integer #\A)  ; 大写字母A的值为65
(integer->char 97)  ; 整型数转换为字符, #\b
(string->list "hello")   ; 字符串转换为列表, (#\h #\e #\l #\l #\o)
(list->string (make-list 4 #\a)) ; 列表转换为字符串, "aaaa"
(string->symbol "good")  ; 字符串转换为符号类型, good
(symbol->string 'better)  ; 符号类型转换为字符串, "better"
```

**过程**

> scheme 中, 过程(procedure)是一种数据类型. `(define 过程名 ( lambda (参数 ...) (操作过程 ...)))` 或者 `(define (过程名 参数) (过程内容 …))`

```
(procedure? +)  ; #t, 运算符就是一种过程

(define add5 (lambda (x) (+ x 5)))   ; 定义了一个过程, 给输入的整数+5
(add5 11)  ; 16

define square (lambda (x)  (* x x)))

(define (add6 x) (+ x 6))  ; 省略lambda
(add6 10)

(define fun
    (lambda(proc x y)
        (proc x y)))
fun(* 5 6)  ; 30

(define add
    (lambda (x y)
        (+ x y)))
fun(add 100 200)  ; 300, 同fun(+ 100 200)

((lambda (x) (+ x x)) 5)  ; 匿名过程, 10

过程嵌套定义
(define fix 
    (lambda (x y z)
        (define add 
            (lambda (a b) (+ a b)))
        (- x (add y z))))
(display (fix 100 20 30))  ; 50
```
