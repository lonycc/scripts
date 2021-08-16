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

> 总提交次数: 1549, 总通过次数: 975, 已通过题数: 616

> 已通过题目的难度和数量: EASY = 474, MEDIUM = 129, HARD = 13, 

| 最近提交时间 | 题目 | 题目难度 | 提交次数 |
| ---- | ---- | ---- | ---- |
| 2021-08-13 04:56  | [删除字符使字符串变好](https://leetcode-cn.com/problems/delete-characters-to-make-fancy-string) | EASY | 2 |
| 2021-08-10 02:23  | [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | MEDIUM | 1 |
| 2021-08-10 01:57  | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs) | MEDIUM | 1 |
| 2021-08-09 01:45  | [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 5 |
| 2021-08-06 07:15  | [字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | MEDIUM | 7 |
| 2021-08-05 09:38  | [杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 3 |
| 2021-08-05 09:35  | [最长回文串](https://leetcode-cn.com/problems/longest-palindrome) | EASY | 2 |
| 2021-08-05 09:24  | [设计哈希映射](https://leetcode-cn.com/problems/design-hashmap) | EASY | 2 |
| 2021-08-05 09:22  | [字符串相加](https://leetcode-cn.com/problems/add-strings) | EASY | 3 |
| 2021-08-05 09:19  | [单词规律](https://leetcode-cn.com/problems/word-pattern) | EASY | 2 |
| 2021-08-04 23:23  | [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2) | MEDIUM | 3 |
| 2021-08-03 08:01  | [生成匹配的括号](https://leetcode-cn.com/problems/IDBivT) | MEDIUM | 1 |
| 2021-08-03 07:57  | [三除数](https://leetcode-cn.com/problems/three-divisors) | EASY | 1 |
| 2021-08-03 07:07  | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum) | MEDIUM | 1 |
| 2021-08-03 06:51  | [最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence) | MEDIUM | 1 |
| 2021-08-03 06:36  | [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence) | MEDIUM | 1 |
| 2021-08-03 01:49  | [不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees) | MEDIUM | 1 |
| 2021-08-03 01:43  | [判断子序列](https://leetcode-cn.com/problems/is-subsequence) | EASY | 8 |
| 2021-07-30 08:44  | [等差数列划分](https://leetcode-cn.com/problems/arithmetic-slices) | MEDIUM | 1 |
| 2021-07-30 08:00  | [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii) | MEDIUM | 1 |
| 2021-07-30 07:46  | [不同路径](https://leetcode-cn.com/problems/unique-paths) | MEDIUM | 1 |
| 2021-07-30 02:46  | [比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare) | EASY | 3 |
| 2021-07-30 02:44  | [Excel 表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number) | EASY | 2 |
| 2021-07-30 02:24  | [检查是否所有字符出现次数相同](https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences) | EASY | 1 |
| 2021-07-30 02:18  | [字符串转化后的各位数字之和](https://leetcode-cn.com/problems/sum-of-digits-of-string-after-convert) | EASY | 1 |
| 2021-07-30 02:10  | [多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 2 |
| 2021-07-30 02:08  | [只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 6 |
| 2021-07-28 10:06  | [杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 4 |
| 2021-07-26 14:06  | [二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree) | MEDIUM | 1 |
| 2021-07-26 14:02  | [单词拆分](https://leetcode-cn.com/problems/word-break) | MEDIUM | 9 |
| 2021-07-26 06:39  | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | MEDIUM | 3 |
| 2021-07-26 06:11  | [位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 4 |
| 2021-07-26 06:10  | [颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 6 |
| 2021-07-26 06:04  | [路径总和](https://leetcode-cn.com/problems/path-sum) | EASY | 7 |
| 2021-07-26 06:01  | [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 8 |
| 2021-07-26 05:59  | [二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) | EASY | 3 |
| 2021-07-26 05:56  | [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree) | EASY | 4 |
| 2021-07-26 05:54  | [两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst) | EASY | 2 |
| 2021-07-23 03:02  | [检查是否区域内所有整数都被覆盖](https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered) | EASY | 5 |
| 2021-07-23 03:00  | [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | MEDIUM | 1 |
| 2021-07-23 02:49  | [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | MEDIUM | 1 |
| 2021-07-23 02:38  | [三角形最小路径和](https://leetcode-cn.com/problems/triangle) | MEDIUM | 1 |
| 2021-07-23 02:16  | [打家劫舍](https://leetcode-cn.com/problems/house-robber) | MEDIUM | 4 |
| 2021-07-23 02:14  | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 7 |
| 2021-07-23 02:09  | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 3 |
| 2021-07-23 02:02  | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 8 |
| 2021-07-23 02:00  | [对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 3 |
| 2021-07-22 07:10  | [判断矩阵经轮转后是否一致](https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation) | EASY | 1 |
| 2021-07-22 06:58  | [旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 4 |
| 2021-07-22 06:45  | [01 矩阵](https://leetcode-cn.com/problems/01-matrix) | MEDIUM | 1 |
| 2021-07-22 03:51  | [字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation) | MEDIUM | 1 |
| 2021-07-22 03:27  | [全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 4 |
| 2021-07-22 02:30  | [组合](https://leetcode-cn.com/problems/combinations) | MEDIUM | 2 |
| 2021-07-22 02:25  | [最佳观光组合](https://leetcode-cn.com/problems/best-sightseeing-pair) | MEDIUM | 1 |
| 2021-07-22 02:16  | [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 5 |
| 2021-07-22 02:15  | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) | EASY | 2 |
| 2021-07-22 02:14  | [二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) | EASY | 8 |
| 2021-07-22 02:10  | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | EASY | 4 |
| 2021-07-22 02:10  | [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) | EASY | 2 |
| 2021-07-21 02:48  | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 9 |
| 2021-07-21 02:48  | [反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 5 |
| 2021-07-21 02:41  | [乘积为正数的最长子数组长度](https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product) | MEDIUM | 1 |
| 2021-07-21 02:05  | [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | MEDIUM | 3 |
| 2021-07-21 02:01  | [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks) | EASY | 4 |
| 2021-07-21 01:54  | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 6 |
| 2021-07-20 09:57  | [可以输入的最大单词数](https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type) | EASY | 2 |
| 2021-07-20 09:52  | [数组中最大数对和的最小值](https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array) | MEDIUM | 2 |
| 2021-07-20 03:00  | [环形子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-circular-subarray) | MEDIUM | 1 |
| 2021-07-20 02:32  | [腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges) | MEDIUM | 1 |
| 2021-07-20 02:05  | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 5 |
| 2021-07-20 01:58  | [删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 4 |
| 2021-07-19 09:12  | [移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | EASY | 4 |
| 2021-07-19 08:55  | [岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island) | MEDIUM | 1 |
| 2021-07-19 02:14  | [填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node) | MEDIUM | 1 |
| 2021-07-19 02:03  | [跳跃游戏](https://leetcode-cn.com/problems/jump-game) | MEDIUM | 1 |
| 2021-07-19 01:56  | [跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii) | MEDIUM | 4 |
| 2021-07-19 01:30  | [环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 4 |
| 2021-07-19 01:24  | [合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 4 |
| 2021-07-18 01:14  | [删除并获得点数](https://leetcode-cn.com/problems/delete-and-earn) | MEDIUM | 2 |
| 2021-07-18 01:01  | [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii) | MEDIUM | 1 |
| 2021-07-18 00:35  | [图像渲染](https://leetcode-cn.com/problems/flood-fill) | EASY | 2 |
| 2021-07-18 00:32  | [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram) | EASY | 2 |
| 2021-07-18 00:29  | [赎金信](https://leetcode-cn.com/problems/ransom-note) | EASY | 3 |
| 2021-07-18 00:15  | [字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string) | EASY | 4 |
| 2021-07-17 23:42  | [字符串的排列](https://leetcode-cn.com/problems/permutation-in-string) | MEDIUM | 1 |
| 2021-07-17 09:11  | [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | MEDIUM | 1 |
| 2021-07-17 04:11  | [使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) | EASY | 2 |
| 2021-07-17 03:59  | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku) | MEDIUM | 2 |
| 2021-07-17 02:23  | [矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | MEDIUM | 7 |
| 2021-07-16 07:18  | [第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number) | EASY | 2 |
| 2021-07-16 07:15  | [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | EASY | 4 |
| 2021-07-16 07:08  | [圆形赛道上经过次数最多的扇区](https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track) | EASY | 1 |
| 2021-07-16 07:04  | [最长的美好子字符串](https://leetcode-cn.com/problems/longest-nice-substring) | EASY | 2 |
| 2021-07-16 06:50  | [在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | EASY | 7 |
| 2021-07-16 02:25  | [重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | EASY | 5 |
| 2021-07-16 02:09  | [删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) | MEDIUM | 1 |
| 2021-07-16 02:00  | [链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list) | EASY | 2 |
| 2021-07-15 01:34  | [反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) | EASY | 2 |
| 2021-07-15 01:32  | [反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 8 |
| 2021-07-15 01:28  | [两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 3 |
| 2021-07-14 03:02  | [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 3 |
| 2021-07-13 17:00  | [两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 12 |
| 2021-07-13 16:56  | [两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted) | EASY | 13 |
| 2021-07-13 16:49  | [移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 7 |
| 2021-07-13 09:33  | [二叉搜索树节点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes) | EASY | 1 |
| 2021-07-13 08:51  | [另一棵树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree) | EASY | 4 |
| 2021-07-13 08:05  | [重复至少 K 次且长度为 M 的模式](https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times) | EASY | 1 |
| 2021-07-13 02:43  | [存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | EASY | 3 |
| 2021-07-13 00:00  | [旋转数组](https://leetcode-cn.com/problems/rotate-array) | MEDIUM | 3 |
| 2021-07-12 23:51  | [有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array) | EASY | 2 |
| 2021-07-12 13:03  | [搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 6 |
| 2021-07-12 13:01  | [第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | EASY | 12 |
| 2021-07-12 12:58  | [二分查找](https://leetcode-cn.com/problems/binary-search) | EASY | 6 |
| 2021-07-12 06:30  | [统计平方和三元组的数目](https://leetcode-cn.com/problems/count-square-sum-triples) | EASY | 1 |
| 2021-07-12 03:44  | [判断字符串是否可分解为值均等的子串](https://leetcode-cn.com/problems/check-if-string-is-decomposable-into-value-equal-substrings) | EASY | 6 |
| 2021-07-12 02:12  | [H 指数 II](https://leetcode-cn.com/problems/h-index-ii) | MEDIUM | 1 |
| 2021-07-12 01:58  | [数组串联](https://leetcode-cn.com/problems/concatenation-of-array) | EASY | 1 |
| 2021-07-09 05:57  | [二叉树中第二小的节点](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree) | EASY | 1 |
| 2021-07-09 03:33  | [主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci) | EASY | 8 |
| 2021-07-05 03:21  | [二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst) | EASY | 1 |
| 2021-07-05 02:40  | [基于排列构建数组](https://leetcode-cn.com/problems/build-array-from-permutation) | EASY | 1 |
| 2021-07-02 07:25  | [等价多米诺骨牌对的数量](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs) | EASY | 3 |
| 2021-07-02 07:08  | [检查整数及其两倍数是否存在](https://leetcode-cn.com/problems/check-if-n-and-its-double-exist) | EASY | 1 |
| 2021-07-02 07:00  | [数组序号转换](https://leetcode-cn.com/problems/rank-transform-of-an-array) | EASY | 1 |
| 2021-07-02 06:46  | [范围求和 II](https://leetcode-cn.com/problems/range-addition-ii) | EASY | 2 |
| 2021-07-02 06:36  | [旋转字符串](https://leetcode-cn.com/problems/rotate-string) | EASY | 1 |
| 2021-07-02 03:49  | [左叶子之和](https://leetcode-cn.com/problems/sum-of-left-leaves) | EASY | 1 |
| 2021-07-02 03:42  | [替换所有的问号](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters) | EASY | 1 |
| 2021-07-02 03:29  | [雪糕的最大数量](https://leetcode-cn.com/problems/maximum-ice-cream-bars) | MEDIUM | 2 |
| 2021-07-02 03:24  | [最小操作次数使数组元素相等](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements) | EASY | 2 |
| 2021-07-02 03:08  | [最大重复子字符串](https://leetcode-cn.com/problems/maximum-repeating-substring) | EASY | 4 |
| 2021-07-02 02:50  | [生成交替二进制字符串的最少操作数](https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string) | EASY | 1 |
| 2021-07-02 02:29  | [替换隐藏数字得到的最晚时间](https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits) | EASY | 2 |
| 2021-07-02 02:02  | [图片平滑器](https://leetcode-cn.com/problems/image-smoother) | EASY | 2 |
| 2021-07-01 09:48  | [删除一个元素使数组严格递增](https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing) | EASY | 3 |
| 2021-07-01 08:22  | [完成一半题目](https://leetcode-cn.com/problems/WqXACV) | EASY | 4 |
| 2021-07-01 08:02  | [上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string) | EASY | 1 |
| 2021-07-01 07:58  | [较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups) | EASY | 1 |
| 2021-07-01 07:50  | [找出星型图的中心节点](https://leetcode-cn.com/problems/find-center-of-star-graph) | EASY | 1 |
| 2021-07-01 07:46  | [两个数对之间的最大乘积差](https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs) | EASY | 1 |
| 2021-07-01 07:42  | [K 次取反后最大化的数组和](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations) | EASY | 1 |
| 2021-07-01 07:04  | [有效的回旋镖](https://leetcode-cn.com/problems/valid-boomerang) | EASY | 1 |
| 2021-07-01 06:56  | [分糖果 II](https://leetcode-cn.com/problems/distribute-candies-to-people) | EASY | 2 |
| 2021-07-01 06:46  | [最常见的单词](https://leetcode-cn.com/problems/most-common-word) | EASY | 2 |
| 2021-07-01 02:41  | [子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i) | EASY | 1 |
| 2021-07-01 02:29  | [排列硬币](https://leetcode-cn.com/problems/arranging-coins) | EASY | 1 |
| 2021-07-01 02:13  | [寻找比目标字母大的最小字母](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target) | EASY | 1 |
| 2021-06-30 10:17  | [至少是其他数字两倍的最大数](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others) | EASY | 2 |
| 2021-06-30 10:10  | [最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence) | EASY | 2 |
| 2021-06-30 02:46  | [是否所有 1 都至少相隔 k 个元素](https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away) | EASY | 1 |
| 2021-06-30 02:40  | [整理字符串](https://leetcode-cn.com/problems/make-the-string-great) | EASY | 1 |
| 2021-06-29 10:18  | [判断路径是否相交](https://leetcode-cn.com/problems/path-crossing) | EASY | 3 |
| 2021-06-29 08:21  | [子集](https://leetcode-cn.com/problems/subsets) | MEDIUM | 4 |
| 2021-06-29 08:06  | [用户分组](https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to) | MEDIUM | 1 |
| 2021-06-29 07:49  | [十-二进制数的最少数目](https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers) | MEDIUM | 1 |
| 2021-06-29 07:41  | [统计一个圆中点的数目](https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle) | MEDIUM | 1 |
| 2021-06-27 15:13  | [提莫攻击](https://leetcode-cn.com/problems/teemo-attacking) | EASY | 1 |
| 2021-06-25 07:24  | [存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii) | EASY | 1 |
| 2021-06-25 06:51  | [一年中的第几天](https://leetcode-cn.com/problems/day-of-the-year) | EASY | 1 |
| 2021-06-25 06:45  | [质数排列](https://leetcode-cn.com/problems/prime-arrangements) | EASY | 1 |
| 2021-06-24 08:59  | [三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | EASY | 1 |
| 2021-06-24 08:57  | [将整数转换为两个无零整数的和](https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers) | EASY | 1 |
| 2021-06-24 08:41  | [数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer) | EASY | 3 |
| 2021-06-24 06:21  | [重新分配字符使所有字符串都相等](https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal) | EASY | 1 |
| 2021-06-24 02:57  | [仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters) | EASY | 1 |
| 2021-06-24 02:46  | [检查二进制字符串字段](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones) | EASY | 2 |
| 2021-06-24 02:40  | [字符串中第二大的数字](https://leetcode-cn.com/problems/second-largest-digit-in-a-string) | EASY | 1 |
| 2021-06-24 02:30  | [字符串中的最大奇数](https://leetcode-cn.com/problems/largest-odd-number-in-string) | EASY | 1 |
| 2021-06-24 02:06  | [学生出勤记录 I](https://leetcode-cn.com/problems/student-attendance-record-i) | EASY | 1 |
| 2021-06-24 01:58  | [相对名次](https://leetcode-cn.com/problems/relative-ranks) | EASY | 1 |
| 2021-06-23 10:32  | [检测大写字母](https://leetcode-cn.com/problems/detect-capital) | EASY | 1 |
| 2021-06-23 10:16  | [设计哈希集合](https://leetcode-cn.com/problems/design-hashset) | EASY | 1 |
| 2021-06-23 07:34  | [期望个数统计](https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji) | EASY | 2 |
| 2021-06-23 07:23  | [颜色填充](https://leetcode-cn.com/problems/color-fill-lcci) | EASY | 1 |
| 2021-06-23 07:03  | [字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci) | EASY | 1 |
| 2021-06-23 06:51  | [珠玑妙算](https://leetcode-cn.com/problems/master-mind-lcci) | EASY | 3 |
| 2021-06-23 06:37  | [稀疏数组搜索](https://leetcode-cn.com/problems/sparse-array-search-lcci) | EASY | 1 |
| 2021-06-23 03:45  | [顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof) | EASY | 1 |
| 2021-06-23 03:22  | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 1 |
| 2021-06-23 03:22  | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | MEDIUM | 6 |
| 2021-06-23 02:32  | [旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 1 |
| 2021-06-23 02:26  | [三合一](https://leetcode-cn.com/problems/three-in-one-lcci) | EASY | 1 |
| 2021-06-23 02:08  | [在区间范围内统计奇数数目](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range) | EASY | 1 |
| 2021-06-23 02:01  | [二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | EASY | 2 |
| 2021-06-23 01:57  | [连续字符](https://leetcode-cn.com/problems/consecutive-characters) | EASY | 1 |
| 2021-06-22 10:08  | [重新格式化字符串](https://leetcode-cn.com/problems/reformat-the-string) | EASY | 1 |
| 2021-06-22 09:46  | [分割字符串的最大得分](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string) | EASY | 1 |
| 2021-06-22 09:32  | [日期之间隔几天](https://leetcode-cn.com/problems/number-of-days-between-two-dates) | EASY | 1 |
| 2021-06-22 09:16  | [青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof) | EASY | 5 |
| 2021-06-22 09:09  | [BiNode](https://leetcode-cn.com/problems/binode-lcci) | EASY | 1 |
| 2021-06-22 07:39  | [合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci) | EASY | 1 |
| 2021-06-22 06:48  | [字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof) | MEDIUM | 1 |
| 2021-06-22 06:46  | [检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci) | EASY | 2 |
| 2021-06-22 06:36  | [字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | EASY | 5 |
| 2021-06-22 03:46  | [回文排列](https://leetcode-cn.com/problems/palindrome-permutation-lcci) | EASY | 2 |
| 2021-06-22 03:33  | [下载插件](https://leetcode-cn.com/problems/Ju9Xwi) | EASY | 5 |
| 2021-06-21 09:14  | [长按键入](https://leetcode-cn.com/problems/long-pressed-name) | EASY | 4 |
| 2021-06-21 08:32  | [翻转数位](https://leetcode-cn.com/problems/reverse-bits-lcci) | EASY | 1 |
| 2021-06-21 08:22  | [将数组分成和相等的三个部分](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum) | EASY | 1 |
| 2021-06-21 08:08  | [验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii) | EASY | 1 |
| 2021-06-21 06:30  | [完美数](https://leetcode-cn.com/problems/perfect-number) | EASY | 2 |
| 2021-06-21 03:34  | [移动石子直到连续](https://leetcode-cn.com/problems/moving-stones-until-consecutive) | MEDIUM | 3 |
| 2021-06-21 02:33  | [字符串中的单词数](https://leetcode-cn.com/problems/number-of-segments-in-a-string) | EASY | 2 |
| 2021-06-21 02:26  | [三步问题](https://leetcode-cn.com/problems/three-steps-problem-lcci) | EASY | 2 |
| 2021-06-21 02:19  | [种花问题](https://leetcode-cn.com/problems/can-place-flowers) | EASY | 4 |
| 2021-06-21 01:48  | [按键持续时间最长的键](https://leetcode-cn.com/problems/slowest-key) | EASY | 1 |
| 2021-06-18 09:55  | [3的幂](https://leetcode-cn.com/problems/power-of-three) | EASY | 2 |
| 2021-06-18 09:03  | [按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | EASY | 2 |
| 2021-06-18 08:42  | [可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) | EASY | 3 |
| 2021-06-18 08:18  | [字符串中不同整数的数目](https://leetcode-cn.com/problems/number-of-different-integers-in-a-string) | EASY | 1 |
| 2021-06-18 07:43  | [二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree) | EASY | 1 |
| 2021-06-18 07:22  | [七进制数](https://leetcode-cn.com/problems/base-7) | EASY | 2 |
| 2021-06-18 06:56  | [插入](https://leetcode-cn.com/problems/insert-into-bits-lcci) | EASY | 2 |
| 2021-06-18 03:54  | [最长和谐子序列](https://leetcode-cn.com/problems/longest-harmonious-subsequence) | EASY | 3 |
| 2021-06-18 03:12  | [重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern) | EASY | 2 |
| 2021-06-18 02:56  | [丑数](https://leetcode-cn.com/problems/ugly-number) | EASY | 2 |
| 2021-06-18 02:46  | [1比特与2比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) | EASY | 3 |
| 2021-06-18 02:31  | [获取生成数组中的最大值](https://leetcode-cn.com/problems/get-maximum-in-generated-array) | EASY | 10 |
| 2021-06-18 02:02  | [两个列表的最小索引总和](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists) | EASY | 3 |
| 2021-06-17 10:28  | [找到小镇的法官](https://leetcode-cn.com/problems/find-the-town-judge) | EASY | 2 |
| 2021-06-17 08:41  | [反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii) | EASY | 7 |
| 2021-06-17 08:00  | [复写零](https://leetcode-cn.com/problems/duplicate-zeros) | EASY | 3 |
| 2021-06-17 07:40  | [字符串的最大公因子](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings) | EASY | 1 |
| 2021-06-17 06:47  | [单调数列](https://leetcode-cn.com/problems/monotonic-array) | EASY | 6 |
| 2021-06-17 06:19  | [数组中的字符串匹配](https://leetcode-cn.com/problems/string-matching-in-an-array) | EASY | 5 |
| 2021-06-17 03:20  | [分发饼干](https://leetcode-cn.com/problems/assign-cookies) | EASY | 1 |
| 2021-06-17 02:44  | [N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal) | EASY | 2 |
| 2021-06-17 02:16  | [有效数字](https://leetcode-cn.com/problems/valid-number) | HARD | 4 |
| 2021-06-16 14:37  | [斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 17 |
| 2021-06-16 14:28  | [除数博弈](https://leetcode-cn.com/problems/divisor-game) | EASY | 3 |
| 2021-06-16 14:20  | [石子游戏](https://leetcode-cn.com/problems/stone-game) | MEDIUM | 2 |
| 2021-06-16 10:01  | [公交站间的距离](https://leetcode-cn.com/problems/distance-between-bus-stops) | EASY | 1 |
| 2021-06-16 09:52  | [千位分隔数](https://leetcode-cn.com/problems/thousand-separator) | EASY | 1 |
| 2021-06-16 09:18  | [翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof) | EASY | 2 |
| 2021-06-16 09:12  | [重新排列单词间的空格](https://leetcode-cn.com/problems/rearrange-spaces-between-words) | EASY | 1 |
| 2021-06-16 08:51  | [寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index) | EASY | 2 |
| 2021-06-16 08:45  | [密钥格式化](https://leetcode-cn.com/problems/license-key-formatting) | EASY | 1 |
| 2021-06-16 08:15  | [缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) | EASY | 2 |
| 2021-06-16 07:58  | [旋转数字](https://leetcode-cn.com/problems/rotated-digits) | MEDIUM | 1 |
| 2021-06-16 07:46  | [阶乘尾数](https://leetcode-cn.com/problems/factorial-zeros-lcci) | EASY | 3 |
| 2021-06-16 07:40  | [十进制整数的反码](https://leetcode-cn.com/problems/complement-of-base-10-integer) | EASY | 1 |
| 2021-06-16 07:35  | [动物收容所](https://leetcode-cn.com/problems/animal-shelter-lcci) | EASY | 3 |
| 2021-06-16 07:11  | [查询后的偶数和](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries) | MEDIUM | 2 |
| 2021-06-16 06:57  | [二进制间距](https://leetcode-cn.com/problems/binary-gap) | EASY | 2 |
| 2021-06-16 06:43  | [Bigram 分词](https://leetcode-cn.com/problems/occurrences-after-bigram) | EASY | 1 |
| 2021-06-16 06:32  | [连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | EASY | 1 |
| 2021-06-16 06:30  | [最大三角形面积](https://leetcode-cn.com/problems/largest-triangle-area) | EASY | 1 |
| 2021-06-16 02:36  | [传递信息](https://leetcode-cn.com/problems/chuan-di-xin-xi) | EASY | 3 |
| 2021-06-16 01:54  | [三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes) | EASY | 2 |
| 2021-06-15 12:46  | [连续数列](https://leetcode-cn.com/problems/contiguous-sequence-lcci) | EASY | 1 |
| 2021-06-15 12:42  | [三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle) | EASY | 2 |
| 2021-06-15 10:02  | [独特的电子邮件地址](https://leetcode-cn.com/problems/unique-email-addresses) | EASY | 2 |
| 2021-06-15 09:52  | [用栈操作构建数组](https://leetcode-cn.com/problems/build-an-array-with-stack-operations) | EASY | 1 |
| 2021-06-15 09:33  | [矩阵中战斗力最弱的 K 行](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix) | EASY | 3 |
| 2021-06-15 07:49  | [仅执行一次字符串交换能否使两个字符串相等](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal) | EASY | 2 |
| 2021-06-15 07:37  | [统计最大组的数目](https://leetcode-cn.com/problems/count-largest-group) | EASY | 1 |
| 2021-06-15 07:05  | [Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | EASY | 1 |
| 2021-06-15 06:57  | [能否连接形成数组](https://leetcode-cn.com/problems/check-array-formation-through-concatenation) | EASY | 2 |
| 2021-06-15 06:31  | [去掉最低工资和最高工资后的工资平均值](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary) | EASY | 1 |
| 2021-06-15 06:27  | [二进制矩阵中的特殊位置](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix) | EASY | 1 |
| 2021-06-15 02:56  | [计算力扣银行的钱](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank) | EASY | 3 |
| 2021-06-15 01:45  | [山脉数组的峰顶索引](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array) | EASY | 5 |
| 2021-06-11 19:05  | [写字符串需要的行数](https://leetcode-cn.com/problems/number-of-lines-to-write-string) | EASY | 5 |
| 2021-06-11 18:26  | [转置矩阵](https://leetcode-cn.com/problems/transpose-matrix) | EASY | 1 |
| 2021-06-11 18:16  | [文件夹操作日志搜集器](https://leetcode-cn.com/problems/crawler-log-folder) | EASY | 1 |
| 2021-06-11 17:15  | [重复 N 次的元素](https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array) | EASY | 1 |
| 2021-06-11 17:06  | [数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 7 |
| 2021-06-11 16:47  | [删除回文子序列](https://leetcode-cn.com/problems/remove-palindromic-subsequences) | EASY | 2 |
| 2021-06-11 16:18  | [可以被一步捕获的棋子数](https://leetcode-cn.com/problems/available-captures-for-rook) | EASY | 2 |
| 2021-06-11 09:55  | [重新格式化电话号码](https://leetcode-cn.com/problems/reformat-phone-number) | EASY | 5 |
| 2021-06-11 09:35  | [检查单词是否为句中其他单词的前缀](https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence) | EASY | 1 |
| 2021-06-11 09:16  | [调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof) | EASY | 1 |
| 2021-06-11 09:13  | [盒子中小球的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box) | EASY | 2 |
| 2021-06-11 09:01  | [三维形体投影面积](https://leetcode-cn.com/problems/projection-area-of-3d-shapes) | EASY | 2 |
| 2021-06-11 08:41  | [下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i) | EASY | 1 |
| 2021-06-11 08:29  | [数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array) | EASY | 2 |
| 2021-06-11 08:17  | [最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i) | EASY | 1 |
| 2021-06-11 08:12  | [非递增顺序的最小子序列](https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order) | EASY | 3 |
| 2021-06-11 07:58  | [字符的最短距离](https://leetcode-cn.com/problems/shortest-distance-to-a-character) | EASY | 2 |
| 2021-06-11 07:43  | [逐步求和得到正数的最小值](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum) | EASY | 1 |
| 2021-06-11 07:29  | [拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) | EASY | 1 |
| 2021-06-11 07:16  | [数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof) | EASY | 1 |
| 2021-06-11 07:14  | [移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci) | EASY | 2 |
| 2021-06-11 06:55  | [最大升序子数组和](https://leetcode-cn.com/problems/maximum-ascending-subarray-sum) | EASY | 1 |
| 2021-06-11 06:50  | [最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference) | EASY | 1 |
| 2021-06-11 06:42  | [分糖果](https://leetcode-cn.com/problems/distribute-candies) | EASY | 1 |
| 2021-06-11 06:30  | [分式化简](https://leetcode-cn.com/problems/deep-dark-fraction) | EASY | 1 |
| 2021-06-11 06:17  | [子域名访问计数](https://leetcode-cn.com/problems/subdomain-visit-count) | MEDIUM | 1 |
| 2021-06-11 04:01  | [从根到叶的二进制数之和](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers) | EASY | 1 |
| 2021-06-11 03:53  | [棒球比赛](https://leetcode-cn.com/problems/baseball-game) | EASY | 1 |
| 2021-06-11 03:38  | [检查数组是否经排序和轮转得到](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated) | EASY | 1 |
| 2021-06-11 03:23  | [最小差值 I](https://leetcode-cn.com/problems/smallest-range-i) | EASY | 1 |
| 2021-06-11 03:10  | [卡车上的最大单元数](https://leetcode-cn.com/problems/maximum-units-on-a-truck) | EASY | 1 |
| 2021-06-11 03:00  | [到目标元素的最小距离](https://leetcode-cn.com/problems/minimum-distance-to-the-target-element) | EASY | 1 |
| 2021-06-11 02:55  | [玩筹码](https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position) | EASY | 1 |
| 2021-06-11 02:42  | [数字的补数](https://leetcode-cn.com/problems/number-complement) | EASY | 1 |
| 2021-06-11 02:32  | [配对交换](https://leetcode-cn.com/problems/exchange-lcci) | EASY | 1 |
| 2021-06-11 02:27  | [按照频率将数组升序排序](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency) | EASY | 1 |
| 2021-06-11 02:16  | [和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) | EASY | 1 |
| 2021-06-10 15:30  | [有序数组中出现次数超过25%的元素](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array) | EASY | 1 |
| 2021-06-10 15:26  | [一周中的第几天](https://leetcode-cn.com/problems/day-of-the-week) | EASY | 1 |
| 2021-06-10 15:23  | [栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci) | EASY | 1 |
| 2021-06-10 15:03  | [找到最近的有相同 X 或 Y 坐标的点](https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate) | EASY | 3 |
| 2021-06-10 14:36  | [找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 1 |
| 2021-06-10 14:26  | [“气球” 的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balloons) | EASY | 1 |
| 2021-06-10 14:17  | [最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight) | EASY | 2 |
| 2021-06-10 14:09  | [拆炸弹](https://leetcode-cn.com/problems/defuse-the-bomb) | EASY | 2 |
| 2021-06-10 13:42  | [和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof) | EASY | 2 |
| 2021-06-10 13:33  | [存在连续三个奇数的数组](https://leetcode-cn.com/problems/three-consecutive-odds) | EASY | 2 |
| 2021-06-10 13:30  | [找出数组中的幸运数](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) | EASY | 2 |
| 2021-06-10 13:27  | [第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof) | EASY | 1 |
| 2021-06-10 13:12  | [N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree) | EASY | 1 |
| 2021-06-10 13:02  | [按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii) | EASY | 1 |
| 2021-06-10 12:53  | [用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 1 |
| 2021-06-10 10:18  | [两个数组间的距离值](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays) | EASY | 1 |
| 2021-06-10 10:10  | [按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity) | EASY | 1 |
| 2021-06-10 10:05  | [键盘行](https://leetcode-cn.com/problems/keyboard-row) | EASY | 1 |
| 2021-06-10 09:52  | [矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix) | EASY | 1 |
| 2021-06-10 09:45  | [特殊等价字符串组](https://leetcode-cn.com/problems/groups-of-special-equivalent-strings) | MEDIUM | 3 |
| 2021-06-10 09:07  | [托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix) | EASY | 1 |
| 2021-06-10 08:46  | [化栈为队](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci) | EASY | 1 |
| 2021-06-10 08:42  | [最近的请求次数](https://leetcode-cn.com/problems/number-of-recent-calls) | EASY | 2 |
| 2021-06-10 08:33  | [判断能否形成等差数列](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence) | EASY | 1 |
| 2021-06-10 07:09  | [删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) | EASY | 1 |
| 2021-06-10 06:58  | [和为零的N个唯一整数](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero) | EASY | 2 |
| 2021-06-10 06:41  | [查找常用字符](https://leetcode-cn.com/problems/find-common-characters) | EASY | 1 |
| 2021-06-10 06:33  | [奇数值单元格的数目](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix) | EASY | 1 |
| 2021-06-10 05:11  | [递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree) | EASY | 2 |
| 2021-06-10 05:07  | [统计有序矩阵中的负数](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix) | EASY | 4 |
| 2021-06-10 04:41  | [6 和 9 组成的最大数字](https://leetcode-cn.com/problems/maximum-69-number) | EASY | 2 |
| 2021-06-10 03:17  | [高度检查器](https://leetcode-cn.com/problems/height-checker) | EASY | 1 |
| 2021-06-10 03:08  | [通过翻转子数组使两个数组相等](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays) | EASY | 1 |
| 2021-06-10 02:45  | [生成每种字符都是奇数个的字符串](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts) | EASY | 2 |
| 2021-06-10 02:31  | [长度为三且各字符不同的子字符串](https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters) | EASY | 1 |
| 2021-06-09 10:02  | [替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 1 |
| 2021-06-09 10:00  | [截断句子](https://leetcode-cn.com/problems/truncate-sentence) | EASY | 1 |
| 2021-06-09 09:58  | [自除数](https://leetcode-cn.com/problems/self-dividing-numbers) | EASY | 2 |
| 2021-06-09 09:37  | [解码字母到整数映射](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping) | EASY | 2 |
| 2021-06-09 09:10  | [设计有序流](https://leetcode-cn.com/problems/design-an-ordered-stream) | EASY | 1 |
| 2021-06-09 08:50  | [数组中两元素的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array) | EASY | 1 |
| 2021-06-09 08:48  | [检查某单词是否等于两单词之和](https://leetcode-cn.com/problems/check-if-word-equals-summation-of-two-words) | EASY | 3 |
| 2021-06-09 08:26  | [判断国际象棋棋盘中一个格子的颜色](https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square) | EASY | 1 |
| 2021-06-09 08:17  | [可以形成最大正方形的矩形数目](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square) | EASY | 1 |
| 2021-06-09 08:11  | [最少操作使数组递增](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing) | EASY | 1 |
| 2021-06-09 08:04  | [比特位计数](https://leetcode-cn.com/problems/counting-bits) | EASY | 2 |
| 2021-06-09 07:54  | [最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci) | EASY | 2 |
| 2021-06-09 07:49  | [翻转图像](https://leetcode-cn.com/problems/flipping-an-image) | EASY | 2 |
| 2021-06-09 07:37  | [K 进制表示下的各位数字总和](https://leetcode-cn.com/problems/sum-of-digits-in-base-k) | EASY | 1 |
| 2021-06-09 07:27  | [在既定时间做作业的学生人数](https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time) | EASY | 2 |
| 2021-06-09 07:20  | [分割平衡字符串](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings) | EASY | 2 |
| 2021-06-09 06:48  | [矩阵对角线元素的和](https://leetcode-cn.com/problems/matrix-diagonal-sum) | EASY | 1 |
| 2021-06-09 06:41  | [按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | EASY | 3 |
| 2021-06-09 03:25  | [访问所有点的最小时间](https://leetcode-cn.com/problems/minimum-time-visiting-all-points) | EASY | 1 |
| 2021-06-09 02:47  | [统计匹配检索规则的物品数量](https://leetcode-cn.com/problems/count-items-matching-a-rule) | EASY | 1 |
| 2021-06-09 02:37  | [找出所有子集的异或总和再求和](https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals) | EASY | 2 |
| 2021-06-09 02:33  | [数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array) | EASY | 1 |
| 2021-06-08 14:45  | [有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree) | MEDIUM | 1 |
| 2021-06-08 13:57  | [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree) | EASY | 1 |
| 2021-06-08 09:53  | [哪种连续子字符串更长](https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros) | EASY | 1 |
| 2021-06-08 09:26  | [移动所有球到每个盒子所需的最小操作数](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box) | MEDIUM | 1 |
| 2021-06-08 07:21  | [求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof) | MEDIUM | 1 |
| 2021-06-08 07:20  | [最富有客户的资产总量](https://leetcode-cn.com/problems/richest-customer-wealth) | EASY | 1 |
| 2021-06-08 07:17  | [保持城市天际线](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline) | MEDIUM | 2 |
| 2021-06-08 06:35  | [TinyURL 的加密与解密](https://leetcode-cn.com/problems/encode-and-decode-tinyurl) | MEDIUM | 3 |
| 2021-06-08 06:21  | [交换数字](https://leetcode-cn.com/problems/swap-numbers-lcci) | MEDIUM | 2 |
| 2021-06-08 06:18  | [整数的各位积和之差](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer) | EASY | 1 |
| 2021-06-08 03:12  | [打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof) | EASY | 1 |
| 2021-06-08 03:03  | [旅行终点站](https://leetcode-cn.com/problems/destination-city) | EASY | 1 |
| 2021-06-08 02:48  | [机器人能否返回原点](https://leetcode-cn.com/problems/robot-return-to-origin) | EASY | 1 |
| 2021-06-08 02:38  | [返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci) | EASY | 1 |
| 2021-06-08 02:26  | [交替合并字符串](https://leetcode-cn.com/problems/merge-strings-alternately) | EASY | 1 |
| 2021-06-08 02:17  | [最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii) | MEDIUM | 1 |
| 2021-06-07 10:13  | [将每个元素替换为右侧最大元素](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side) | EASY | 1 |
| 2021-06-07 10:05  | [将句子排序](https://leetcode-cn.com/problems/sorting-the-sentence) | EASY | 1 |
| 2021-06-07 09:46  | [找到最高海拔](https://leetcode-cn.com/problems/find-the-highest-altitude) | EASY | 2 |
| 2021-06-07 09:34  | [删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses) | EASY | 1 |
| 2021-06-07 09:04  | [解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array) | EASY | 1 |
| 2021-06-07 08:55  | [亲密字符串](https://leetcode-cn.com/problems/buddy-strings) | EASY | 1 |
| 2021-06-07 08:29  | [非递减数列](https://leetcode-cn.com/problems/non-decreasing-array) | MEDIUM | 1 |
| 2021-06-07 08:16  | [蓄水](https://leetcode-cn.com/problems/o8SXZn) | EASY | 8 |
| 2021-06-07 06:54  | [目标和](https://leetcode-cn.com/problems/target-sum) | MEDIUM | 1 |
| 2021-06-07 03:47  | [二叉树的坡度](https://leetcode-cn.com/problems/binary-tree-tilt) | EASY | 2 |
| 2021-06-07 02:42  | [数组拆分 I](https://leetcode-cn.com/problems/array-partition-i) | EASY | 1 |
| 2021-06-04 09:31  | [统计一致字符串的数目](https://leetcode-cn.com/problems/count-the-number-of-consistent-strings) | EASY | 1 |
| 2021-06-04 08:18  | [有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number) | EASY | 2 |
| 2021-06-04 07:53  | [判断句子是否为全字母句](https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram) | EASY | 1 |
| 2021-06-04 07:46  | [数组元素积的符号](https://leetcode-cn.com/problems/sign-of-the-product-of-an-array) | EASY | 1 |
| 2021-06-04 07:43  | [人口最多的年份](https://leetcode-cn.com/problems/maximum-population-year) | EASY | 2 |
| 2021-06-04 07:09  | [二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst) | EASY | 3 |
| 2021-06-04 06:48  | [检查两个字符串数组是否相等](https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent) | EASY | 1 |
| 2021-06-04 06:46  | [统计位数为偶数的数字](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits) | EASY | 2 |
| 2021-06-04 06:36  | [将所有数字用字符替换](https://leetcode-cn.com/problems/replace-all-digits-with-characters) | EASY | 1 |
| 2021-06-04 02:47  | [公平的糖果棒交换](https://leetcode-cn.com/problems/fair-candy-swap) | EASY | 1 |
| 2021-06-03 03:03  | [螺旋矩阵 III](https://leetcode-cn.com/problems/spiral-matrix-iii) | MEDIUM | 1 |
| 2021-06-03 02:14  | [两句话中的不常见单词](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences) | EASY | 1 |
| 2021-06-02 07:12  | [划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets) | MEDIUM | 1 |
| 2021-06-02 06:39  | [数组的度](https://leetcode-cn.com/problems/degree-of-an-array) | EASY | 1 |
| 2021-06-02 03:37  | [计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings) | EASY | 1 |
| 2021-06-02 03:23  | [交替位二进制数](https://leetcode-cn.com/problems/binary-number-with-alternating-bits) | EASY | 2 |
| 2021-06-02 03:19  | [前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words) | MEDIUM | 1 |
| 2021-06-02 02:23  | [员工的重要性](https://leetcode-cn.com/problems/employee-importance) | EASY | 2 |
| 2021-06-01 07:11  | [有重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-ii-lcci) | MEDIUM | 1 |
| 2021-06-01 02:53  | [无重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-i-lcci) | MEDIUM | 1 |
| 2021-06-01 02:35  | [汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci) | EASY | 2 |
| 2021-05-31 09:54  | [递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci) | MEDIUM | 2 |
| 2021-05-31 09:11  | [幂集](https://leetcode-cn.com/problems/power-set-lcci) | MEDIUM | 2 |
| 2021-05-31 08:08  | [魔术索引](https://leetcode-cn.com/problems/magic-index-lcci) | EASY | 1 |
| 2021-05-31 07:47  | [寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) | HARD | 1 |
| 2021-05-31 07:44  | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) | MEDIUM | 2 |
| 2021-05-28 09:09  | [逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | MEDIUM | 3 |
| 2021-05-28 07:37  | [汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance) | MEDIUM | 11 |
| 2021-05-28 07:34  | [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci) | EASY | 1 |
| 2021-05-28 07:33  | [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 1 |
| 2021-05-28 07:26  | [两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | EASY | 1 |
| 2021-05-28 07:24  | [链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | EASY | 1 |
| 2021-05-28 07:08  | [链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci) | EASY | 2 |
| 2021-05-28 06:47  | [合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof) | EASY | 1 |
| 2021-05-28 06:29  | [从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 1 |
| 2021-05-28 05:55  | [二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) | EASY | 3 |
| 2021-05-28 05:02  | [删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | EASY | 3 |
| 2021-05-28 04:46  | [删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof) | EASY | 2 |
| 2021-05-28 03:47  | [反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof) | EASY | 2 |
| 2021-05-27 07:42  | [判断字符串的两半是否相似](https://leetcode-cn.com/problems/determine-if-string-halves-are-alike) | EASY | 1 |
| 2021-05-27 07:29  | [平均等待时间](https://leetcode-cn.com/problems/average-waiting-time) | MEDIUM | 3 |
| 2021-05-27 03:48  | [无法吃午餐的学生数量](https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch) | EASY | 3 |
| 2021-05-26 09:19  | [设计 Goal 解析器](https://leetcode-cn.com/problems/goal-parser-interpretation) | EASY | 2 |
| 2021-05-26 09:09  | [两数相加](https://leetcode-cn.com/problems/add-two-numbers) | MEDIUM | 2 |
| 2021-05-26 06:34  | [最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci) | MEDIUM | 1 |
| 2021-05-26 03:50  | [预测赢家](https://leetcode-cn.com/problems/predict-the-winner) | MEDIUM | 1 |
| 2021-05-26 03:04  | [Nim 游戏](https://leetcode-cn.com/problems/nim-game) | EASY | 1 |
| 2021-05-26 02:53  | [链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node) | MEDIUM | 1 |
| 2021-05-26 02:47  | [随机数索引](https://leetcode-cn.com/problems/random-pick-index) | MEDIUM | 2 |
| 2021-05-26 02:22  | [转换成小写字母](https://leetcode-cn.com/problems/to-lower-case) | EASY | 2 |
| 2021-05-25 06:39  | [消除游戏](https://leetcode-cn.com/problems/elimination-game) | MEDIUM | 4 |
| 2021-05-25 03:48  | [URL化](https://leetcode-cn.com/problems/string-to-url-lcci) | EASY | 2 |
| 2021-05-25 03:44  | [用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues) | EASY | 3 |
| 2021-05-23 14:31  | [猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower) | EASY | 5 |
| 2021-05-18 07:37  | [速算机器人](https://leetcode-cn.com/problems/nGK0Fy) | EASY | 1 |
| 2021-05-18 07:33  | [乐团站位](https://leetcode-cn.com/problems/SNJvJP) | EASY | 1 |
| 2021-05-18 07:13  | [早餐组合](https://leetcode-cn.com/problems/2vYnGI) | EASY | 2 |
| 2021-05-18 06:39  | [采购方案](https://leetcode-cn.com/problems/4xy4Wx) | EASY | 1 |
| 2021-05-18 06:16  | [跳水板](https://leetcode-cn.com/problems/diving-board-lcci) | EASY | 4 |
| 2021-05-18 05:06  | [圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | EASY | 1 |
| 2021-05-18 05:00  | [扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof) | EASY | 2 |
| 2021-05-18 04:44  | [不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof) | EASY | 3 |
| 2021-05-18 04:41  | [0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof) | EASY | 2 |
| 2021-05-18 03:47  | [形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) | MEDIUM | 2 |
| 2021-05-17 02:25  | [二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) | EASY | 2 |
| 2021-05-17 02:00  | [整数转换](https://leetcode-cn.com/problems/convert-integer-lcci) | EASY | 8 |
| 2021-05-15 08:33  | [罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 10 |
| 2021-05-14 11:06  | [最大数值](https://leetcode-cn.com/problems/maximum-lcci) | EASY | 1 |
| 2021-05-14 11:03  | [不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci) | EASY | 1 |
| 2021-05-14 11:02  | [消失的数字](https://leetcode-cn.com/problems/missing-number-lcci) | EASY | 1 |
| 2021-05-14 10:37  | [整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | MEDIUM | 5 |
| 2021-05-14 10:36  | [二进制表示中质数个计算置位](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation) | EASY | 1 |
| 2021-05-14 10:22  | [将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero) | EASY | 4 |
| 2021-05-14 09:22  | [丢失的数字](https://leetcode-cn.com/problems/missing-number) | EASY | 4 |
| 2021-05-14 09:09  | [2 的幂](https://leetcode-cn.com/problems/power-of-two) | EASY | 1 |
| 2021-05-14 08:44  | [4的幂](https://leetcode-cn.com/problems/power-of-four) | EASY | 5 |
| 2021-05-13 03:27  | [删列造序](https://leetcode-cn.com/problems/delete-columns-to-make-sorted) | EASY | 1 |
| 2021-05-13 03:12  | [停在原地的方案数](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) | HARD | 4 |
| 2021-05-13 02:38  | [完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | MEDIUM | 3 |
| 2021-05-13 02:30  | [比赛中的配对次数](https://leetcode-cn.com/problems/count-of-matches-in-tournament) | EASY | 3 |
| 2021-05-13 02:18  | [全排列 II](https://leetcode-cn.com/problems/permutations-ii) | MEDIUM | 3 |
| 2021-05-12 08:20  | [汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 6 |
| 2021-05-11 08:33  | [二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 |
| 2021-05-11 08:25  | [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 |
| 2021-05-11 08:16  | [二叉树剪枝](https://leetcode-cn.com/problems/binary-tree-pruning) | MEDIUM | 1 |
| 2021-05-11 08:08  | [二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree) | EASY | 1 |
| 2021-05-10 09:43  | [单值二叉树](https://leetcode-cn.com/problems/univalued-binary-tree) | EASY | 1 |
| 2021-05-10 09:23  | [叶子相似的树](https://leetcode-cn.com/problems/leaf-similar-trees) | EASY | 2 |
| 2021-05-10 09:15  | [二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof) | EASY | 2 |
| 2021-05-10 09:06  | [对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 4 |
| 2021-05-10 08:56  | [从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) | EASY | 1 |
| 2021-05-10 08:42  | [平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof) | EASY | 2 |
| 2021-05-10 08:31  | [二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 3 |
| 2021-03-29 08:12  | [唯一元素的和](https://leetcode-cn.com/problems/sum-of-unique-elements) | EASY | 2 |
| 2021-03-25 02:41  | [打印零与奇偶数](https://leetcode-cn.com/problems/print-zero-even-odd) | MEDIUM | 2 |
| 2021-03-23 08:26  | [大小为 K 的不重叠线段的数目](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments) | MEDIUM | 1 |
| 2021-03-22 08:13  | [网络信号最好的坐标](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality) | MEDIUM | 5 |
| 2021-03-22 02:54  | [删除某些元素后的数组均值](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements) | EASY | 1 |
| 2021-03-19 15:50  | [设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 3 |
| 2021-03-19 15:32  | [二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof) | EASY | 3 |
| 2020-12-18 08:42  | [找不同](https://leetcode-cn.com/problems/find-the-difference) | EASY | 6 |
| 2020-12-04 07:12  | [阶乘函数后 K 个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function) | HARD | 1 |
| 2020-12-03 15:48  | [适龄的朋友](https://leetcode-cn.com/problems/friends-of-appropriate-ages) | MEDIUM | 1 |
| 2020-12-03 15:02  | [山羊拉丁文](https://leetcode-cn.com/problems/goat-latin) | EASY | 2 |
| 2020-12-02 07:28  | [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 1 |
| 2020-11-30 16:12  | [黑白方格画](https://leetcode-cn.com/problems/ccw6C7) | EASY | 1 |
| 2020-11-26 08:42  | [两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | MEDIUM | 3 |
| 2020-11-26 06:48  | [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square) | EASY | 5 |
| 2020-11-26 06:22  | [计算各个位数不同的数字个数](https://leetcode-cn.com/problems/count-numbers-with-unique-digits) | MEDIUM | 4 |
| 2020-11-26 02:41  | [两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays) | EASY | 4 |
| 2020-11-24 06:33  | [数字范围按位与](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range) | MEDIUM | 1 |
| 2020-11-23 13:11  | [商品折扣后的最终价格](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop) | EASY | 1 |
| 2020-11-23 12:54  | [数组中的 k 个最强值](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array) | MEDIUM | 2 |
| 2020-11-23 11:52  | [重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array) | EASY | 2 |
| 2020-11-23 09:21  | [同构字符串](https://leetcode-cn.com/problems/isomorphic-strings) | EASY | 4 |
| 2020-11-23 06:39  | [计数质数](https://leetcode-cn.com/problems/count-primes) | EASY | 3 |
| 2020-11-20 09:21  | [快乐数](https://leetcode-cn.com/problems/happy-number) | EASY | 3 |
| 2020-11-20 08:12  | [二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) | MEDIUM | 4 |
| 2020-11-20 07:18  | [求众数 II](https://leetcode-cn.com/problems/majority-element-ii) | MEDIUM | 5 |
| 2020-11-20 06:25  | [汇总区间](https://leetcode-cn.com/problems/summary-ranges) | EASY | 6 |
| 2020-11-18 17:51  | [只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) | MEDIUM | 3 |
| 2020-11-18 12:35  | [分发糖果](https://leetcode-cn.com/problems/candy) | HARD | 2 |
| 2020-11-18 12:12  | [加油站](https://leetcode-cn.com/problems/gas-station) | MEDIUM | 5 |
| 2020-11-18 09:04  | [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree) | EASY | 10 |
| 2020-11-18 03:45  | [二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths) | EASY | 3 |
| 2020-11-18 02:29  | [活字印刷](https://leetcode-cn.com/problems/letter-tile-possibilities) | MEDIUM | 1 |
| 2020-11-17 07:08  | [分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | MEDIUM | 2 |
| 2020-11-16 23:46  | [距离顺序排列矩阵单元格](https://leetcode-cn.com/problems/matrix-cells-in-distance-order) | EASY | 2 |
| 2020-11-16 23:27  | [IP 地址无效化](https://leetcode-cn.com/problems/defanging-an-ip-address) | EASY | 2 |
| 2020-11-16 23:16  | [所有奇数长度子数组的和](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays) | EASY | 2 |
| 2020-11-15 01:04  | [删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci) | EASY | 2 |
| 2020-11-14 15:37  | [宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones) | EASY | 2 |
| 2020-11-14 06:38  | [最小栈](https://leetcode-cn.com/problems/min-stack) | EASY | 2 |
| 2020-11-13 15:50  | [解压缩编码列表](https://leetcode-cn.com/problems/decompress-run-length-encoded-list) | EASY | 2 |
| 2020-11-12 13:54  | [第 k 个缺失的正整数](https://leetcode-cn.com/problems/kth-missing-positive-number) | EASY | 2 |
| 2020-11-12 11:16  | [重新排列字符串](https://leetcode-cn.com/problems/shuffle-string) | EASY | 4 |
| 2020-11-12 11:05  | [换酒问题](https://leetcode-cn.com/problems/water-bottles) | EASY | 4 |
| 2020-11-12 06:51  | [验证回文串](https://leetcode-cn.com/problems/valid-palindrome) | EASY | 7 |
| 2020-11-11 14:49  | [转变日期格式](https://leetcode-cn.com/problems/reformat-date) | EASY | 5 |
| 2020-11-11 14:30  | [好数对的数目](https://leetcode-cn.com/problems/number-of-good-pairs) | EASY | 1 |
| 2020-11-11 08:44  | [Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title) | EASY | 7 |
| 2020-11-11 07:30  | [x 的平方根](https://leetcode-cn.com/problems/sqrtx) | EASY | 10 |
| 2020-11-11 03:53  | [阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes) | EASY | 4 |
| 2020-11-11 03:37  | [Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion) | MEDIUM | 8 |
| 2020-11-10 03:12  | [下一个排列](https://leetcode-cn.com/problems/next-permutation) | MEDIUM | 3 |
| 2020-11-09 15:25  | [包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof) | EASY | 2 |
| 2020-11-09 15:09  | [左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof) | EASY | 2 |
| 2020-11-09 15:06  | [拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) | EASY | 3 |
| 2020-11-09 14:51  | [一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | EASY | 4 |
| 2020-11-09 06:10  | [最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin) | MEDIUM | 8 |
| 2020-11-06 08:47  | [除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | MEDIUM | 8 |
| 2020-11-06 08:13  | [根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits) | EASY | 1 |
| 2020-11-06 07:36  | [猜数字](https://leetcode-cn.com/problems/guess-numbers) | EASY | 1 |
| 2020-11-06 07:33  | [特殊数组的特征值](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x) | EASY | 1 |
| 2020-11-06 04:57  | [警告一小时内使用相同员工卡大于等于三次的人](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period) | MEDIUM | 6 |
| 2020-11-05 08:30  | [两个相同字符之间的最长子字符串](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters) | EASY | 3 |
| 2020-11-05 02:38  | [拿硬币](https://leetcode-cn.com/problems/na-ying-bi) | EASY | 3 |
| 2020-11-04 15:40  | [插入区间](https://leetcode-cn.com/problems/insert-interval) | MEDIUM | 1 |
| 2020-11-04 15:09  | [重新排列日志文件](https://leetcode-cn.com/problems/reorder-data-in-log-files) | EASY | 1 |
| 2020-11-04 14:58  | [增减字符串匹配](https://leetcode-cn.com/problems/di-string-match) | EASY | 2 |
| 2020-11-04 09:18  | [括号的最大嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses) | EASY | 2 |
| 2020-11-03 14:57  | [有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array) | EASY | 3 |
| 2020-11-02 15:56  | [加一](https://leetcode-cn.com/problems/plus-one) | EASY | 2 |
| 2020-11-02 15:33  | [最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | EASY | 2 |
| 2020-11-02 07:45  | [各位相加](https://leetcode-cn.com/problems/add-digits) | EASY | 2 |
| 2020-11-02 07:37  | [最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | MEDIUM | 1 |
| 2020-10-31 02:29  | [O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed) | HARD | 8 |
| 2020-10-30 08:08  | [岛屿的周长](https://leetcode-cn.com/problems/island-perimeter) | EASY | 2 |
| 2020-10-29 13:53  | [正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | HARD | 1 |
| 2020-10-29 13:23  | [寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | HARD | 5 |
| 2020-10-29 12:25  | [判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci) | EASY | 4 |
| 2020-10-29 11:00  | [求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 4 |
| 2020-10-28 11:19  | [独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences) | EASY | 3 |
| 2020-09-09 15:21  | [接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | HARD | 1 |
| 2020-09-09 15:00  | [缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive) | HARD | 2 |
| 2020-09-09 14:02  | [组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii) | MEDIUM | 2 |
| 2020-09-09 13:34  | [组合总和](https://leetcode-cn.com/problems/combination-sum) | MEDIUM | 1 |
| 2020-09-09 13:18  | [判定是否互为字符重排](https://leetcode-cn.com/problems/check-permutation-lcci) | EASY | 3 |
| 2020-08-16 12:43  | [找出数组游戏的赢家](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game) | MEDIUM | 1 |
| 2020-08-16 10:42  | [统计好三元组](https://leetcode-cn.com/problems/count-good-triplets) | EASY | 1 |
| 2020-08-16 10:33  | [数字转换为十六进制数](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal) | EASY | 6 |
| 2020-07-30 16:18  | [按序打印](https://leetcode-cn.com/problems/print-in-order) | EASY | 7 |
| 2020-07-30 15:49  | [重新格式化部门表](https://leetcode-cn.com/problems/reformat-department-table) | EASY | 2 |
| 2019-04-06 15:23  | [数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | EASY | 5 |
| 2019-04-06 15:13  | [字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | MEDIUM | 5 |
| 2019-04-06 12:17  | [转置文件](https://leetcode-cn.com/problems/transpose-file) | MEDIUM | 1 |
| 2018-09-28 07:47  | [构造矩形](https://leetcode-cn.com/problems/construct-the-rectangle) | EASY | 1 |
| 2018-09-26 13:47  | [O(1) 时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) | MEDIUM | 1 |
| 2018-09-26 13:35  | [数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | MEDIUM | 1 |
| 2018-09-26 13:34  | [第三大的数](https://leetcode-cn.com/problems/third-maximum-number) | EASY | 1 |
| 2018-09-21 08:24  | [二进制求和](https://leetcode-cn.com/problems/add-binary) | EASY | 1 |
| 2018-08-31 07:01  | [区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable) | MEDIUM | 1 |
| 2018-08-31 06:57  | [区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable) | EASY | 1 |
| 2018-08-31 06:41  | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n) | MEDIUM | 6 |
| 2018-08-29 10:23  | [压缩字符串](https://leetcode-cn.com/problems/string-compression) | MEDIUM | 2 |
| 2018-08-29 09:33  | [外观数列](https://leetcode-cn.com/problems/count-and-say) | MEDIUM | 14 |
| 2018-08-29 07:48  | [实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 4 |
| 2018-08-29 07:38  | [删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 5 |
| 2018-08-28 09:12  | [移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 5 |
| 2018-08-27 08:44  | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 7 |
| 2018-08-27 08:21  | [二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | MEDIUM | 1 |
| 2018-08-27 08:11  | [二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) | EASY | 3 |
| 2018-08-27 03:01  | [唯一摩尔斯密码词](https://leetcode-cn.com/problems/unique-morse-code-words) | EASY | 1 |
| 2018-08-25 02:48  | [错误的集合](https://leetcode-cn.com/problems/set-mismatch) | EASY | 11 |
| 2018-08-24 13:52  | [N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal) | EASY | 3 |
| 2018-08-23 17:45  | [相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 |
| 2018-08-23 17:33  | [最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | EASY | 1 |
| 2018-08-22 12:23  | [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 7 |
| 2018-08-22 08:28  | [行程和用户](https://leetcode-cn.com/problems/trips-and-users) | HARD | 1 |
| 2018-08-22 08:13  | [体育馆的人流量](https://leetcode-cn.com/problems/human-traffic-of-stadium) | HARD | 2 |
| 2018-08-22 08:07  | [第N高的薪水](https://leetcode-cn.com/problems/nth-highest-salary) | MEDIUM | 4 |
| 2018-08-22 07:53  | [连续出现的数字](https://leetcode-cn.com/problems/consecutive-numbers) | MEDIUM | 3 |
| 2018-08-22 07:32  | [部门工资前三高的所有员工](https://leetcode-cn.com/problems/department-top-three-salaries) | HARD | 1 |
| 2018-08-22 07:24  | [删除重复的电子邮箱](https://leetcode-cn.com/problems/delete-duplicate-emails) | EASY | 3 |
| 2018-08-22 07:12  | [换座位](https://leetcode-cn.com/problems/exchange-seats) | MEDIUM | 1 |
| 2018-08-22 06:55  | [部门工资最高的员工](https://leetcode-cn.com/problems/department-highest-salary) | MEDIUM | 9 |
| 2018-08-22 06:49  | [分数排名](https://leetcode-cn.com/problems/rank-scores) | MEDIUM | 1 |
| 2018-08-22 06:22  | [回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 1 |
| 2018-08-22 06:17  | [整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 3 |
| 2018-08-22 04:27  | [上升的温度](https://leetcode-cn.com/problems/rising-temperature) | EASY | 1 |
| 2018-08-22 03:52  | [从不订购的客户](https://leetcode-cn.com/problems/customers-who-never-order) | EASY | 3 |
| 2018-08-22 03:44  | [查找重复的电子邮箱](https://leetcode-cn.com/problems/duplicate-emails) | EASY | 1 |
| 2018-08-22 03:41  | [超过经理收入的员工](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers) | EASY | 2 |
| 2018-08-22 03:35  | [超过5名学生的课](https://leetcode-cn.com/problems/classes-more-than-5-students) | EASY | 2 |
| 2018-08-22 03:24  | [大的国家](https://leetcode-cn.com/problems/big-countries) | EASY | 2 |
| 2018-08-22 03:20  | [第二高的薪水](https://leetcode-cn.com/problems/second-highest-salary) | EASY | 4 |
| 2018-08-22 03:00  | [变更性别](https://leetcode-cn.com/problems/swap-salary) | EASY | 2 |
| 2018-08-22 02:52  | [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change) | EASY | 1 |
| 2018-08-21 16:03  | [有趣的电影](https://leetcode-cn.com/problems/not-boring-movies) | EASY | 3 |
| 2018-08-21 11:24  | [组合两个表](https://leetcode-cn.com/problems/combine-two-tables) | EASY | 1 |
| 2018-08-21 11:05  | [统计词频](https://leetcode-cn.com/problems/word-frequency) | MEDIUM | 1 |
| 2018-08-21 10:59  | [有效电话号码](https://leetcode-cn.com/problems/valid-phone-numbers) | EASY | 8 |
| 2018-08-21 10:36  | [第十行](https://leetcode-cn.com/problems/tenth-line) | EASY | 12 |
