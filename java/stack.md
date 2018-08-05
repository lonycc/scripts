# 这里介绍栈(stack)结构

栈是一种只能在一端进行push/pop操作的特殊线性表, 具有LIFO(后进先出)的特性, 栈顶浮动, 栈底固定.

栈的特性常用于逆序输出, 判断分隔符是否匹配等. 数据入栈和出栈的时间复杂度都为O(1).

```
import java.util.Stack;
import java.util.EmptyStackException;

public class StackDemo {
    static void showpush(Stack<Object> st, Object a) {
        st.push(a);
        System.out.println("push(" + a + ")");
        System.out.println("stack: " + st);
    }

    static void showpop(Stack<Object> st) {
        System.out.print("pop -> ");
        Object a = (Object) st.pop();
        System.out.println(a);
        System.out.println("stack: " + st);
    }

    public static void main(String args[]) {
        Stack<Object> st = new Stack<Object>();
        System.out.println("stack: " + st);
        showpush(st, 12);
        showpush(st, "funny");
        showpush(st, 99);
        showpush(st, "c");

        System.out.println("stack peek:" + st.peek());

        showpop(st);
        showpop(st);

        Boolean isEmpty = st.empty();
        System.out.println("stack is empty? " + isEmpty);

        int index = st.search("funny");
        System.out.println("index of funny in stack is " + index);

        showpop(st);

        try {
            showpop(st);
            showpop(st);
        } catch (EmptyStackException e) {
            System.out.println("empty stack");
        }
    }

}
```
