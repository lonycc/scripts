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
; 逻辑型(boolean)
#f #t 分别代表false和true

; 数字型(number), 包括 整型(integer)，有理数型(rational)，实型(real)，复数型(complex)
(define c 3+2i)  ; 复数
(define d 22/7)  ; 实数
(define e 10)    ; 整数
(define f 3.1414)  ; 有理数

 #b1010 ; 二进制
 #o56   ; 八进制
 #d98   ; 十进制, 前缀#d可省略
 #x1afc ; 十六进制
 
 ; 字符型(char)
 字符型数据均以符号组合 "#\" 开始，表示单个字符，只接受Ascii字符
 #\A 字符A
 #\0 字符0
 #\space 空格符
 #\newline 换行符
 
 符号型(symbol), 可以是单个字符或括号里的多个字符
 define a (quote xyz)) ; 定义变量a为符号类型, 值为xyz
 define xyz 'a   ; 定义变量xyz为符号类型，值为a
 单引号和'等价
 
 
; 字符串(string)
(define name "tomson")
(string-length name)  ; 取字符串的长度
(string-set! name 0 #\g)  ; 更改字符串首字母(第0个字符)为小写字母g (#\g)
(string-ref name 3)  ; 取得字符串左侧第3个字符（从0开始）
(define other (string #\h #\e #\l #\l #\o ))  ; 同 (define other "hello")
(string-append "aa" "bb" "cc")    ; 字符串连接, "aabbcc"


; 点对(pair)
(define p (cons 4 5)) ; (4 . 5)
(define w '(1 2 3 4)) ;
(car p)  ; 4
(cdr p)  ; 5
(set-car! p "hello")
(set-cdr! p "good")



; 列表(list)
(define la (list 1 2 3 4 ))
(length la)   ; 列表长度, 4
(list-ref la 2)  ; 索引为2的项, 3
(list-set! la 2 99)  ; 索引为2的项的值设为99
(define y (make-list 5 6))  ; 创建列表y, 5个6组成


; list是pair的子类型
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
; 最多支持c[\a\d]{4}r, 也就是中间最多四个


; 向量(vector)
(define v (vector 3 4 5)) 
(define v #(3 4 5))
(vector-ref v 0)  ; 求第1个变量的值, 3
vector-length v)  ; 求vector的长度, 3
(vector-set! v 2 "abc")  ; 设定vector第3个元素的值
(define x (make-vector 5 6))  ; 创建向量表, #(6 6 6 6 6)


; 类型判断  (类型? 变量)
(boolean? 0)  ; #f
(char? #\space)  ; #t
(number? 22/7)  ; #t
(rational? 22/7) ; #t
(null? '())  ; #t
(symbol? 'x)  ; #t

(odd? 5) ; 是否为基数
(even? 10)  ; 是否为偶数
(positive? 1) ; 是否正数
(negative? -1)  ; 是否负数
(zero? 0)  ; 是否0
(string=? "aa" "bb" "cc")  ; 字符串是否相等
(string-ci=? "aa" "aa" "aa")  
(char=? #\a #\b)
(char<? #\a #\b)
(char>? #\a #\b)
(char<=? #\a #\b #\c)
(char>=? #\a #\b #\c)

(define x 5)
(symbol? x)   ; #f

; 比较运算
(eqv? 34 34)  ; 比较值, #t
(define x 0)
(= x 0)  ; #t
(>= x 0) ; #t

(define v (vector 3 4 5))
(define w #(3 4 5))
(eq? v w)   ; #f, 此时v和w是两个对象, eq比较两个参数是否指向同一个对象
(eqv? v w)  ; #f, 同eq
(equal? v w) ; #t, equal比较两个对象的结构和内容


; 算术运算
(- 4)  ; -4
(/ 4)  ; 1/4
(max 1 0 5 3)  ; 求最大
(min 1 0 5 3)  ; 求最小
(abs -7)  ; 绝对值
(quotient 5 2)  ; 除法, 求商(整数部分), 2
(modulo 5 2)   ; 除法, 求余, 1
(remainder 5 2)  ; 求余, 1
(sqrt 8)  ; 平方根
(log 1000) ; 对数
(expt 2 5) ; 幂次 32
(exp 2) ; 指数, 自然常数e为底
此外还支持很多数学公式, 如三角函数sin/cos/asin/atan/acos, atan接受1或2个参数,


; 类型转换
(number->string 123)  ; 数字转换为字符串
(string->number "456")  ; 字符串转换为数字
(char->integer #\a)   ; 字符转换为整型数，小写字母a的ASCII码值为96
(char->integer #\A)  ; 大写字母A的值为65
(integer->char 97)  ; 整型数转换为字符, #\b
(string->list "hello")   ; 字符串转换为列表, (#\h #\e #\l #\l #\o)
(list->string (make-list 4 #\a)) ; 列表转换为字符串, "aaaa"
(string->symbol "good")  ; 字符串转换为符号类型, good
(symbol->string 'better)  ; 符号类型转换为字符串, "better"
(exact->inexact (/ 29 3 7))  ; 分数转浮点数
```

**过程**

> scheme 中, 过程(procedure)是一种数据类型. `(define 过程名 ( lambda (参数 ...) (操作过程 ...)))` 或者 `(define (过程名 参数) (过程内容 …))`

```
(procedure? +)  ; #t, 运算符就是一种过程

(define add5 (lambda (x) (+ x 5)))   ; 定义了一个过程, 给输入的整数+5
(add5 11)  ; 16

(define square (lambda (x)  (* x x)))

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

; 过程嵌套定义
(define fix 
    (lambda (x y z)
        (define add 
            (lambda (a b) (+ a b)))
        (- x (add y z))))
(display (fix 100 20 30))  ; 50
```

**常用结构**

```
; 顺序结构
(begin 
    (display "Hello world!")  ; 输出"Hello world!"
    (newline))              ; 换行


; if结构
(if (= x 0) 
    (display "is zero")
    (display "not zero"))

(if (< x 100) (display "lower than 100"))   ; 条件成立则执行


; cond结构, 类似C语言switch结构
(define w (lambda (x)
      (cond ((< x 0) 'lower)
           ((> x 0) 'upper)
           (else 'equal))))


; case结构, 结构中的值可以是复合类型数据，如列表，向量表等
(case (* 2 3)
    ((2 3 5 7) 'prime)
    ((1 4 6 8 9) 'composite))
    (else 'none)


; and结构
(and (boolean? #f) (string? 'a))  ; #f
(and (list 1 2 3) (vector 'a 'b 'c))  ; #(a b c), 表达式的值都不是boolean, 返回最后一个表达式的值
(and 1 2 3 4 )   ; 4
(and 'e 'd 'c 'b 'a)  ; 'a


; or结构, 返回第一个不为#f的值
(or #f #t)  ; #t
(or #f 0)   ; 0
(or 1 2 3)  ; 1
(or #f 1 2 3)  ; 1
```

**递归**

```
(define  factoral (lambda (x)
    (if (<= x 1) 1
        (* x (factoral (- x 1))))))


(define (factoral n)
    (define (iter product counter)
        (if (> counter n)
            product
            (iter (* counter product) (+ counter 1))))
    (iter 1 1))
(display (factoral 4))


; 递归实现循环
(define loop
    (lambda(x y)
        (if (<= x y)
            (begin (display x) (display #\\space) (set! x (+ x 1))
                (loop x y)))))
(loop 1 10)
```

**变量和过程的绑定**

```
(let ((p1 v1) (p2 v2) ...) exp1 exp2 ...) ; 变量作用域在exp中, 其实就是lambda的语法糖

((lambda (p1 p2 ...) exp1 exp2 ...) v1 v2)

(let ((x 2) (y 5)) (* x y)) ; let将变量或过程绑定在过程内部, 即局部变量, 10, x y仅在(* x y)中有效

(let ((x 5))
    (define foo (lambda (y) (bar x y)))
    (define bar (lambda (a b) (+ (* a b) a)))
    (foo (+ x 3)))  ; 过程是先(foo 8), 展开后(bar 5 8), 再展开(+ (* 5 8) 5), 得到45

; let*表达式可以用于引用定义在同一个绑定中的变量
(let ((x 2) (y 5))
    (let* ((x 6)(z (+ x y)))  ; 此时x的值已为6，所以z的值应为11，如此最后的值为66
    (* z x)))

; letrec将内部定义的过程/变量进行相互引用
(letrec ((countdown
            (lambda (i)
                (if (= i 0) 'listoff
                    (begin (display i) (display ",")
                        (countdown (- i 1)))))))
        (countdown 10))


; apply, 为数据赋予某一操作过程, 参数1是过程, 参数2是列表
(apply + (list 1 2 3 4)  ; 给列表赋予相加操作, 10

 (define sum
    (lambda (x )
        (apply + x)))
(sum list(1 2 3 4))  ; 10

(define avg
    (lambda(x)
        (/ (sum x) (length x))))
(avg list(1 2 3))  ; 2

; map, 为多个列表赋予操作过程
(map + (list 1 2 3) (list 4 5 6))    ; (5 7 9)
(map car '((a . b)(c . d)(e . f)))   ; (a c e)
```

**输入输出**

> 基于C语言的封装

```
(current-input-port)  ; 当前输入端口
(current-output-port)  ; 当前输出端口
(input-port? in)     ; 判断是否输入端口
(output-port? out)   ; 判断是否输出端口

(open-input-file  "/path/to/file")
(open-output-file "/path/to/file")
(close-input-port input_port)
(close-output-port output_port)

(define port (open-input-file "readme"))
(read port)  ; 读取内容
(close-input-port port)   ; 关闭

(read)  ; 执行后即等待键盘输入
(define x (read))  ; 等待键盘输入并赋值给x


(read-char)  ; 接受单个字符
(load "source.scm")  ; 调用源文件执行


(define port1 (open-output-file "temp"))  ; 打开文件端口赋于port1
(write "hi\\n,what's up" port1)  ; 写入内容
(close-output-port port1)
```

**语法扩展**

> scheme允许扩展如cond/let等的宏关键字

```
(define-syntax 宏名
    (syntax-rules()
        ((模板) 操作))
        . . . ))

; 自定义一个start宏, 功能同begin
(define-syntax start
        (syntax-rules ()
                ((start exp1)
                        exp1)
                ((start exp1 exp2 ...)
                        (let ((temp exp1)) (start exp2 ...))) ))
(start (display "hello") (newline))



(use-modules (ice-9 popen))  ; 引用ice-9模块, popen过程
(use-modules (ice-9 pretty-print))    ; 引用漂亮输出模块
(pretty-print '(define fix (lambda (n)
        (cond ((= n 0) 'iszero)
                ((< n 0) 'lower)
                (else 'upper)))))   ; 代码格式混乱

; 格式化后的输出
(define fix
  (lambda (n)
    (cond ((= n 0) 'iszero)
          ((< n 0) 'lower)
          (else 'upper))))


; 命令行参数
#! /usr/local/bin/guile -s
!#
(define cmm (command-line))
(display "应用程序名称：")
(display (car cmm))  
(newline)
(define args (cdr cmm))
(define long (length args))
(define loop (lambda (count len obj)
    (if (<= count len)
        (begin
            (display "参数 ")
            (display count)
            (display " 是：")
            (display (list-ref obj (- count 1)))
            (newline)
            (set! count (+ count 1))
            (loop count len obj)))))
(loop 1 long args)

; 执行方法  ./t.scm abc 123
```
