## 相关介绍
这是一个简易的LeetCode自动统计程序, 可自动统计最近提交通过的题目, 并以Markdown的形式展示相关的数据。
根据个人需求, 我只重点获取**提交次数**和**重刷次数**这两个指标, 目的是为了更好地辅助做题。
## 使用教程
1. Fork本仓库
2. 配置GitHub Actions所需的参数
    - 点击仓库下的Settings->Secrets->New repository secret, 分别添加以下secret
        - Name:LEETCODE_EMAIL  Value:你的LeetCode账号
        - Name:LEETCODE_PASSWORD  Value:你的LeetCode密码
    - 点击[tokens](https://github.com/settings/tokens)->Generate new token
        - Note:GITHUB_TOKEN
        - Select scopes:建议全部勾选
    - 修改[action.yml](.github/workflows/action.yml)文件的第`42行`, 将`email`更改为你的GitHub邮箱地址
    - 修改[action.yml](.github/workflows/action.yml)文件的第`43行`, 将`name`更改为你的GitHub用户名
3. 默认配置为12小时更新一次，可根据需求修改[action.yml](.github/workflows/action.yml)文件的第`6行`
## 补充说明
如有其他需求, 欢迎提交PR。


> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

> 总提交次数: 1315, 总通过次数: 786, 已通过题数: 526

> 已通过题目的难度和数量: EASY = 426, MEDIUM = 87, HARD = 13, 

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2021-06-27 15:13 | [#495 提莫攻击](https://leetcode-cn.com/problems/teemo-attacking) | EASY | 1 | 1 |
| 2021-06-25 07:24 | [#219 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii) | EASY | 1 | 1 |
| 2021-06-25 07:18 | [#653 两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst) | EASY | 1 | 1 |
| 2021-06-25 06:51 | [#1154 一年中的第几天](https://leetcode-cn.com/problems/day-of-the-year) | EASY | 1 | 1 |
| 2021-06-25 06:45 | [#1175 质数排列](https://leetcode-cn.com/problems/prime-arrangements) | EASY | 1 | 1 |
| 2021-06-24 08:59 | [#628 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | EASY | 1 | 1 |
| 2021-06-24 08:57 | [#1317 将整数转换为两个无零整数的和](https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers) | EASY | 1 | 1 |
| 2021-06-24 08:41 | [#989 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer) | EASY | 3 | 1 |
| 2021-06-24 06:41 | [#1893 检查是否区域内所有整数都被覆盖](https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered) | EASY | 4 | 1 |
| 2021-06-24 06:21 | [#1897 重新分配字符使所有字符串都相等](https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal) | EASY | 1 | 1 |
| 2021-06-24 02:57 | [#917 仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters) | EASY | 1 | 1 |
| 2021-06-24 02:46 | [#1784 检查二进制字符串字段](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones) | EASY | 2 | 1 |
| 2021-06-24 02:40 | [#1796 字符串中第二大的数字](https://leetcode-cn.com/problems/second-largest-digit-in-a-string) | EASY | 1 | 1 |
| 2021-06-24 02:30 | [#1903 字符串中的最大奇数](https://leetcode-cn.com/problems/largest-odd-number-in-string) | EASY | 1 | 1 |
| 2021-06-24 02:19 | [#121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 3 | 1 |
| 2021-06-24 02:06 | [#551 学生出勤记录 I](https://leetcode-cn.com/problems/student-attendance-record-i) | EASY | 1 | 1 |
| 2021-06-24 01:58 | [#506 相对名次](https://leetcode-cn.com/problems/relative-ranks) | EASY | 1 | 1 |
| 2021-06-23 10:32 | [#520 检测大写字母](https://leetcode-cn.com/problems/detect-capital) | EASY | 1 | 1 |
| 2021-06-23 10:16 | [#705 设计哈希集合](https://leetcode-cn.com/problems/design-hashset) | EASY | 1 | 1 |
| 2021-06-23 09:59 | [#706 设计哈希映射](https://leetcode-cn.com/problems/design-hashmap) | EASY | 1 | 1 |
| 2021-06-23 07:34 | [#LCP 11 期望个数统计](https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji) | EASY | 2 | 1 |
| 2021-06-23 07:23 | [#733 图像渲染](https://leetcode-cn.com/problems/flood-fill) | EASY | 1 | 1 |
| 2021-06-23 07:23 | [#面试题 08.10 颜色填充](https://leetcode-cn.com/problems/color-fill-lcci) | EASY | 1 | 1 |
| 2021-06-23 07:03 | [#面试题 01.09 字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci) | EASY | 1 | 1 |
| 2021-06-23 06:51 | [#面试题 16.15 珠玑妙算](https://leetcode-cn.com/problems/master-mind-lcci) | EASY | 3 | 1 |
| 2021-06-23 06:37 | [#面试题 10.05 稀疏数组搜索](https://leetcode-cn.com/problems/sparse-array-search-lcci) | EASY | 1 | 1 |
| 2021-06-23 03:45 | [#剑指 Offer 29 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof) | EASY | 1 | 1 |
| 2021-06-23 03:22 | [#剑指 Offer 40 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 1 | 1 |
| 2021-06-23 03:22 | [#34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | MEDIUM | 6 | 1 |
| 2021-06-23 03:01 | [#剑指 Offer 53 - I 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | EASY | 6 | 1 |
| 2021-06-23 02:32 | [#剑指 Offer 11 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 1 | 1 |
| 2021-06-23 02:26 | [#面试题 03.01 三合一](https://leetcode-cn.com/problems/three-in-one-lcci) | EASY | 1 | 1 |
| 2021-06-23 02:08 | [#1523 在区间范围内统计奇数数目](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range) | EASY | 1 | 1 |
| 2021-06-23 02:01 | [#剑指 Offer 15 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | EASY | 2 | **2** |
| 2021-06-23 01:57 | [#1446 连续字符](https://leetcode-cn.com/problems/consecutive-characters) | EASY | 1 | 1 |
| 2021-06-22 10:08 | [#1417 重新格式化字符串](https://leetcode-cn.com/problems/reformat-the-string) | EASY | 1 | 1 |
| 2021-06-22 09:46 | [#1422 分割字符串的最大得分](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string) | EASY | 1 | 1 |
| 2021-06-22 09:32 | [#1360 日期之间隔几天](https://leetcode-cn.com/problems/number-of-days-between-two-dates) | EASY | 1 | 1 |
| 2021-06-22 09:16 | [#剑指 Offer 10- II 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof) | EASY | 5 | 1 |
| 2021-06-22 09:09 | [#面试题 17.12 BiNode](https://leetcode-cn.com/problems/binode-lcci) | EASY | 1 | 1 |
| 2021-06-22 07:39 | [#面试题 10.01 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci) | EASY | 1 | 1 |
| 2021-06-22 06:48 | [#剑指 Offer 38 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof) | MEDIUM | 1 | 1 |
| 2021-06-22 06:46 | [#面试题 04.04 检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci) | EASY | 2 | 1 |
| 2021-06-22 06:36 | [#面试题 01.06 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | EASY | 5 | 1 |
| 2021-06-22 03:46 | [#面试题 01.04 回文排列](https://leetcode-cn.com/problems/palindrome-permutation-lcci) | EASY | 2 | 1 |
| 2021-06-22 03:33 | [#LCS 01 下载插件](https://leetcode-cn.com/problems/Ju9Xwi) | EASY | 5 | 1 |
| 2021-06-21 09:54 | [#704 二分查找](https://leetcode-cn.com/problems/binary-search) | EASY | 4 | 1 |
| 2021-06-21 09:14 | [#925 长按键入](https://leetcode-cn.com/problems/long-pressed-name) | EASY | 4 | 1 |
| 2021-06-21 08:32 | [#面试题 05.03 翻转数位](https://leetcode-cn.com/problems/reverse-bits-lcci) | EASY | 1 | 1 |
| 2021-06-21 08:22 | [#1013 将数组分成和相等的三个部分](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum) | EASY | 1 | 1 |
| 2021-06-21 08:08 | [#680 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii) | EASY | 1 | 1 |
| 2021-06-21 06:30 | [#507 完美数](https://leetcode-cn.com/problems/perfect-number) | EASY | 2 | 1 |
| 2021-06-21 03:34 | [#1033 移动石子直到连续](https://leetcode-cn.com/problems/moving-stones-until-consecutive) | EASY | 3 | 1 |
| 2021-06-21 02:33 | [#434 字符串中的单词数](https://leetcode-cn.com/problems/number-of-segments-in-a-string) | EASY | 2 | 1 |
| 2021-06-21 02:26 | [#面试题 08.01 三步问题](https://leetcode-cn.com/problems/three-steps-problem-lcci) | EASY | 2 | 1 |
| 2021-06-21 02:19 | [#605 种花问题](https://leetcode-cn.com/problems/can-place-flowers) | EASY | 4 | 1 |
| 2021-06-21 01:48 | [#1629 按键持续时间最长的键](https://leetcode-cn.com/problems/slowest-key) | EASY | 1 | 1 |
| 2021-06-18 09:55 | [#326 3的幂](https://leetcode-cn.com/problems/power-of-three) | EASY | 2 | 1 |
| 2021-06-18 09:03 | [#面试题 17.16 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | EASY | 2 | 1 |
| 2021-06-18 08:42 | [#1018 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) | EASY | 3 | 1 |
| 2021-06-18 08:18 | [#1805 字符串中不同整数的数目](https://leetcode-cn.com/problems/number-of-different-integers-in-a-string) | EASY | 1 | 1 |
| 2021-06-18 07:43 | [#501 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree) | EASY | 1 | 1 |
| 2021-06-18 07:22 | [#504 七进制数](https://leetcode-cn.com/problems/base-7) | EASY | 2 | 1 |
| 2021-06-18 06:56 | [#面试题 05.01 插入](https://leetcode-cn.com/problems/insert-into-bits-lcci) | EASY | 2 | 1 |
| 2021-06-18 03:54 | [#594 最长和谐子序列](https://leetcode-cn.com/problems/longest-harmonious-subsequence) | EASY | 3 | 1 |
| 2021-06-18 03:12 | [#459 重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern) | EASY | 2 | 1 |
| 2021-06-18 02:56 | [#263 丑数](https://leetcode-cn.com/problems/ugly-number) | EASY | 2 | 1 |
| 2021-06-18 02:46 | [#717 1比特与2比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) | EASY | 3 | 1 |
| 2021-06-18 02:31 | [#1646 获取生成数组中的最大值](https://leetcode-cn.com/problems/get-maximum-in-generated-array) | EASY | 10 | 1 |
| 2021-06-18 02:02 | [#599 两个列表的最小索引总和](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists) | EASY | 3 | **2** |
| 2021-06-17 10:28 | [#997 找到小镇的法官](https://leetcode-cn.com/problems/find-the-town-judge) | EASY | 2 | 1 |
| 2021-06-17 08:41 | [#541 反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii) | EASY | 7 | 1 |
| 2021-06-17 08:00 | [#1089 复写零](https://leetcode-cn.com/problems/duplicate-zeros) | EASY | 3 | 1 |
| 2021-06-17 07:40 | [#1071 字符串的最大公因子](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings) | EASY | 1 | 1 |
| 2021-06-17 06:47 | [#896 单调数列](https://leetcode-cn.com/problems/monotonic-array) | EASY | 6 | 1 |
| 2021-06-17 06:19 | [#1408 数组中的字符串匹配](https://leetcode-cn.com/problems/string-matching-in-an-array) | EASY | 5 | 1 |
| 2021-06-17 03:20 | [#455 分发饼干](https://leetcode-cn.com/problems/assign-cookies) | EASY | 1 | 1 |
| 2021-06-17 02:44 | [#590 N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal) | EASY | 2 | 1 |
| 2021-06-17 02:28 | [#145 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) | EASY | 7 | 1 |
| 2021-06-17 02:16 | [#65 有效数字](https://leetcode-cn.com/problems/valid-number) | HARD | 4 | 1 |
| 2021-06-16 14:37 | [#剑指 Offer 10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 17 | 1 |
| 2021-06-16 14:28 | [#1025 除数博弈](https://leetcode-cn.com/problems/divisor-game) | EASY | 3 | 1 |
| 2021-06-16 14:20 | [#877 石子游戏](https://leetcode-cn.com/problems/stone-game) | MEDIUM | 2 | **2** |
| 2021-06-16 10:01 | [#1184 公交站间的距离](https://leetcode-cn.com/problems/distance-between-bus-stops) | EASY | 1 | 1 |
| 2021-06-16 09:52 | [#1556 千位分隔数](https://leetcode-cn.com/problems/thousand-separator) | EASY | 1 | 1 |
| 2021-06-16 09:18 | [#剑指 Offer 58 - I 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof) | EASY | 2 | 1 |
| 2021-06-16 09:12 | [#1592 重新排列单词间的空格](https://leetcode-cn.com/problems/rearrange-spaces-between-words) | EASY | 1 | 1 |
| 2021-06-16 08:51 | [#724 寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index) | EASY | 2 | 1 |
| 2021-06-16 08:45 | [#482 密钥格式化](https://leetcode-cn.com/problems/license-key-formatting) | EASY | 1 | 1 |
| 2021-06-16 08:30 | [#290 单词规律](https://leetcode-cn.com/problems/word-pattern) | EASY | 1 | 1 |
| 2021-06-16 08:15 | [#1232 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) | EASY | 2 | 1 |
| 2021-06-16 07:58 | [#788 旋转数字](https://leetcode-cn.com/problems/rotated-digits) | EASY | 1 | 1 |
| 2021-06-16 07:46 | [#面试题 16.05 阶乘尾数](https://leetcode-cn.com/problems/factorial-zeros-lcci) | EASY | 3 | 1 |
| 2021-06-16 07:40 | [#1009 十进制整数的反码](https://leetcode-cn.com/problems/complement-of-base-10-integer) | EASY | 1 | 1 |
| 2021-06-16 07:35 | [#面试题 03.06 动物收容所](https://leetcode-cn.com/problems/animal-shelter-lcci) | EASY | 3 | 1 |
| 2021-06-16 07:11 | [#985 查询后的偶数和](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries) | EASY | 2 | 1 |
| 2021-06-16 06:57 | [#868 二进制间距](https://leetcode-cn.com/problems/binary-gap) | EASY | 2 | 1 |
| 2021-06-16 06:43 | [#1078 Bigram 分词](https://leetcode-cn.com/problems/occurrences-after-bigram) | EASY | 1 | 1 |
| 2021-06-16 06:32 | [#剑指 Offer 42 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | EASY | 1 | 0 |
| 2021-06-16 06:30 | [#812 最大三角形面积](https://leetcode-cn.com/problems/largest-triangle-area) | EASY | 1 | 0 |
| 2021-06-16 02:36 | [#LCP 07 传递信息](https://leetcode-cn.com/problems/chuan-di-xin-xi) | EASY | 3 | 1 |
| 2021-06-16 01:54 | [#892 三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes) | EASY | 2 | 1 |
| 2021-06-15 12:46 | [#面试题 16.17 连续数列](https://leetcode-cn.com/problems/contiguous-sequence-lcci) | EASY | 1 | 1 |
| 2021-06-15 12:42 | [#976 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle) | EASY | 2 | 1 |
| 2021-06-15 10:02 | [#929 独特的电子邮件地址](https://leetcode-cn.com/problems/unique-email-addresses) | EASY | 2 | 1 |
| 2021-06-15 09:52 | [#1441 用栈操作构建数组](https://leetcode-cn.com/problems/build-an-array-with-stack-operations) | EASY | 1 | 1 |
| 2021-06-15 09:33 | [#1337 矩阵中战斗力最弱的 K 行](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix) | EASY | 3 | 1 |
| 2021-06-15 07:49 | [#1790 仅执行一次字符串交换能否使两个字符串相等](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal) | EASY | 2 | 1 |
| 2021-06-15 07:37 | [#1399 统计最大组的数目](https://leetcode-cn.com/problems/count-largest-group) | EASY | 1 | 1 |
| 2021-06-15 07:05 | [#412 Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | EASY | 1 | 1 |
| 2021-06-15 06:57 | [#1640 能否连接形成数组](https://leetcode-cn.com/problems/check-array-formation-through-concatenation) | EASY | 2 | 1 |
| 2021-06-15 06:31 | [#1491 去掉最低工资和最高工资后的工资平均值](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary) | EASY | 1 | 1 |
| 2021-06-15 06:27 | [#1582 二进制矩阵中的特殊位置](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix) | EASY | 1 | 1 |
| 2021-06-15 02:56 | [#1716 计算力扣银行的钱](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank) | EASY | 3 | 1 |
| 2021-06-15 01:45 | [#852 山脉数组的峰顶索引](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array) | EASY | 5 | **2** |
| 2021-06-11 19:28 | [#242 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram) | EASY | 1 | 1 |
| 2021-06-11 19:05 | [#806 写字符串需要的行数](https://leetcode-cn.com/problems/number-of-lines-to-write-string) | EASY | 5 | 1 |
| 2021-06-11 18:26 | [#867 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix) | EASY | 1 | 1 |
| 2021-06-11 18:16 | [#1598 文件夹操作日志搜集器](https://leetcode-cn.com/problems/crawler-log-folder) | EASY | 1 | 1 |
| 2021-06-11 17:15 | [#961 重复 N 次的元素](https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array) | EASY | 1 | 1 |
| 2021-06-11 17:06 | [#剑指 Offer 03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 7 | 1 |
| 2021-06-11 16:47 | [#1332 删除回文子序列](https://leetcode-cn.com/problems/remove-palindromic-subsequences) | EASY | 2 | 1 |
| 2021-06-11 16:28 | [#122 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) | EASY | 1 | 1 |
| 2021-06-11 16:18 | [#999 可以被一步捕获的棋子数](https://leetcode-cn.com/problems/available-captures-for-rook) | EASY | 2 | 1 |
| 2021-06-11 09:55 | [#1694 重新格式化电话号码](https://leetcode-cn.com/problems/reformat-phone-number) | EASY | 5 | 1 |
| 2021-06-11 09:35 | [#1455 检查单词是否为句中其他单词的前缀](https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence) | EASY | 1 | 1 |
| 2021-06-11 09:16 | [#剑指 Offer 21 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof) | EASY | 1 | 1 |
| 2021-06-11 09:13 | [#1742 盒子中小球的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box) | EASY | 2 | 1 |
| 2021-06-11 09:01 | [#883 三维形体投影面积](https://leetcode-cn.com/problems/projection-area-of-3d-shapes) | EASY | 2 | 1 |
| 2021-06-11 08:41 | [#496 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i) | EASY | 1 | 1 |
| 2021-06-11 08:34 | [#509 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | EASY | 3 | 1 |
| 2021-06-11 08:29 | [#1122 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array) | EASY | 2 | 1 |
| 2021-06-11 08:17 | [#521 最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i) | EASY | 1 | 1 |
| 2021-06-11 08:12 | [#1403 非递增顺序的最小子序列](https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order) | EASY | 3 | 1 |
| 2021-06-11 07:58 | [#821 字符的最短距离](https://leetcode-cn.com/problems/shortest-distance-to-a-character) | EASY | 2 | 1 |
| 2021-06-11 07:43 | [#1413 逐步求和得到正数的最小值](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum) | EASY | 1 | 1 |
| 2021-06-11 07:29 | [#1160 拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) | EASY | 1 | 1 |
| 2021-06-11 07:16 | [#剑指 Offer 39 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2021-06-11 07:14 | [#面试题 02.01 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci) | EASY | 2 | 1 |
| 2021-06-11 06:55 | [#1800 最大升序子数组和](https://leetcode-cn.com/problems/maximum-ascending-subarray-sum) | EASY | 1 | 1 |
| 2021-06-11 06:50 | [#1200 最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference) | EASY | 1 | 1 |
| 2021-06-11 06:42 | [#575 分糖果](https://leetcode-cn.com/problems/distribute-candies) | EASY | 1 | 1 |
| 2021-06-11 06:30 | [#LCP 02 分式化简](https://leetcode-cn.com/problems/deep-dark-fraction) | EASY | 1 | 1 |
| 2021-06-11 06:17 | [#811 子域名访问计数](https://leetcode-cn.com/problems/subdomain-visit-count) | EASY | 1 | 1 |
| 2021-06-11 04:01 | [#1022 从根到叶的二进制数之和](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers) | EASY | 1 | 1 |
| 2021-06-11 03:53 | [#682 棒球比赛](https://leetcode-cn.com/problems/baseball-game) | EASY | 1 | 1 |
| 2021-06-11 03:38 | [#1752 检查数组是否经排序和轮转得到](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated) | EASY | 1 | 1 |
| 2021-06-11 03:23 | [#908 最小差值 I](https://leetcode-cn.com/problems/smallest-range-i) | EASY | 1 | 1 |
| 2021-06-11 03:13 | [#144 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) | EASY | 1 | 1 |
| 2021-06-11 03:10 | [#1710 卡车上的最大单元数](https://leetcode-cn.com/problems/maximum-units-on-a-truck) | EASY | 1 | 1 |
| 2021-06-11 03:00 | [#1848 到目标元素的最小距离](https://leetcode-cn.com/problems/minimum-distance-to-the-target-element) | EASY | 1 | 1 |
| 2021-06-11 02:55 | [#1217 玩筹码](https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position) | EASY | 1 | 1 |
| 2021-06-11 02:42 | [#476 数字的补数](https://leetcode-cn.com/problems/number-complement) | EASY | 1 | 1 |
| 2021-06-11 02:32 | [#面试题 05.07 配对交换](https://leetcode-cn.com/problems/exchange-lcci) | EASY | 1 | 1 |
| 2021-06-11 02:27 | [#1636 按照频率将数组升序排序](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency) | EASY | 1 | 1 |
| 2021-06-11 02:16 | [#剑指 Offer 57 - II 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) | EASY | 1 | 1 |
| 2021-06-10 15:30 | [#1287 有序数组中出现次数超过25%的元素](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array) | EASY | 1 | 1 |
| 2021-06-10 15:26 | [#1185 一周中的第几天](https://leetcode-cn.com/problems/day-of-the-week) | EASY | 1 | 1 |
| 2021-06-10 15:23 | [#面试题 03.02 栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci) | EASY | 1 | 1 |
| 2021-06-10 15:03 | [#1779 找到最近的有相同 X 或 Y 坐标的点](https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate) | EASY | 3 | 1 |
| 2021-06-10 14:36 | [#448 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 1 | 1 |
| 2021-06-10 14:26 | [#1189 “气球” 的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balloons) | EASY | 1 | 1 |
| 2021-06-10 14:17 | [#1046 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight) | EASY | 2 | 1 |
| 2021-06-10 14:09 | [#1652 拆炸弹](https://leetcode-cn.com/problems/defuse-the-bomb) | EASY | 2 | 1 |
| 2021-06-10 13:42 | [#剑指 Offer 57 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof) | EASY | 2 | 1 |
| 2021-06-10 13:33 | [#1550 存在连续三个奇数的数组](https://leetcode-cn.com/problems/three-consecutive-odds) | EASY | 2 | 1 |
| 2021-06-10 13:30 | [#1394 找出数组中的幸运数](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) | EASY | 2 | 1 |
| 2021-06-10 13:27 | [#剑指 Offer 50 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof) | EASY | 1 | 1 |
| 2021-06-10 13:12 | [#559 N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree) | EASY | 1 | 1 |
| 2021-06-10 13:02 | [#922 按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii) | EASY | 1 | 1 |
| 2021-06-10 12:53 | [#剑指 Offer 09 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 1 | 1 |
| 2021-06-10 10:18 | [#1385 两个数组间的距离值](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays) | EASY | 1 | 1 |
| 2021-06-10 10:10 | [#905 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity) | EASY | 1 | 1 |
| 2021-06-10 10:05 | [#500 键盘行](https://leetcode-cn.com/problems/keyboard-row) | EASY | 1 | 1 |
| 2021-06-10 09:52 | [#1380 矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix) | EASY | 1 | 1 |
| 2021-06-10 09:45 | [#893 特殊等价字符串组](https://leetcode-cn.com/problems/groups-of-special-equivalent-strings) | EASY | 3 | 1 |
| 2021-06-10 09:07 | [#766 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix) | EASY | 1 | 1 |
| 2021-06-10 08:46 | [#面试题 03.04 化栈为队](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci) | EASY | 1 | 1 |
| 2021-06-10 08:42 | [#933 最近的请求次数](https://leetcode-cn.com/problems/number-of-recent-calls) | EASY | 2 | 1 |
| 2021-06-10 08:33 | [#1502 判断能否形成等差数列](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence) | EASY | 1 | 1 |
| 2021-06-10 07:09 | [#1047 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) | EASY | 1 | 1 |
| 2021-06-10 06:58 | [#1304 和为零的N个唯一整数](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero) | EASY | 2 | 1 |
| 2021-06-10 06:50 | [#977 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array) | EASY | 1 | 1 |
| 2021-06-10 06:41 | [#1002 查找常用字符](https://leetcode-cn.com/problems/find-common-characters) | EASY | 1 | 1 |
| 2021-06-10 06:33 | [#1252 奇数值单元格的数目](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix) | EASY | 1 | 1 |
| 2021-06-10 05:11 | [#897 递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree) | EASY | 2 | 1 |
| 2021-06-10 05:07 | [#1351 统计有序矩阵中的负数](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix) | EASY | 4 | 1 |
| 2021-06-10 04:41 | [#1323 6 和 9 组成的最大数字](https://leetcode-cn.com/problems/maximum-69-number) | EASY | 2 | 1 |
| 2021-06-10 03:17 | [#1051 高度检查器](https://leetcode-cn.com/problems/height-checker) | EASY | 1 | 1 |
| 2021-06-10 03:08 | [#1460 通过翻转子数组使两个数组相等](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays) | EASY | 1 | 1 |
| 2021-06-10 03:01 | [#557 反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) | EASY | 1 | 1 |
| 2021-06-10 02:45 | [#1374 生成每种字符都是奇数个的字符串](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts) | EASY | 2 | 1 |
| 2021-06-10 02:31 | [#1876 长度为三且各字符不同的子字符串](https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters) | EASY | 1 | 1 |
| 2021-06-10 02:15 | [#518 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2) | MEDIUM | 1 | 1 |
| 2021-06-09 10:02 | [#剑指 Offer 05 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 1 | 1 |
| 2021-06-09 10:00 | [#1816 截断句子](https://leetcode-cn.com/problems/truncate-sentence) | EASY | 1 | 1 |
| 2021-06-09 09:58 | [#728 自除数](https://leetcode-cn.com/problems/self-dividing-numbers) | EASY | 2 | 1 |
| 2021-06-09 09:37 | [#1309 解码字母到整数映射](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping) | EASY | 2 | 1 |
| 2021-06-09 09:10 | [#1656 设计有序流](https://leetcode-cn.com/problems/design-an-ordered-stream) | EASY | 1 | 1 |
| 2021-06-09 08:50 | [#1464 数组中两元素的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array) | EASY | 1 | 1 |
| 2021-06-09 08:48 | [#1880 检查某单词是否等于两单词之和](https://leetcode-cn.com/problems/check-if-word-equals-summation-of-two-words) | EASY | 3 | 1 |
| 2021-06-09 08:26 | [#1812 判断国际象棋棋盘中一个格子的颜色](https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square) | EASY | 1 | 1 |
| 2021-06-09 08:17 | [#1725 可以形成最大正方形的矩形数目](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square) | EASY | 1 | 1 |
| 2021-06-09 08:11 | [#1827 最少操作使数组递增](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing) | EASY | 1 | 1 |
| 2021-06-09 08:04 | [#338 比特位计数](https://leetcode-cn.com/problems/counting-bits) | EASY | 2 | 1 |
| 2021-06-09 07:54 | [#面试题 04.02 最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci) | EASY | 2 | 1 |
| 2021-06-09 07:49 | [#832 翻转图像](https://leetcode-cn.com/problems/flipping-an-image) | EASY | 2 | 1 |
| 2021-06-09 07:37 | [#1837 K 进制表示下的各位数字总和](https://leetcode-cn.com/problems/sum-of-digits-in-base-k) | EASY | 1 | 1 |
| 2021-06-09 07:27 | [#1450 在既定时间做作业的学生人数](https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time) | EASY | 2 | 1 |
| 2021-06-09 07:20 | [#1221 分割平衡字符串](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings) | EASY | 2 | 1 |
| 2021-06-09 06:48 | [#1572 矩阵对角线元素的和](https://leetcode-cn.com/problems/matrix-diagonal-sum) | EASY | 1 | 1 |
| 2021-06-09 06:41 | [#1389 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | EASY | 3 | 1 |
| 2021-06-09 03:25 | [#1266 访问所有点的最小时间](https://leetcode-cn.com/problems/minimum-time-visiting-all-points) | EASY | 1 | 1 |
| 2021-06-09 02:47 | [#1773 统计匹配检索规则的物品数量](https://leetcode-cn.com/problems/count-items-matching-a-rule) | EASY | 1 | 1 |
| 2021-06-09 02:37 | [#1863 找出所有子集的异或总和再求和](https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals) | EASY | 2 | **2** |
| 2021-06-09 02:33 | [#1486 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array) | EASY | 1 | 1 |
| 2021-06-08 14:45 | [#109 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree) | MEDIUM | 1 | 1 |
| 2021-06-08 13:57 | [#108 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree) | EASY | 1 | 1 |
| 2021-06-08 09:53 | [#1869 哪种连续子字符串更长](https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros) | EASY | 1 | 1 |
| 2021-06-08 09:26 | [#1769 移动所有球到每个盒子所需的最小操作数](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box) | MEDIUM | 1 | 1 |
| 2021-06-08 07:21 | [#剑指 Offer 64 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof) | MEDIUM | 1 | 1 |
| 2021-06-08 07:20 | [#1672 最富有客户的资产总量](https://leetcode-cn.com/problems/richest-customer-wealth) | EASY | 1 | 1 |
| 2021-06-08 07:17 | [#807 保持城市天际线](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline) | MEDIUM | 2 | 1 |
| 2021-06-08 06:42 | [#1833 雪糕的最大数量](https://leetcode-cn.com/problems/maximum-ice-cream-bars) | MEDIUM | 1 | 1 |
| 2021-06-08 06:35 | [#535 TinyURL 的加密与解密](https://leetcode-cn.com/problems/encode-and-decode-tinyurl) | MEDIUM | 3 | 1 |
| 2021-06-08 06:21 | [#面试题 16.01 交换数字](https://leetcode-cn.com/problems/swap-numbers-lcci) | MEDIUM | 2 | 1 |
| 2021-06-08 06:18 | [#1281 整数的各位积和之差](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer) | EASY | 1 | 1 |
| 2021-06-08 03:12 | [#剑指 Offer 17 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof) | EASY | 1 | 1 |
| 2021-06-08 03:03 | [#1436 旅行终点站](https://leetcode-cn.com/problems/destination-city) | EASY | 1 | 1 |
| 2021-06-08 02:48 | [#657 机器人能否返回原点](https://leetcode-cn.com/problems/robot-return-to-origin) | EASY | 1 | 1 |
| 2021-06-08 02:38 | [#面试题 02.02 返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci) | EASY | 1 | 1 |
| 2021-06-08 02:26 | [#1768 交替合并字符串](https://leetcode-cn.com/problems/merge-strings-alternately) | EASY | 1 | 1 |
| 2021-06-08 02:17 | [#1049 最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii) | MEDIUM | 1 | 1 |
| 2021-06-07 10:13 | [#1299 将每个元素替换为右侧最大元素](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side) | EASY | 1 | 1 |
| 2021-06-07 10:05 | [#1859 将句子排序](https://leetcode-cn.com/problems/sorting-the-sentence) | EASY | 1 | 1 |
| 2021-06-07 09:46 | [#1732 找到最高海拔](https://leetcode-cn.com/problems/find-the-highest-altitude) | EASY | 2 | 1 |
| 2021-06-07 09:34 | [#1021 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses) | EASY | 1 | 1 |
| 2021-06-07 09:04 | [#1720 解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array) | EASY | 1 | 1 |
| 2021-06-07 08:55 | [#859 亲密字符串](https://leetcode-cn.com/problems/buddy-strings) | EASY | 1 | 1 |
| 2021-06-07 08:29 | [#665 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array) | MEDIUM | 1 | 1 |
| 2021-06-07 08:16 | [#LCP 33 蓄水](https://leetcode-cn.com/problems/o8SXZn) | EASY | 8 | 1 |
| 2021-06-07 06:54 | [#494 目标和](https://leetcode-cn.com/problems/target-sum) | MEDIUM | 1 | 1 |
| 2021-06-07 03:47 | [#563 二叉树的坡度](https://leetcode-cn.com/problems/binary-tree-tilt) | EASY | 2 | 1 |
| 2021-06-07 02:42 | [#561 数组拆分 I](https://leetcode-cn.com/problems/array-partition-i) | EASY | 1 | 1 |
| 2021-06-04 09:31 | [#1684 统计一致字符串的数目](https://leetcode-cn.com/problems/count-the-number-of-consistent-strings) | EASY | 1 | 1 |
| 2021-06-04 08:18 | [#1365 有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number) | EASY | 2 | 1 |
| 2021-06-04 07:53 | [#1832 判断句子是否为全字母句](https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram) | EASY | 1 | 1 |
| 2021-06-04 07:46 | [#1822 数组元素积的符号](https://leetcode-cn.com/problems/sign-of-the-product-of-an-array) | EASY | 1 | 1 |
| 2021-06-04 07:43 | [#1854 人口最多的年份](https://leetcode-cn.com/problems/maximum-population-year) | EASY | 2 | 1 |
| 2021-06-04 07:09 | [#938 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst) | EASY | 3 | 1 |
| 2021-06-04 06:48 | [#1662 检查两个字符串数组是否相等](https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent) | EASY | 1 | 1 |
| 2021-06-04 06:46 | [#1295 统计位数为偶数的数字](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits) | EASY | 2 | 1 |
| 2021-06-04 06:36 | [#1844 将所有数字用字符替换](https://leetcode-cn.com/problems/replace-all-digits-with-characters) | EASY | 1 | 1 |
| 2021-06-04 02:54 | [#160 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 4 | **2** |
| 2021-06-04 02:47 | [#888 公平的糖果棒交换](https://leetcode-cn.com/problems/fair-candy-swap) | EASY | 1 | 1 |
| 2021-06-03 03:03 | [#885 螺旋矩阵 III](https://leetcode-cn.com/problems/spiral-matrix-iii) | MEDIUM | 1 | 1 |
| 2021-06-03 02:14 | [#884 两句话中的不常见单词](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences) | EASY | 1 | 1 |
| 2021-06-02 07:33 | [#700 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) | EASY | 2 | 1 |
| 2021-06-02 07:12 | [#698 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets) | MEDIUM | 1 | 1 |
| 2021-06-02 06:39 | [#697 数组的度](https://leetcode-cn.com/problems/degree-of-an-array) | EASY | 1 | 1 |
| 2021-06-02 03:37 | [#696 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings) | EASY | 1 | 1 |
| 2021-06-02 03:23 | [#693 交替位二进制数](https://leetcode-cn.com/problems/binary-number-with-alternating-bits) | EASY | 2 | **2** |
| 2021-06-02 03:19 | [#692 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words) | MEDIUM | 1 | 1 |
| 2021-06-02 02:23 | [#690 员工的重要性](https://leetcode-cn.com/problems/employee-importance) | EASY | 2 | 1 |
| 2021-06-01 07:11 | [#面试题 08.08 有重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-ii-lcci) | MEDIUM | 1 | 1 |
| 2021-06-01 02:53 | [#面试题 08.07 无重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-i-lcci) | MEDIUM | 1 | 1 |
| 2021-06-01 02:35 | [#面试题 08.06 汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci) | EASY | 2 | **2** |
| 2021-05-31 09:54 | [#面试题 08.05 递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci) | MEDIUM | 2 | 1 |
| 2021-05-31 09:11 | [#面试题 08.04 幂集](https://leetcode-cn.com/problems/power-set-lcci) | MEDIUM | 2 | 1 |
| 2021-05-31 08:08 | [#面试题 08.03 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci) | EASY | 1 | 1 |
| 2021-05-31 07:47 | [#154 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) | HARD | 1 | 1 |
| 2021-05-31 07:44 | [#153 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) | MEDIUM | 2 | 1 |
| 2021-05-31 03:00 | [#152 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | MEDIUM | 2 | 1 |
| 2021-05-29 12:06 | [#217 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | EASY | 2 | 1 |
| 2021-05-28 09:09 | [#150 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | MEDIUM | 3 | 1 |
| 2021-05-28 07:37 | [#477 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance) | MEDIUM | 11 | **2** |
| 2021-05-28 07:34 | [#面试题 02.06 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci) | EASY | 1 | 1 |
| 2021-05-28 07:33 | [#234 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 1 | 1 |
| 2021-05-28 07:26 | [#剑指 Offer 52 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | EASY | 1 | 1 |
| 2021-05-28 07:24 | [#剑指 Offer 22 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | EASY | 1 | 1 |
| 2021-05-28 07:08 | [#面试题 02.07 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci) | EASY | 2 | 1 |
| 2021-05-28 06:55 | [#141 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 3 | **2** |
| 2021-05-28 06:47 | [#剑指 Offer 25 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof) | EASY | 1 | 1 |
| 2021-05-28 06:46 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 7 | **2** |
| 2021-05-28 06:29 | [#剑指 Offer 06 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 1 | 1 |
| 2021-05-28 05:55 | [#1290 二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) | EASY | 3 | **2** |
| 2021-05-28 05:02 | [#237 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | EASY | 3 | 1 |
| 2021-05-28 04:46 | [#剑指 Offer 18 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof) | EASY | 2 | 1 |
| 2021-05-28 04:33 | [#876 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list) | EASY | 1 | 1 |
| 2021-05-28 03:47 | [#剑指 Offer 24 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof) | EASY | 2 | 1 |
| 2021-05-27 07:42 | [#1704 判断字符串的两半是否相似](https://leetcode-cn.com/problems/determine-if-string-halves-are-alike) | EASY | 1 | 1 |
| 2021-05-27 07:29 | [#1701 平均等待时间](https://leetcode-cn.com/problems/average-waiting-time) | MEDIUM | 3 | 1 |
| 2021-05-27 03:48 | [#1700 无法吃午餐的学生数量](https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch) | EASY | 3 | 1 |
| 2021-05-26 09:19 | [#1678 设计 Goal 解析器](https://leetcode-cn.com/problems/goal-parser-interpretation) | EASY | 2 | 1 |
| 2021-05-26 09:09 | [#2 两数相加](https://leetcode-cn.com/problems/add-two-numbers) | MEDIUM | 2 | 1 |
| 2021-05-26 06:34 | [#面试题 17.14 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci) | MEDIUM | 1 | 1 |
| 2021-05-26 06:25 | [#面试题 17.10 主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci) | EASY | 6 | 1 |
| 2021-05-26 03:50 | [#486 预测赢家](https://leetcode-cn.com/problems/predict-the-winner) | MEDIUM | 1 | 1 |
| 2021-05-26 03:04 | [#292 Nim 游戏](https://leetcode-cn.com/problems/nim-game) | EASY | 1 | 1 |
| 2021-05-26 02:53 | [#382 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node) | MEDIUM | 1 | 1 |
| 2021-05-26 02:47 | [#398 随机数索引](https://leetcode-cn.com/problems/random-pick-index) | MEDIUM | 2 | 1 |
| 2021-05-26 02:22 | [#709 转换成小写字母](https://leetcode-cn.com/problems/to-lower-case) | EASY | 2 | 1 |
| 2021-05-25 06:39 | [#390 消除游戏](https://leetcode-cn.com/problems/elimination-game) | MEDIUM | 4 | 1 |
| 2021-05-25 03:48 | [#面试题 01.03 URL化](https://leetcode-cn.com/problems/string-to-url-lcci) | EASY | 2 | 1 |
| 2021-05-25 03:44 | [#225 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues) | EASY | 3 | 1 |
| 2021-05-23 14:31 | [#374 猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower) | EASY | 5 | 1 |
| 2021-05-18 07:37 | [#LCP 17 速算机器人](https://leetcode-cn.com/problems/nGK0Fy) | EASY | 1 | 1 |
| 2021-05-18 07:33 | [#LCP 29 乐团站位](https://leetcode-cn.com/problems/SNJvJP) | EASY | 1 | 1 |
| 2021-05-18 07:13 | [#LCP 18 早餐组合](https://leetcode-cn.com/problems/2vYnGI) | EASY | 2 | 1 |
| 2021-05-18 06:39 | [#LCP 28 采购方案](https://leetcode-cn.com/problems/4xy4Wx) | EASY | 1 | 1 |
| 2021-05-18 06:16 | [#面试题 16.11 跳水板](https://leetcode-cn.com/problems/diving-board-lcci) | EASY | 4 | 1 |
| 2021-05-18 05:06 | [#剑指 Offer 62 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2021-05-18 05:00 | [#剑指 Offer 61 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof) | EASY | 2 | 1 |
| 2021-05-18 04:44 | [#剑指 Offer 65 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof) | EASY | 3 | 1 |
| 2021-05-18 04:41 | [#剑指 Offer 53 - II 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof) | EASY | 2 | 1 |
| 2021-05-18 03:47 | [#1442 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) | MEDIUM | 2 | 1 |
| 2021-05-17 02:25 | [#993 二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) | EASY | 2 | 1 |
| 2021-05-17 02:00 | [#面试题 05.06 整数转换](https://leetcode-cn.com/problems/convert-integer-lcci) | EASY | 8 | 1 |
| 2021-05-15 08:33 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 10 | **2** |
| 2021-05-14 11:06 | [#面试题 16.07 最大数值](https://leetcode-cn.com/problems/maximum-lcci) | EASY | 1 | 1 |
| 2021-05-14 11:03 | [#面试题 17.01 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci) | EASY | 1 | 1 |
| 2021-05-14 11:02 | [#面试题 17.04 消失的数字](https://leetcode-cn.com/problems/missing-number-lcci) | EASY | 1 | 1 |
| 2021-05-14 10:37 | [#12 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | MEDIUM | 5 | **3** |
| 2021-05-14 10:36 | [#762 二进制表示中质数个计算置位](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation) | EASY | 1 | 1 |
| 2021-05-14 10:22 | [#1342 将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero) | EASY | 4 | 1 |
| 2021-05-14 09:22 | [#268 丢失的数字](https://leetcode-cn.com/problems/missing-number) | EASY | 4 | 1 |
| 2021-05-14 09:09 | [#231 2 的幂](https://leetcode-cn.com/problems/power-of-two) | EASY | 1 | 1 |
| 2021-05-14 09:05 | [#169 多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 1 | 1 |
| 2021-05-14 08:44 | [#342 4的幂](https://leetcode-cn.com/problems/power-of-four) | EASY | 5 | 1 |
| 2021-05-13 03:27 | [#944 删列造序](https://leetcode-cn.com/problems/delete-columns-to-make-sorted) | EASY | 1 | 1 |
| 2021-05-13 03:12 | [#1269 停在原地的方案数](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) | HARD | 4 | 1 |
| 2021-05-13 02:38 | [#222 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | MEDIUM | 3 | **2** |
| 2021-05-13 02:30 | [#1688 比赛中的配对次数](https://leetcode-cn.com/problems/count-of-matches-in-tournament) | EASY | 3 | 1 |
| 2021-05-13 02:18 | [#47 全排列 II](https://leetcode-cn.com/problems/permutations-ii) | MEDIUM | 3 | **3** |
| 2021-05-12 08:20 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 6 | **2** |
| 2021-05-11 08:33 | [#剑指 Offer 68 - II 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 | 1 |
| 2021-05-11 08:25 | [#剑指 Offer 68 - I 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 | 1 |
| 2021-05-11 08:16 | [#814 二叉树剪枝](https://leetcode-cn.com/problems/binary-tree-pruning) | MEDIUM | 1 | 1 |
| 2021-05-11 08:08 | [#543 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree) | EASY | 1 | 1 |
| 2021-05-10 09:43 | [#965 单值二叉树](https://leetcode-cn.com/problems/univalued-binary-tree) | EASY | 1 | 1 |
| 2021-05-10 09:38 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 7 | **3** |
| 2021-05-10 09:23 | [#872 叶子相似的树](https://leetcode-cn.com/problems/leaf-similar-trees) | EASY | 2 | 1 |
| 2021-05-10 09:15 | [#剑指 Offer 55 - I 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof) | EASY | 2 | 1 |
| 2021-05-10 09:06 | [#剑指 Offer 28 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 4 | **2** |
| 2021-05-10 08:56 | [#剑指 Offer 32 - II 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) | EASY | 1 | 1 |
| 2021-05-10 08:42 | [#剑指 Offer 55 - II 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof) | EASY | 2 | 1 |
| 2021-05-10 08:31 | [#剑指 Offer 27 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 3 | **2** |
| 2021-03-29 08:12 | [#1748 唯一元素的和](https://leetcode-cn.com/problems/sum-of-unique-elements) | EASY | 2 | 1 |
| 2021-03-29 03:52 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 3 | **2** |
| 2021-03-29 03:38 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 5 | **2** |
| 2021-03-25 02:41 | [#1116 打印零与奇偶数](https://leetcode-cn.com/problems/print-zero-even-odd) | MEDIUM | 2 | 1 |
| 2021-03-23 08:26 | [#1621 大小为 K 的不重叠线段的数目](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments) | MEDIUM | 1 | 1 |
| 2021-03-22 08:13 | [#1620 网络信号最好的坐标](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality) | MEDIUM | 5 | 1 |
| 2021-03-22 02:54 | [#1619 删除某些元素后的数组均值](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements) | EASY | 1 | 1 |
| 2021-03-19 15:50 | [#1603 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 3 | **2** |
| 2021-03-19 15:32 | [#剑指 Offer 54 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof) | EASY | 3 | **2** |
| 2020-12-21 06:33 | [#392 判断子序列](https://leetcode-cn.com/problems/is-subsequence) | EASY | 7 | 1 |
| 2020-12-18 08:42 | [#389 找不同](https://leetcode-cn.com/problems/find-the-difference) | EASY | 6 | **2** |
| 2020-12-04 07:12 | [#793 阶乘函数后 K 个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function) | HARD | 1 | 1 |
| 2020-12-03 15:48 | [#825 适龄的朋友](https://leetcode-cn.com/problems/friends-of-appropriate-ages) | MEDIUM | 1 | 1 |
| 2020-12-03 15:02 | [#824 山羊拉丁文](https://leetcode-cn.com/problems/goat-latin) | EASY | 2 | 1 |
| 2020-12-03 09:22 | [#46 全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 1 | 1 |
| 2020-12-02 07:28 | [#11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 1 | 1 |
| 2020-11-30 16:12 | [#LCP 22 黑白方格画](https://leetcode-cn.com/problems/ccw6C7) | EASY | 1 | 1 |
| 2020-11-30 09:43 | [#45 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii) | MEDIUM | 2 | 1 |
| 2020-11-26 08:42 | [#371 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | MEDIUM | 3 | 1 |
| 2020-11-26 06:48 | [#367 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square) | EASY | 5 | 1 |
| 2020-11-26 06:22 | [#357 计算各个位数不同的数字个数](https://leetcode-cn.com/problems/count-numbers-with-unique-digits) | MEDIUM | 4 | 1 |
| 2020-11-26 03:22 | [#350 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 2 | 1 |
| 2020-11-26 02:41 | [#349 两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays) | EASY | 4 | 1 |
| 2020-11-24 06:33 | [#201 数字范围按位与](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range) | MEDIUM | 1 | 1 |
| 2020-11-24 02:18 | [#206 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 2 | 1 |
| 2020-11-23 13:11 | [#1475 商品折扣后的最终价格](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop) | EASY | 1 | 1 |
| 2020-11-23 12:54 | [#1471 数组中的 k 个最强值](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array) | MEDIUM | 2 | 1 |
| 2020-11-23 11:52 | [#1470 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array) | EASY | 2 | **2** |
| 2020-11-23 09:21 | [#205 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings) | EASY | 4 | 1 |
| 2020-11-23 06:39 | [#204 计数质数](https://leetcode-cn.com/problems/count-primes) | EASY | 3 | 1 |
| 2020-11-23 03:15 | [#203 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | EASY | 3 | 1 |
| 2020-11-20 09:21 | [#202 快乐数](https://leetcode-cn.com/problems/happy-number) | EASY | 3 | 1 |
| 2020-11-20 08:12 | [#230 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) | MEDIUM | 4 | 1 |
| 2020-11-20 07:18 | [#229 求众数 II](https://leetcode-cn.com/problems/majority-element-ii) | MEDIUM | 5 | 1 |
| 2020-11-20 06:25 | [#228 汇总区间](https://leetcode-cn.com/problems/summary-ranges) | EASY | 6 | 1 |
| 2020-11-19 07:33 | [#198 打家劫舍](https://leetcode-cn.com/problems/house-robber) | MEDIUM | 2 | 1 |
| 2020-11-19 03:25 | [#283 移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 6 | **2** |
| 2020-11-18 18:24 | [#139 单词拆分](https://leetcode-cn.com/problems/word-break) | MEDIUM | 7 | 1 |
| 2020-11-18 17:51 | [#137 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) | MEDIUM | 3 | 1 |
| 2020-11-18 14:10 | [#136 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 4 | **2** |
| 2020-11-18 12:35 | [#135 分发糖果](https://leetcode-cn.com/problems/candy) | HARD | 2 | 1 |
| 2020-11-18 12:12 | [#134 加油站](https://leetcode-cn.com/problems/gas-station) | MEDIUM | 5 | 1 |
| 2020-11-18 09:04 | [#110 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree) | EASY | 10 | 1 |
| 2020-11-18 08:16 | [#73 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | MEDIUM | 5 | 1 |
| 2020-11-18 03:45 | [#257 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths) | EASY | 3 | **2** |
| 2020-11-18 02:29 | [#1079 活字印刷](https://leetcode-cn.com/problems/letter-tile-possibilities) | MEDIUM | 1 | 1 |
| 2020-11-17 07:08 | [#416 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | MEDIUM | 2 | 1 |
| 2020-11-16 23:46 | [#1030 距离顺序排列矩阵单元格](https://leetcode-cn.com/problems/matrix-cells-in-distance-order) | EASY | 2 | 1 |
| 2020-11-16 23:27 | [#1108 IP 地址无效化](https://leetcode-cn.com/problems/defanging-an-ip-address) | EASY | 2 | 1 |
| 2020-11-16 23:16 | [#1588 所有奇数长度子数组的和](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays) | EASY | 2 | 1 |
| 2020-11-16 10:28 | [#83 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 2 | 1 |
| 2020-11-15 01:04 | [#面试题 02.03 删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci) | EASY | 2 | 1 |
| 2020-11-14 15:37 | [#771 宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones) | EASY | 2 | 1 |
| 2020-11-14 06:38 | [#155 最小栈](https://leetcode-cn.com/problems/min-stack) | EASY | 2 | 1 |
| 2020-11-13 15:50 | [#1313 解压缩编码列表](https://leetcode-cn.com/problems/decompress-run-length-encoded-list) | EASY | 2 | 1 |
| 2020-11-12 13:54 | [#1539 第 k 个缺失的正整数](https://leetcode-cn.com/problems/kth-missing-positive-number) | EASY | 2 | 1 |
| 2020-11-12 11:16 | [#1528 重新排列字符串](https://leetcode-cn.com/problems/shuffle-string) | EASY | 4 | 1 |
| 2020-11-12 11:05 | [#1518 换酒问题](https://leetcode-cn.com/problems/water-bottles) | EASY | 4 | **2** |
| 2020-11-12 06:51 | [#125 验证回文串](https://leetcode-cn.com/problems/valid-palindrome) | EASY | 7 | **2** |
| 2020-11-11 14:49 | [#1507 转变日期格式](https://leetcode-cn.com/problems/reformat-date) | EASY | 5 | 1 |
| 2020-11-11 14:30 | [#1512 好数对的数目](https://leetcode-cn.com/problems/number-of-good-pairs) | EASY | 1 | 1 |
| 2020-11-11 08:44 | [#168 Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title) | EASY | 7 | 1 |
| 2020-11-11 08:05 | [#112 路径总和](https://leetcode-cn.com/problems/path-sum) | EASY | 6 | 1 |
| 2020-11-11 07:30 | [#69 x 的平方根](https://leetcode-cn.com/problems/sqrtx) | EASY | 10 | 1 |
| 2020-11-11 03:53 | [#172 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes) | EASY | 4 | 1 |
| 2020-11-11 03:37 | [#6 Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion) | MEDIUM | 8 | 1 |
| 2020-11-10 03:12 | [#31 下一个排列](https://leetcode-cn.com/problems/next-permutation) | MEDIUM | 3 | 1 |
| 2020-11-09 15:25 | [#剑指 Offer 30 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof) | EASY | 2 | 1 |
| 2020-11-09 15:09 | [#剑指 Offer 58 - II 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof) | EASY | 2 | 1 |
| 2020-11-09 15:06 | [#1431 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) | EASY | 3 | 1 |
| 2020-11-09 14:51 | [#1480 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | EASY | 4 | 1 |
| 2020-11-09 06:10 | [#973 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin) | MEDIUM | 8 | 1 |
| 2020-11-06 08:47 | [#238 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | MEDIUM | 8 | 1 |
| 2020-11-06 08:13 | [#1356 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits) | EASY | 1 | 1 |
| 2020-11-06 07:36 | [#LCP 01 猜数字](https://leetcode-cn.com/problems/guess-numbers) | EASY | 1 | 1 |
| 2020-11-06 07:33 | [#1608 特殊数组的特征值](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x) | EASY | 1 | 1 |
| 2020-11-06 04:57 | [#1604 警告一小时内使用相同员工卡大于等于三次的人](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period) | MEDIUM | 6 | 1 |
| 2020-11-05 08:30 | [#1624 两个相同字符之间的最长子字符串](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters) | EASY | 3 | 1 |
| 2020-11-05 02:38 | [#LCP 06 拿硬币](https://leetcode-cn.com/problems/na-ying-bi) | EASY | 3 | 1 |
| 2020-11-04 15:40 | [#57 插入区间](https://leetcode-cn.com/problems/insert-interval) | MEDIUM | 1 | 1 |
| 2020-11-04 15:09 | [#937 重新排列日志文件](https://leetcode-cn.com/problems/reorder-data-in-log-files) | EASY | 1 | 1 |
| 2020-11-04 14:58 | [#942 增减字符串匹配](https://leetcode-cn.com/problems/di-string-match) | EASY | 2 | 1 |
| 2020-11-04 09:18 | [#1614 括号的最大嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses) | EASY | 2 | 1 |
| 2020-11-03 14:57 | [#941 有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array) | EASY | 3 | 1 |
| 2020-11-02 15:56 | [#66 加一](https://leetcode-cn.com/problems/plus-one) | EASY | 2 | **2** |
| 2020-11-02 15:33 | [#58 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | EASY | 2 | 1 |
| 2020-11-02 07:45 | [#258 各位相加](https://leetcode-cn.com/problems/add-digits) | EASY | 2 | 1 |
| 2020-11-02 07:37 | [#300 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | MEDIUM | 1 | 1 |
| 2020-11-01 07:18 | [#101 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 1 | 1 |
| 2020-10-31 02:29 | [#381 O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed) | HARD | 8 | 1 |
| 2020-10-30 08:08 | [#463 岛屿的周长](https://leetcode-cn.com/problems/island-perimeter) | EASY | 2 | 1 |
| 2020-10-29 13:53 | [#10 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | HARD | 1 | 1 |
| 2020-10-29 13:23 | [#4 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | HARD | 5 | 1 |
| 2020-10-29 12:25 | [#面试题 01.01 判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci) | EASY | 4 | **2** |
| 2020-10-29 11:00 | [#129 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 4 | 1 |
| 2020-10-28 11:19 | [#1207 独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences) | EASY | 3 | 1 |
| 2020-09-09 16:08 | [#43 字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | MEDIUM | 4 | **2** |
| 2020-09-09 15:21 | [#42 接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | HARD | 1 | 1 |
| 2020-09-09 15:00 | [#41 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive) | HARD | 2 | 1 |
| 2020-09-09 14:02 | [#40 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii) | MEDIUM | 2 | 1 |
| 2020-09-09 13:34 | [#39 组合总和](https://leetcode-cn.com/problems/combination-sum) | MEDIUM | 1 | 1 |
| 2020-09-09 13:18 | [#面试题 01.02 判定是否互为字符重排](https://leetcode-cn.com/problems/check-permutation-lcci) | EASY | 3 | 1 |
| 2020-08-16 12:43 | [#1535 找出数组游戏的赢家](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game) | MEDIUM | 1 | 1 |
| 2020-08-16 10:42 | [#1534 统计好三元组](https://leetcode-cn.com/problems/count-good-triplets) | EASY | 1 | 1 |
| 2020-08-16 10:33 | [#405 数字转换为十六进制数](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal) | EASY | 6 | 1 |
| 2020-07-30 16:18 | [#1114 按序打印](https://leetcode-cn.com/problems/print-in-order) | EASY | 7 | 1 |
| 2020-07-30 15:49 | [#1179 重新格式化部门表](https://leetcode-cn.com/problems/reformat-department-table) | EASY | 2 | 1 |
| 2019-07-12 02:25 | [#70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 5 | 1 |
| 2019-05-27 05:29 | [#232 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks) | EASY | 3 | 1 |
| 2019-04-07 05:46 | [#189 旋转数组](https://leetcode-cn.com/problems/rotate-array) | MEDIUM | 2 | 1 |
| 2019-04-07 05:37 | [#167 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted) | EASY | 12 | 1 |
| 2019-04-06 15:23 | [#703 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | EASY | 5 | 1 |
| 2019-04-06 15:13 | [#8 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | MEDIUM | 5 | 1 |
| 2019-04-06 12:17 | [#194 转置文件](https://leetcode-cn.com/problems/transpose-file) | MEDIUM | 1 | 1 |
| 2018-09-28 07:47 | [#492 构造矩形](https://leetcode-cn.com/problems/construct-the-rectangle) | EASY | 1 | 1 |
| 2018-09-26 13:47 | [#380 O(1) 时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) | MEDIUM | 1 | 1 |
| 2018-09-26 13:35 | [#215 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | MEDIUM | 1 | 1 |
| 2018-09-26 13:34 | [#414 第三大的数](https://leetcode-cn.com/problems/third-maximum-number) | EASY | 1 | 1 |
| 2018-09-21 08:30 | [#415 字符串相加](https://leetcode-cn.com/problems/add-strings) | EASY | 1 | 1 |
| 2018-09-21 08:24 | [#67 二进制求和](https://leetcode-cn.com/problems/add-binary) | EASY | 1 | 1 |
| 2018-09-05 15:09 | [#387 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string) | EASY | 2 | 1 |
| 2018-09-05 14:09 | [#88 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 1 | 1 |
| 2018-09-05 13:36 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 11 | **2** |
| 2018-08-31 07:01 | [#307 区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable) | MEDIUM | 1 | 1 |
| 2018-08-31 06:57 | [#303 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable) | EASY | 1 | 1 |
| 2018-08-31 06:41 | [#50 Pow(x, n)](https://leetcode-cn.com/problems/powx-n) | MEDIUM | 6 | 1 |
| 2018-08-29 16:19 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | EASY | 3 | 1 |
| 2018-08-29 14:40 | [#53 最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 3 | 1 |
| 2018-08-29 11:03 | [#48 旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 3 | 1 |
| 2018-08-29 10:23 | [#443 压缩字符串](https://leetcode-cn.com/problems/string-compression) | MEDIUM | 2 | 1 |
| 2018-08-29 09:33 | [#38 外观数列](https://leetcode-cn.com/problems/count-and-say) | MEDIUM | 14 | 1 |
| 2018-08-29 07:48 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 4 | 1 |
| 2018-08-29 07:38 | [#26 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 5 | 1 |
| 2018-08-29 07:18 | [#278 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | EASY | 11 | 1 |
| 2018-08-29 06:40 | [#35 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 5 | 1 |
| 2018-08-28 09:12 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 5 | 1 |
| 2018-08-28 05:38 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 5 | 1 |
| 2018-08-27 08:44 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 7 | 1 |
| 2018-08-27 08:26 | [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 1 | 1 |
| 2018-08-27 08:21 | [#107 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | MEDIUM | 1 | 1 |
| 2018-08-27 08:11 | [#637 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) | EASY | 3 | 1 |
| 2018-08-27 03:01 | [#804 唯一摩尔斯密码词](https://leetcode-cn.com/problems/unique-morse-code-words) | EASY | 1 | 1 |
| 2018-08-25 03:50 | [#566 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | EASY | 2 | 1 |
| 2018-08-25 03:25 | [#344 反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 7 | 1 |
| 2018-08-25 02:48 | [#645 错误的集合](https://leetcode-cn.com/problems/set-mismatch) | EASY | 11 | 1 |
| 2018-08-24 13:52 | [#589 N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal) | EASY | 3 | 1 |
| 2018-08-24 12:55 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 3 | 1 |
| 2018-08-24 06:07 | [#171 Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number) | EASY | 1 | 1 |
| 2018-08-23 17:45 | [#100 相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 | 1 |
| 2018-08-23 17:33 | [#485 最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | EASY | 1 | 1 |
| 2018-08-23 17:21 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 1 | 1 |
| 2018-08-23 17:12 | [#118 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 2 | 1 |
| 2018-08-23 16:48 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 7 | 1 |
| 2018-08-22 12:23 | [#14 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 7 | 1 |
| 2018-08-22 08:28 | [#262 行程和用户](https://leetcode-cn.com/problems/trips-and-users) | HARD | 1 | 1 |
| 2018-08-22 08:13 | [#601 体育馆的人流量](https://leetcode-cn.com/problems/human-traffic-of-stadium) | HARD | 2 | 1 |
| 2018-08-22 08:07 | [#177 第N高的薪水](https://leetcode-cn.com/problems/nth-highest-salary) | MEDIUM | 4 | 1 |
| 2018-08-22 07:53 | [#180 连续出现的数字](https://leetcode-cn.com/problems/consecutive-numbers) | MEDIUM | 3 | 1 |
| 2018-08-22 07:32 | [#185 部门工资前三高的所有员工](https://leetcode-cn.com/problems/department-top-three-salaries) | HARD | 1 | 1 |
| 2018-08-22 07:24 | [#196 删除重复的电子邮箱](https://leetcode-cn.com/problems/delete-duplicate-emails) | EASY | 3 | 1 |
| 2018-08-22 07:12 | [#626 换座位](https://leetcode-cn.com/problems/exchange-seats) | MEDIUM | 1 | 1 |
| 2018-08-22 06:55 | [#184 部门工资最高的员工](https://leetcode-cn.com/problems/department-highest-salary) | MEDIUM | 9 | 1 |
| 2018-08-22 06:49 | [#178 分数排名](https://leetcode-cn.com/problems/rank-scores) | MEDIUM | 1 | 1 |
| 2018-08-22 06:22 | [#9 回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 1 | 1 |
| 2018-08-22 06:17 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 3 | 1 |
| 2018-08-22 04:27 | [#197 上升的温度](https://leetcode-cn.com/problems/rising-temperature) | EASY | 1 | 1 |
| 2018-08-22 03:52 | [#183 从不订购的客户](https://leetcode-cn.com/problems/customers-who-never-order) | EASY | 3 | 1 |
| 2018-08-22 03:44 | [#182 查找重复的电子邮箱](https://leetcode-cn.com/problems/duplicate-emails) | EASY | 1 | 1 |
| 2018-08-22 03:41 | [#181 超过经理收入的员工](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers) | EASY | 2 | 1 |
| 2018-08-22 03:35 | [#596 超过5名学生的课](https://leetcode-cn.com/problems/classes-more-than-5-students) | EASY | 2 | 1 |
| 2018-08-22 03:24 | [#595 大的国家](https://leetcode-cn.com/problems/big-countries) | EASY | 2 | 1 |
| 2018-08-22 03:20 | [#176 第二高的薪水](https://leetcode-cn.com/problems/second-highest-salary) | EASY | 4 | 1 |
| 2018-08-22 03:00 | [#627 变更性别](https://leetcode-cn.com/problems/swap-salary) | EASY | 2 | 1 |
| 2018-08-22 02:52 | [#860 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change) | EASY | 1 | 1 |
| 2018-08-21 16:03 | [#620 有趣的电影](https://leetcode-cn.com/problems/not-boring-movies) | EASY | 3 | 1 |
| 2018-08-21 11:24 | [#175 组合两个表](https://leetcode-cn.com/problems/combine-two-tables) | EASY | 1 | 1 |
| 2018-08-21 11:05 | [#192 统计词频](https://leetcode-cn.com/problems/word-frequency) | MEDIUM | 1 | 1 |
| 2018-08-21 10:59 | [#193 有效电话号码](https://leetcode-cn.com/problems/valid-phone-numbers) | EASY | 8 | 1 |
| 2018-08-21 10:36 | [#195 第十行](https://leetcode-cn.com/problems/tenth-line) | EASY | 12 | **2** |
