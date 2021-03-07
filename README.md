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

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2020-12-21 06:33 | [#392 判断子序列](https://leetcode-cn.com/problems/is-subsequence) | EASY | 7 | 1 |
| 2020-12-18 08:42 | [#389 找不同](https://leetcode-cn.com/problems/find-the-difference) | EASY | 6 | **2** |
| 2020-12-04 07:12 | [#793 阶乘函数后 K 个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function) | HARD | 1 | 1 |
| 2020-12-03 15:48 | [#825 适龄的朋友](https://leetcode-cn.com/problems/friends-of-appropriate-ages) | MEDIUM | 1 | 1 |
| 2020-12-03 15:02 | [#824 山羊拉丁文](https://leetcode-cn.com/problems/goat-latin) | EASY | 2 | 1 |
| 2020-12-03 09:22 | [#46 全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 1 | 1 |
| 2020-12-02 07:56 | [#12 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | MEDIUM | 4 | **2** |
| 2020-12-02 07:28 | [#11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 1 | 1 |
| 2020-12-02 02:33 | [#47 全排列 II](https://leetcode-cn.com/problems/permutations-ii) | MEDIUM | 2 | **2** |
| 2020-11-30 16:12 | [#LCP 22 黑白方格画](https://leetcode-cn.com/problems/ccw6C7) | EASY | 1 | 1 |
| 2020-11-30 09:43 | [#45 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii) | HARD | 2 | 1 |
| 2020-11-26 08:42 | [#371 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | MEDIUM | 3 | 1 |
| 2020-11-26 06:48 | [#367 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square) | EASY | 5 | 1 |
| 2020-11-26 06:22 | [#357 计算各个位数不同的数字个数](https://leetcode-cn.com/problems/count-numbers-with-unique-digits) | MEDIUM | 4 | 1 |
| 2020-11-26 03:22 | [#350 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 2 | 1 |
| 2020-11-26 02:41 | [#349 两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays) | EASY | 4 | 1 |
| 2020-11-24 15:18 | [#222 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | MEDIUM | 2 | 1 |
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
| 2020-11-17 14:42 | [#剑指 Offer 28 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 3 | 1 |
| 2020-11-17 13:28 | [#剑指 Offer 27 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 2 | 1 |
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
| 2020-11-06 08:57 | [#477 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance) | MEDIUM | 10 | 1 |
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
| 2020-10-30 08:28 | [#1603 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 1 | 1 |
| 2020-10-30 08:08 | [#463 岛屿的周长](https://leetcode-cn.com/problems/island-perimeter) | EASY | 2 | 1 |
| 2020-10-29 13:53 | [#10 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | HARD | 1 | 1 |
| 2020-10-29 13:23 | [#4 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | HARD | 5 | 1 |
| 2020-10-29 12:25 | [#面试题 01.01 判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci) | EASY | 4 | **2** |
| 2020-10-29 11:00 | [#129 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 4 | 1 |
| 2020-10-28 11:19 | [#1207 独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences) | EASY | 3 | 1 |
| 2020-09-16 13:22 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 5 | **2** |
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
| 2018-09-26 13:47 | [#380 常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) | MEDIUM | 1 | 1 |
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
| 2018-08-29 16:19 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | MEDIUM | 3 | 1 |
| 2018-08-29 14:40 | [#53 最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 3 | 1 |
| 2018-08-29 11:03 | [#48 旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 3 | 1 |
| 2018-08-29 10:23 | [#443 压缩字符串](https://leetcode-cn.com/problems/string-compression) | MEDIUM | 2 | 1 |
| 2018-08-29 09:33 | [#38 外观数列](https://leetcode-cn.com/problems/count-and-say) | EASY | 14 | 1 |
| 2018-08-29 07:48 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 4 | 1 |
| 2018-08-29 07:38 | [#26 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 5 | 1 |
| 2018-08-29 07:18 | [#278 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | EASY | 11 | 1 |
| 2018-08-29 06:40 | [#35 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 5 | 1 |
| 2018-08-29 05:26 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 5 | 1 |
| 2018-08-28 09:12 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 5 | 1 |
| 2018-08-28 05:38 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 5 | 1 |
| 2018-08-27 08:44 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 7 | 1 |
| 2018-08-27 08:26 | [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 1 | 1 |
| 2018-08-27 08:21 | [#107 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | MEDIUM | 1 | 1 |
| 2018-08-27 08:11 | [#637 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) | EASY | 3 | 1 |
| 2018-08-27 03:01 | [#804 唯一摩尔斯密码词](https://leetcode-cn.com/problems/unique-morse-code-words) | EASY | 1 | 1 |
| 2018-08-25 04:58 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 5 | 1 |
| 2018-08-25 04:29 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 2 | 1 |
| 2018-08-25 04:23 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 4 | 1 |
| 2018-08-25 03:50 | [#566 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | EASY | 2 | 1 |
| 2018-08-25 03:25 | [#344 反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 7 | 1 |
| 2018-08-25 02:48 | [#645 错误的集合](https://leetcode-cn.com/problems/set-mismatch) | EASY | 11 | 1 |
| 2018-08-24 13:52 | [#589 N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal) | EASY | 3 | 1 |
| 2018-08-24 12:55 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 3 | 1 |
| 2018-08-24 12:32 | [#852 山脉数组的峰顶索引](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array) | EASY | 4 | 1 |
| 2018-08-24 06:07 | [#171 Excel表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number) | EASY | 1 | 1 |
| 2018-08-23 17:45 | [#100 相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 | 1 |
| 2018-08-23 17:33 | [#485 最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | EASY | 1 | 1 |
| 2018-08-23 17:21 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 1 | 1 |
| 2018-08-23 17:12 | [#118 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 2 | 1 |
| 2018-08-23 16:48 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 7 | 1 |
| 2018-08-22 12:42 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 9 | 1 |
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
