//
// 对于一个字节的无符号整型变量，求其二进制表示中1的个数
//
// Application:
// 1. 图片相似度检测
// 2. 文字匹配: Hamming Distance

#include <iostream>
#include <bitset>
using namespace std;

//方法1:逐个数,声明一个计数变量,当尾数为1时加1,然后/2(右移),直到该数为0为止
int Method01(int n)
{
  int count(0); //声明计数变量
  while (n != 0)
  {
    count += n & 1;
    n >>= 1;  //右移
  }
  return count;
}

//方法2: n与n-1相与的最低位永远是0, 只考虑1的位数,当n中大多数据位是0时,采用该方法最好
//引申：判断一个数是否为2的幂次方, n > 0 && ((n & (n-1)) == 0
int Method02(int n)
{
  int count(0);
  while (n != 0)
  {
    n &= n - 1;
    ++count;
  }
  return count;
}

//方法3,Hamming Weight:使用分治的思想,先计算每对相邻的2位中有几个1,再计算每相邻的4位中有几个1,
//然后8位,16位,32位
int Method03_HammingWeight(int n)
{
  n = (n & 0x55555555) + ((n >> 1) & 0x55555555);
  n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
  n = (n & 0x0F0F0F0F) + ((n >> 4) & 0x0F0F0F0F);
  n = (n & 0x00FF00FF) + ((n >> 8) & 0x00FF00FF);
  n = (n & 0x0000FFFF) + ((n >> 16) & 0x0000FFFF);
  return n;
}


int main()
{
  int n(0);
  cout << "Please Input the number:";
  cin >> n;
  bitset<32> myBit(n);
  cout << "Number " << n << " = " << myBit << endl;
  cout << "Count of 1 in Binary Format: " << myBit.count() << endl;

  cout << "Method 01: " << Method01(n) << endl;
  cout << "Method 02: " << Method02(n) << endl;
  cout << "Method 03, Hamming Weight: " << Method03_HammingWeight(n) << endl;
  return 0;
}
