# 这里介绍几种常见的排序算法

## 1. 冒泡排序

> 相邻元素依次比较, 大的放后面, 一轮比较后最大的元素在最后面; 继续下一轮，比较到第N-1个元素为止; 直到没有元素可比，即完成排序.

> 两层循环, 时间复杂度为O(n^2)

```
public class BubbleSort {
    public static int[] sort(int[] array){
        for(int i = 1 ; i < array.length; i++){
            boolean flag = true;
            for (int j = 0 ; j < array.length-i; j++) {
                if (array[j] > array[j+1]) {
                    array[j] = array[j] ^ array[j+1];
                    array[j+1] = array[j] ^ array[j+1];
                    array[j] = array[j] ^ array[j+1];
                    flag = false;
                }
            }

            if (flag) break;

            System.out.print("第"+i+"轮排序后的结果为:");
            display(array);
        }

        return array;
    }

    //遍历显示数组
    public static void display(int[] array) {
        for (int i = 0 ; i < array.length ; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] array = {4,2,8,9,5,7,6,1,3};

        System.out.println("未排序数组顺序为：");
        display(array);

        System.out.println("-----------------------");
        array = sort(array);
        System.out.println("-----------------------");

        System.out.println("经过冒泡排序后的数组顺序为：");
        display(array);
    }
}
```

## 2. 选择排序

> 每次从一堆待排序数据元素中选出最小的元素, 存放在序列起始位置, 直到全部待排序元素排完.

> 时间复杂度O(n^2)

```
public class ChoiceSort {
    public static int[] sort(int[] array) {
        //总共要经过N-1轮比较
        for (int i = 0 ; i < array.length-1 ; i++) {
            int min = i;

            //每轮需要比较的次数
            for (int j = i+1 ; j < array.length ; j++) {
                if ( array[j] < array[min]) min = j; //当前最小值元素index
            }

            //将找到的最小值和i位置所在的值进行交换
            if (i != min) {
                array[i] = array[i] ^ array[min];
                array[min] = array[i] ^ array[min];
                array[i] = array[i] ^ array[min];
            }

            System.out.print("第"+(i+1)+"轮排序后的结果为:");
            display(array);
        }
        return array;
    }

    //遍历显示数组
    public static void display(int[] array) {
        for (int i = 0 ; i < array.length ; i++) {
            System.out.print(array[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args){
        int[] array = {4,2,8,9,5,7,6,1,3};

        System.out.println("未排序数组顺序为：");
        display(array);

        System.out.println("-----------------------");
        array = sort(array);
        System.out.println("-----------------------");

        System.out.println("经过选择排序后的数组顺序为：");
        display(array);
    }
}
```

## 3. 插入排序

> 每一步将一个待排序的记录, 插入到前面已经排好的有序序列中, 直到插完所有元素.

> 

```
public class InsertSort {
    public static int[] sort(int[] array) {
        int j;
        for (int i = 1 ; i < array.length ; i++) {
            int tmp = array[i]; //记录要插入的数据
            j = i;
            while (j > 0 && tmp < array[j-1]) {//从已经排序的序列最右边的开始比较，找到比其小的数
                array[j] = array[j-1];//向后挪动
                j--;
            }
            array[j] = tmp; //存在比其小的数，插入

            System.out.print("第"+(i+1)+"轮排序后的结果为:");
            display(array);
        }
        return array;
    }

    //遍历显示数组
    public static void display(int[] array) {
        for (int i = 0 ; i < array.length ; i++) {
            System.out.print(array[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args){
        int[] array = {4,2,8,9,5,7,6,1,3};

        System.out.println("未排序数组顺序为：");
        display(array);

        System.out.println("-----------------------");
        array = sort(array);
        System.out.println("-----------------------");

        System.out.println("经过插入排序后的数组顺序为：");
        display(array);
    }
}
```

> 总结：三种排序方式, 冒泡排序平均性能不如后两种

> 选择排序把交换次数降低到最低, 但是比较次数还是挺大的. 当数据量小, 并且交换数据相对于比较数据更加耗时的情况下, 可以应用选择排序.

> 在大多数情况下, 假设数据量比较小或基本有序时, 插入排序是三种算法中最好的选择
