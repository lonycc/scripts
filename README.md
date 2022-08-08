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

> 总提交次数: 1994, 总通过次数: 1361, 已通过题数: 830

> 已通过题目的难度和数量: EASY = 600, MEDIUM = 209, HARD = 21, 

| 最近提交时间 | 题目 | 题目难度 | 提交次数 |
| ---- | ---- | ---- | ---- |
| 2022-08-05 07:39  | [剑指 Offer II 080. 含有 k 个元素的组合](https://leetcode-cn.com/problems/uUsW3B) | MEDIUM | 1 |
| 2022-08-05 07:36  | [2352. 相等行列对](https://leetcode-cn.com/problems/equal-row-and-column-pairs) | MEDIUM | 3 |
| 2022-08-05 07:19  | [面试题13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof) | MEDIUM | 2 |
| 2022-08-05 07:13  | [2358. 分组的最大数量](https://leetcode-cn.com/problems/maximum-number-of-groups-entering-a-competition) | MEDIUM | 1 |
| 2022-08-05 07:04  | [836. 矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap) | EASY | 2 |
| 2022-08-05 07:02  | [1260. 二维网格迁移](https://leetcode-cn.com/problems/shift-2d-grid) | EASY | 1 |
| 2022-08-05 07:01  | [2347. 最好的扑克手牌](https://leetcode-cn.com/problems/best-poker-hand) | EASY | 2 |
| 2022-08-05 06:55  | [2357. 使数组中所有元素都等于零](https://leetcode-cn.com/problems/make-array-zero-by-subtracting-equal-amounts) | EASY | 1 |
| 2022-08-05 06:52  | [2351. 第一个出现两次的字母](https://leetcode-cn.com/problems/first-letter-to-appear-twice) | EASY | 2 |
| 2022-08-05 02:18  | [623. 在二叉树中增加一行](https://leetcode-cn.com/problems/add-one-row-to-tree) | MEDIUM | 2 |
| 2022-08-05 02:15  | [175. 组合两个表](https://leetcode-cn.com/problems/combine-two-tables) | EASY | 3 |
| 2022-08-05 02:14  | [1581. 进店却未进行过交易的顾客](https://leetcode-cn.com/problems/customer-who-visited-but-did-not-make-any-transactions) | EASY | 4 |
| 2022-08-05 02:14  | [1148. 文章浏览 I](https://leetcode-cn.com/problems/article-views-i) | EASY | 3 |
| 2022-08-04 09:14  | [1965. 丢失信息的雇员](https://leetcode-cn.com/problems/employees-with-missing-information) | EASY | 3 |
| 2022-08-04 09:13  | [1795. 每个产品在不同商店的价格](https://leetcode-cn.com/problems/rearrange-products-table) | EASY | 3 |
| 2022-08-04 09:13  | [608. 树节点](https://leetcode-cn.com/problems/tree-node) | MEDIUM | 3 |
| 2022-08-04 09:12  | [176. 第二高的薪水](https://leetcode-cn.com/problems/second-highest-salary) | MEDIUM | 7 |
| 2022-08-03 02:30  | [1667. 修复表中的名字](https://leetcode-cn.com/problems/fix-names-in-a-table) | EASY | 4 |
| 2022-08-03 02:29  | [1484. 按日期分组销售产品](https://leetcode-cn.com/problems/group-sold-products-by-the-date) | EASY | 3 |
| 2022-08-03 02:28  | [1527. 患某种疾病的患者](https://leetcode-cn.com/problems/patients-with-a-condition) | EASY | 3 |
| 2022-08-02 07:58  | [2335. 装满杯子需要的最短总时长](https://leetcode-cn.com/problems/minimum-amount-of-time-to-fill-cups) | EASY | 1 |
| 2022-08-02 07:55  | [2341. 数组能形成多少数对](https://leetcode-cn.com/problems/maximum-number-of-pairs-in-array) | EASY | 2 |
| 2022-08-02 07:46  | [54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix) | MEDIUM | 3 |
| 2022-08-02 07:44  | [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest) | MEDIUM | 1 |
| 2022-08-02 07:42  | [15. 三数之和](https://leetcode-cn.com/problems/3sum) | MEDIUM | 1 |
| 2022-08-02 07:40  | [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array) | MEDIUM | 1 |
| 2022-08-02 07:39  | [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum) | HARD | 1 |
| 2022-08-02 07:37  | [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree) | MEDIUM | 4 |
| 2022-08-02 07:32  | [148. 排序链表](https://leetcode-cn.com/problems/sort-list) | MEDIUM | 2 |
| 2022-08-02 07:30  | [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists) | HARD | 3 |
| 2022-08-02 07:28  | [61. 旋转链表](https://leetcode-cn.com/problems/rotate-list) | MEDIUM | 1 |
| 2022-08-02 07:26  | [89. 格雷编码](https://leetcode-cn.com/problems/gray-code) | MEDIUM | 2 |
| 2022-08-02 07:24  | [146. LRU 缓存](https://leetcode-cn.com/problems/lru-cache) | MEDIUM | 1 |
| 2022-08-02 07:14  | [167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted) | MEDIUM | 14 |
| 2022-08-02 07:14  | [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 4 |
| 2022-08-02 07:11  | [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | MEDIUM | 4 |
| 2022-08-02 07:06  | [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors) | MEDIUM | 3 |
| 2022-08-02 07:03  | [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum) | MEDIUM | 3 |
| 2022-08-02 06:54  | [80. 删除有序数组中的重复项 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii) | MEDIUM | 3 |
| 2022-08-02 06:44  | [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 6 |
| 2022-08-02 06:41  | [27. 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 6 |
| 2022-08-02 06:38  | [283. 移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 8 |
| 2022-08-02 06:35  | [559. N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree) | EASY | 3 |
| 2022-08-02 06:32  | [429. N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal) | MEDIUM | 2 |
| 2022-08-02 06:28  | [590. N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal) | EASY | 4 |
| 2022-08-02 06:24  | [589. N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal) | EASY | 5 |
| 2022-08-02 06:19  | [1873. 计算特殊奖金](https://leetcode-cn.com/problems/calculate-special-bonus) | EASY | 4 |
| 2022-08-02 06:18  | [627. 变更性别](https://leetcode-cn.com/problems/swap-salary) | EASY | 5 |
| 2022-08-02 06:18  | [196. 删除重复的电子邮箱](https://leetcode-cn.com/problems/delete-duplicate-emails) | EASY | 5 |
| 2022-08-02 06:16  | [622. 设计循环队列](https://leetcode-cn.com/problems/design-circular-queue) | MEDIUM | 2 |
| 2022-08-01 03:24  | [595. 大的国家](https://leetcode-cn.com/problems/big-countries) | EASY | 5 |
| 2022-08-01 03:22  | [1757. 可回收且低脂的产品](https://leetcode-cn.com/problems/recyclable-and-low-fat-products) | EASY | 3 |
| 2022-08-01 03:21  | [584. 寻找用户推荐人](https://leetcode-cn.com/problems/find-customer-referee) | EASY | 4 |
| 2022-08-01 03:20  | [183. 从不订购的客户](https://leetcode-cn.com/problems/customers-who-never-order) | EASY | 5 |
| 2022-08-01 03:11  | [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder) | HARD | 2 |
| 2022-08-01 03:09  | [1129. 颜色交替的最短路径](https://leetcode-cn.com/problems/shortest-path-with-alternating-colors) | MEDIUM | 1 |
| 2022-08-01 03:07  | [1654. 到家的最少跳跃次数](https://leetcode-cn.com/problems/minimum-jumps-to-reach-home) | MEDIUM | 2 |
| 2022-08-01 03:05  | [365. 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem) | MEDIUM | 2 |
| 2022-08-01 03:03  | [1466. 重新规划路线](https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero) | MEDIUM | 2 |
| 2022-08-01 03:00  | [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition) | MEDIUM | 1 |
| 2022-08-01 02:59  | [785. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite) | MEDIUM | 2 |
| 2022-08-01 02:58  | [752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock) | MEDIUM | 2 |
| 2022-08-01 02:55  | [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation) | MEDIUM | 2 |
| 2022-08-01 02:54  | [1306. 跳跃游戏 III](https://leetcode-cn.com/problems/jump-game-iii) | MEDIUM | 1 |
| 2022-08-01 02:53  | [1615. 最大网络秩](https://leetcode-cn.com/problems/maximal-network-rank) | MEDIUM | 2 |
| 2022-08-01 02:51  | [847. 访问所有节点的最短路径](https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes) | HARD | 2 |
| 2022-08-01 02:49  | [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix) | MEDIUM | 2 |
| 2022-08-01 02:48  | [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix) | MEDIUM | 1 |
| 2022-08-01 02:42  | [934. 最短的桥](https://leetcode-cn.com/problems/shortest-bridge) | MEDIUM | 3 |
| 2022-08-01 02:39  | [1926. 迷宫中离入口最近的出口](https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze) | MEDIUM | 1 |
| 2022-08-01 02:37  | [1376. 通知所有员工所需的时间](https://leetcode-cn.com/problems/time-needed-to-inform-all-employees) | MEDIUM | 5 |
| 2022-08-01 02:33  | [802. 找到最终的安全状态](https://leetcode-cn.com/problems/find-eventual-safe-states) | MEDIUM | 2 |
| 2022-08-01 02:31  | [1557. 可以到达所有点的最少点数目](https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes) | MEDIUM | 1 |
| 2022-08-01 02:29  | [1319. 连通网络的操作次数](https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected) | MEDIUM | 2 |
| 2022-08-01 02:26  | [547. 省份数量](https://leetcode-cn.com/problems/number-of-provinces) | MEDIUM | 2 |
| 2022-08-01 02:23  | [841. 钥匙和房间](https://leetcode-cn.com/problems/keys-and-rooms) | MEDIUM | 2 |
| 2022-08-01 02:10  | [797. 所有可能的路径](https://leetcode-cn.com/problems/all-paths-from-source-to-target) | MEDIUM | 1 |
| 2022-08-01 02:06  | [997. 找到小镇的法官](https://leetcode-cn.com/problems/find-the-town-judge) | EASY | 3 |
| 2022-08-01 01:55  | [1374. 生成每种字符都是奇数个的字符串](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts) | EASY | 3 |
| 2022-07-28 07:38  | [1331. 数组序号转换](https://leetcode-cn.com/problems/rank-transform-of-an-array) | EASY | 2 |
| 2022-07-28 07:35  | [1622. 奇妙序列](https://leetcode-cn.com/problems/fancy-sequence) | HARD | 13 |
| 2022-07-28 07:32  | [914. 卡牌分组](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards) | EASY | 18 |
| 2022-07-28 07:30  | [60. 排列序列](https://leetcode-cn.com/problems/permutation-sequence) | HARD | 2 |
| 2022-07-28 07:29  | [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words) | HARD | 4 |
| 2022-07-28 07:28  | [18. 四数之和](https://leetcode-cn.com/problems/4sum) | MEDIUM | 3 |
| 2022-07-28 07:26  | [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow) | MEDIUM | 2 |
| 2022-07-28 07:23  | [1162. 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible) | MEDIUM | 1 |
| 2022-07-28 07:21  | [1905. 统计子岛屿](https://leetcode-cn.com/problems/count-sub-islands) | MEDIUM | 1 |
| 2022-07-28 07:20  | [1020. 飞地的数量](https://leetcode-cn.com/problems/number-of-enclaves) | MEDIUM | 2 |
| 2022-07-28 07:03  | [2331. 计算布尔二叉树的值](https://leetcode-cn.com/problems/evaluate-boolean-binary-tree) | EASY | 3 |
| 2022-07-25 09:56  | [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring) | MEDIUM | 2 |
| 2022-07-25 09:32  | [1. 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 14 |
| 2022-07-25 06:21  | [1312. 让字符串成为回文串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome) | HARD | 1 |
| 2022-07-22 09:58  | [剑指 Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | EASY | 2 |
| 2022-07-22 09:57  | [812. 最大三角形面积](https://leetcode-cn.com/problems/largest-triangle-area) | EASY | 2 |
| 2022-07-22 02:11  | [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements) | MEDIUM | 1 |
| 2022-07-21 02:29  | [692. 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words) | MEDIUM | 2 |
| 2022-07-21 02:18  | [1046. 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight) | EASY | 3 |
| 2022-07-20 02:35  | [1254. 统计封闭岛屿的数目](https://leetcode-cn.com/problems/number-of-closed-islands) | MEDIUM | 1 |
| 2022-07-20 02:28  | [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands) | MEDIUM | 2 |
| 2022-07-20 02:28  | [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island) | MEDIUM | 2 |
| 2022-07-20 02:13  | [394. 字符串解码](https://leetcode-cn.com/problems/decode-string) | MEDIUM | 1 |
| 2022-07-20 02:01  | [844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare) | EASY | 4 |
| 2022-07-19 08:36  | [733. 图像渲染](https://leetcode-cn.com/problems/flood-fill) | EASY | 4 |
| 2022-07-19 06:57  | [299. 猜数字游戏](https://leetcode-cn.com/problems/bulls-and-cows) | MEDIUM | 1 |
| 2022-07-18 03:40  | [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string) | MEDIUM | 1 |
| 2022-07-18 03:06  | [424. 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement) | MEDIUM | 1 |
| 2022-07-18 02:33  | [62. 不同路径](https://leetcode-cn.com/problems/unique-paths) | MEDIUM | 2 |
| 2022-07-18 02:24  | [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | EASY | 6 |
| 2022-07-18 02:22  | [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 8 |
| 2022-07-18 02:16  | [746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) | EASY | 3 |
| 2022-07-14 06:21  | [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | MEDIUM | 6 |
| 2022-07-14 02:38  | [235. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree) | EASY | 5 |
| 2022-07-13 02:53  | [278. 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | EASY | 13 |
| 2022-07-13 02:48  | [704. 二分查找](https://leetcode-cn.com/problems/binary-search) | EASY | 7 |
| 2022-07-12 09:30  | [274. H 指数](https://leetcode-cn.com/problems/h-index) | MEDIUM | 3 |
| 2022-07-12 09:00  | [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) | MEDIUM | 1 |
| 2022-07-12 02:07  | [1252. 奇数值单元格的数目](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix) | EASY | 2 |
| 2022-07-12 02:03  | [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 4 |
| 2022-07-11 02:38  | [409. 最长回文串](https://leetcode-cn.com/problems/longest-palindrome) | EASY | 3 |
| 2022-07-11 02:28  | [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 6 |
| 2022-07-10 15:15  | [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | MEDIUM | 2 |
| 2022-07-10 15:13  | [876. 链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list) | EASY | 3 |
| 2022-07-09 06:05  | [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 10 |
| 2022-07-09 06:02  | [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 6 |
| 2022-07-08 08:51  | [1217. 玩筹码](https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position) | EASY | 2 |
| 2022-07-08 02:21  | [392. 判断子序列](https://leetcode-cn.com/problems/is-subsequence) | EASY | 9 |
| 2022-07-08 02:19  | [205. 同构字符串](https://leetcode-cn.com/problems/isomorphic-strings) | EASY | 8 |
| 2022-07-07 06:38  | [724. 寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index) | EASY | 3 |
| 2022-07-07 06:32  | [1480. 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | EASY | 6 |
| 2022-07-06 06:52  | [2319. 判断矩阵是否是一个 X 矩阵](https://leetcode-cn.com/problems/check-if-matrix-is-x-matrix) | EASY | 1 |
| 2022-07-06 06:30  | [720. 词典中最长的单词](https://leetcode-cn.com/problems/longest-word-in-dictionary) | MEDIUM | 1 |
| 2022-07-06 06:23  | [1971. 寻找图中是否存在路径](https://leetcode-cn.com/problems/find-if-path-exists-in-graph) | EASY | 1 |
| 2022-07-06 03:25  | [2047. 句子中的有效单词数](https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence) | EASY | 1 |
| 2022-07-06 03:16  | [2325. 解密消息](https://leetcode-cn.com/problems/decode-the-message) | EASY | 1 |
| 2022-06-30 03:54  | [2315. 统计星号](https://leetcode-cn.com/problems/count-asterisks) | EASY | 1 |
| 2022-06-30 03:39  | [1175. 质数排列](https://leetcode-cn.com/problems/prime-arrangements) | EASY | 2 |
| 2022-06-21 03:53  | [59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii) | MEDIUM | 1 |
| 2022-06-21 02:11  | [1108. IP 地址无效化](https://leetcode-cn.com/problems/defanging-an-ip-address) | EASY | 3 |
| 2022-06-20 02:26  | [2309. 兼具大小写的最好英文字母](https://leetcode-cn.com/problems/greatest-english-letter-in-upper-and-lower-case) | EASY | 1 |
| 2022-06-15 03:00  | [1275. 找出井字棋的获胜者](https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game) | EASY | 1 |
| 2022-06-15 02:48  | [498. 对角线遍历](https://leetcode-cn.com/problems/diagonal-traverse) | MEDIUM | 2 |
| 2022-06-14 09:53  | [LCP 51. 烹饪料理](https://leetcode-cn.com/problems/UEcfPD) | EASY | 1 |
| 2022-06-14 09:49  | [2303. 计算应缴税款总额](https://leetcode-cn.com/problems/calculate-amount-paid-in-taxes) | EASY | 1 |
| 2022-06-14 07:48  | [2299. 强密码检验器 II](https://leetcode-cn.com/problems/strong-password-checker-ii) | EASY | 1 |
| 2022-06-14 07:35  | [2062. 统计字符串中的元音子字符串](https://leetcode-cn.com/problems/count-vowel-substrings-of-a-string) | EASY | 1 |
| 2022-06-13 07:28  | [1051. 高度检查器](https://leetcode-cn.com/problems/height-checker) | EASY | 2 |
| 2022-06-06 07:27  | [剑指 Offer II 019. 最多删除一个字符得到回文](https://leetcode-cn.com/problems/RQku0D) | EASY | 1 |
| 2022-06-06 07:22  | [2259. 移除指定数字得到的最大结果](https://leetcode-cn.com/problems/remove-digit-from-number-to-maximize-result) | EASY | 2 |
| 2022-06-06 06:55  | [2293. 极大极小游戏](https://leetcode-cn.com/problems/min-max-game) | EASY | 1 |
| 2022-06-06 02:24  | [1158. 市场分析 I](https://leetcode-cn.com/problems/market-analysis-i) | MEDIUM | 2 |
| 2022-06-06 02:23  | [1407. 排名靠前的旅行者](https://leetcode-cn.com/problems/top-travellers) | EASY | 2 |
| 2022-06-06 02:23  | [1393. 股票的资本损益](https://leetcode-cn.com/problems/capital-gainloss) | MEDIUM | 2 |
| 2022-06-06 02:23  | [1741. 查找每个员工花费的总时间](https://leetcode-cn.com/problems/find-total-time-spent-by-each-employee) | EASY | 2 |
| 2022-06-06 02:23  | [1890. 2020年最后一次登录](https://leetcode-cn.com/problems/the-latest-login-in-2020) | EASY | 3 |
| 2022-06-06 02:22  | [511. 游戏玩法分析 I](https://leetcode-cn.com/problems/game-play-analysis-i) | EASY | 2 |
| 2022-06-06 02:22  | [586. 订单最多的客户](https://leetcode-cn.com/problems/customer-placing-the-largest-number-of-orders) | EASY | 2 |
| 2022-06-06 02:22  | [1729. 求关注者的数量](https://leetcode-cn.com/problems/find-followers-count) | EASY | 3 |
| 2022-06-06 02:21  | [1693. 每天的领导和合伙人](https://leetcode-cn.com/problems/daily-leads-and-partners) | EASY | 2 |
| 2022-06-06 02:21  | [1141. 查询近30天活跃用户数](https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i) | EASY | 2 |
| 2022-06-06 02:20  | [607. 销售员](https://leetcode-cn.com/problems/sales-person) | EASY | 3 |
| 2022-06-06 02:18  | [197. 上升的温度](https://leetcode-cn.com/problems/rising-temperature) | EASY | 2 |
| 2022-06-02 09:20  | [2099. 找到和最大的长度为 K 的子序列](https://leetcode-cn.com/problems/find-subsequence-of-length-k-with-the-largest-sum) | EASY | 2 |
| 2022-06-02 09:13  | [2133. 检查是否每一行每一列都包含全部整数](https://leetcode-cn.com/problems/check-if-every-row-and-column-contains-all-numbers) | EASY | 1 |
| 2022-06-02 09:06  | [345. 反转字符串中的元音字母](https://leetcode-cn.com/problems/reverse-vowels-of-a-string) | EASY | 1 |
| 2022-06-02 09:02  | [606. 根据二叉树创建字符串](https://leetcode-cn.com/problems/construct-string-from-binary-tree) | EASY | 1 |
| 2022-06-02 08:56  | [748. 最短补全词](https://leetcode-cn.com/problems/shortest-completing-word) | EASY | 1 |
| 2022-06-02 08:01  | [2273. 移除字母异位词后的结果数组](https://leetcode-cn.com/problems/find-resultant-array-after-removing-anagrams) | EASY | 1 |
| 2022-06-02 07:52  | [剑指 Offer II 018. 有效的回文](https://leetcode-cn.com/problems/XltzEq) | EASY | 3 |
| 2022-06-02 07:36  | [剑指 Offer II 034. 外星语言是否排序](https://leetcode-cn.com/problems/lwyVBB) | EASY | 1 |
| 2022-06-02 07:36  | [953. 验证外星语词典](https://leetcode-cn.com/problems/verifying-an-alien-dictionary) | EASY | 1 |
| 2022-06-02 03:02  | [2103. 环和杆](https://leetcode-cn.com/problems/rings-and-rods) | EASY | 1 |
| 2022-06-02 02:50  | [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst) | MEDIUM | 1 |
| 2022-06-01 02:38  | [473. 火柴拼正方形](https://leetcode-cn.com/problems/matchsticks-to-square) | MEDIUM | 1 |
| 2022-05-31 09:49  | [2220. 转换数字的最少位翻转次数](https://leetcode-cn.com/problems/minimum-bit-flips-to-convert-number) | EASY | 1 |
| 2022-05-31 09:43  | [2037. 使每位学生都有座位的最少移动次数](https://leetcode-cn.com/problems/minimum-number-of-moves-to-seat-everyone) | EASY | 2 |
| 2022-05-31 09:36  | [2190. 数组中紧跟 key 之后出现最频繁的数字](https://leetcode-cn.com/problems/most-frequent-number-following-key-in-an-array) | EASY | 3 |
| 2022-05-31 09:23  | [2210. 统计数组中峰和谷的数量](https://leetcode-cn.com/problems/count-hills-and-valleys-in-an-array) | EASY | 1 |
| 2022-05-31 09:13  | [2200. 找出数组中的所有 K 近邻下标](https://leetcode-cn.com/problems/find-all-k-distant-indices-in-an-array) | EASY | 1 |
| 2022-05-31 07:55  | [2231. 按奇偶性交换后的最大数字](https://leetcode-cn.com/problems/largest-number-after-digit-swaps-by-parity) | EASY | 1 |
| 2022-05-31 07:39  | [2148. 元素计数](https://leetcode-cn.com/problems/count-elements-with-strictly-smaller-and-greater-elements) | EASY | 1 |
| 2022-05-31 07:27  | [2287. 重排字符形成目标字符串](https://leetcode-cn.com/problems/rearrange-characters-to-make-target-string) | EASY | 2 |
| 2022-05-31 07:16  | [2027. 转换字符串的最少操作次数](https://leetcode-cn.com/problems/minimum-moves-to-convert-string) | EASY | 1 |
| 2022-05-31 07:09  | [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses) | MEDIUM | 1 |
| 2022-05-30 14:34  | [2073. 买票需要的时间](https://leetcode-cn.com/problems/time-needed-to-buy-tickets) | EASY | 1 |
| 2022-05-30 09:39  | [2016. 增量元素之间的最大差值](https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements) | EASY | 1 |
| 2022-05-30 09:10  | [2180. 统计各位数字之和为偶数的整数个数](https://leetcode-cn.com/problems/count-integers-with-even-digit-sum) | EASY | 2 |
| 2022-05-30 09:07  | [2078. 两栋颜色不同且距离最远的房子](https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors) | EASY | 1 |
| 2022-05-30 09:02  | [2094. 找出 3 位偶数](https://leetcode-cn.com/problems/finding-3-digit-even-numbers) | EASY | 3 |
| 2022-05-30 07:21  | [2032. 至少在两个数组中出现的值](https://leetcode-cn.com/problems/two-out-of-three) | EASY | 1 |
| 2022-05-30 06:38  | [2283. 判断一个数的数字计数是否等于数位的值](https://leetcode-cn.com/problems/check-if-number-has-equal-digit-count-and-digit-value) | EASY | 1 |
| 2022-05-30 06:30  | [2119. 反转两次的数字](https://leetcode-cn.com/problems/a-number-after-a-double-reversal) | EASY | 2 |
| 2022-05-30 06:21  | [剑指 Offer II 032. 有效的变位词](https://leetcode-cn.com/problems/dKk3P7) | EASY | 2 |
| 2022-05-30 06:14  | [2138. 将字符串拆分为若干长度为 k 的组](https://leetcode-cn.com/problems/divide-a-string-into-groups-of-size-k) | EASY | 4 |
| 2022-05-30 03:24  | [2042. 检查句子中的数字是否递增](https://leetcode-cn.com/problems/check-if-numbers-are-ascending-in-a-sentence) | EASY | 1 |
| 2022-05-30 03:21  | [1995. 统计特殊四元组](https://leetcode-cn.com/problems/count-special-quadruplets) | EASY | 1 |
| 2022-05-30 03:14  | [2236. 判断根结点是否等于子结点之和](https://leetcode-cn.com/problems/root-equals-sum-of-children) | EASY | 1 |
| 2022-05-30 03:08  | [2108. 找出数组中的第一个回文字符串](https://leetcode-cn.com/problems/find-first-palindromic-string-in-the-array) | EASY | 1 |
| 2022-05-30 03:07  | [2129. 将标题首字母大写](https://leetcode-cn.com/problems/capitalize-the-title) | EASY | 1 |
| 2022-05-30 03:02  | [2185. 统计包含给定前缀的字符串](https://leetcode-cn.com/problems/counting-words-with-a-given-prefix) | EASY | 1 |
| 2022-05-30 02:59  | [1022. 从根到叶的二进制数之和](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers) | EASY | 4 |
| 2022-05-30 02:45  | [2164. 对奇偶下标分别排序](https://leetcode-cn.com/problems/sort-even-and-odd-indices-independently) | EASY | 1 |
| 2022-05-30 02:33  | [2224. 转化时间需要的最少操作数](https://leetcode-cn.com/problems/minimum-number-of-operations-to-convert-time) | EASY | 1 |
| 2022-05-30 02:13  | [2053. 数组中第 K 个独一无二的字符串](https://leetcode-cn.com/problems/kth-distinct-string-in-an-array) | EASY | 1 |
| 2022-05-28 15:14  | [2124. 检查是否所有 A 都在 B 之前](https://leetcode-cn.com/problems/check-if-all-as-appears-before-all-bs) | EASY | 2 |
| 2022-05-28 15:04  | [2114. 句子中的最多单词数](https://leetcode-cn.com/problems/maximum-number-of-words-found-in-sentences) | EASY | 1 |
| 2022-05-28 15:02  | [2144. 打折购买糖果的最小开销](https://leetcode-cn.com/problems/minimum-cost-of-buying-candies-with-discount) | EASY | 2 |
| 2022-05-28 14:53  | [2022. 将一维数组转变成二维数组](https://leetcode-cn.com/problems/convert-1d-array-into-2d-array) | EASY | 1 |
| 2022-05-28 14:46  | [2089. 找出数组排序后的目标下标](https://leetcode-cn.com/problems/find-target-indices-after-sorting-array) | EASY | 2 |
| 2022-05-28 14:39  | [2085. 统计出现过一次的公共字符串](https://leetcode-cn.com/problems/count-common-words-with-one-occurrence) | EASY | 2 |
| 2022-05-28 14:08  | [2243. 计算字符串的数字和](https://leetcode-cn.com/problems/calculate-digit-sum-of-a-string) | EASY | 1 |
| 2022-05-28 11:47  | [2057. 值相等的最小索引](https://leetcode-cn.com/problems/smallest-index-with-equal-value) | EASY | 1 |
| 2022-05-28 11:44  | [2239. 找到最接近 0 的数字](https://leetcode-cn.com/problems/find-closest-number-to-zero) | EASY | 2 |
| 2022-05-28 11:28  | [2068. 检查两个字符串是否几乎相等](https://leetcode-cn.com/problems/check-whether-two-strings-are-almost-equivalent) | EASY | 1 |
| 2022-05-28 03:21  | [1021. 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses) | EASY | 2 |
| 2022-05-27 07:51  | [2215. 找出两数组的不同](https://leetcode-cn.com/problems/find-the-difference-of-two-arrays) | EASY | 2 |
| 2022-05-27 07:47  | [2206. 将数组划分成相等数对](https://leetcode-cn.com/problems/divide-array-into-equal-pairs) | EASY | 1 |
| 2022-05-27 07:44  | [2248. 多个数组求交集](https://leetcode-cn.com/problems/intersection-of-multiple-arrays) | EASY | 1 |
| 2022-05-27 07:38  | [剑指 Offer II 006. 排序数组中两个数字之和](https://leetcode-cn.com/problems/kLl5u1) | EASY | 2 |
| 2022-05-27 07:36  | [剑指 Offer II 041. 滑动窗口的平均值](https://leetcode-cn.com/problems/qIsx9U) | EASY | 1 |
| 2022-05-27 07:27  | [2269. 找到一个数字的 K 美丽值](https://leetcode-cn.com/problems/find-the-k-beauty-of-a-number) | EASY | 2 |
| 2022-05-27 07:17  | [面试题 17.11. 单词距离](https://leetcode-cn.com/problems/find-closest-lcci) | MEDIUM | 1 |
| 2022-05-27 03:27  | [1084. 销售分析III](https://leetcode-cn.com/problems/sales-analysis-iii) | EASY | 1 |
| 2022-05-27 03:19  | [1050. 合作过至少三次的演员和导演](https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times) | EASY | 1 |
| 2022-05-26 09:50  | [1587. 银行账户概要 II](https://leetcode-cn.com/problems/bank-account-summary-ii) | EASY | 1 |
| 2022-05-26 08:56  | [2255. 统计是给定字符串前缀的字符串数目](https://leetcode-cn.com/problems/count-prefixes-of-a-given-string) | EASY | 1 |
| 2022-05-26 08:50  | [剑指 Offer II 027. 回文链表](https://leetcode-cn.com/problems/aMhZSa) | EASY | 1 |
| 2022-05-26 07:48  | [LCP 50. 宝石补给](https://leetcode-cn.com/problems/WHnhjV) | EASY | 1 |
| 2022-05-26 07:42  | [剑指 Offer II 023. 两个链表的第一个重合节点](https://leetcode-cn.com/problems/3u1WK4) | EASY | 1 |
| 2022-05-26 07:34  | [剑指 Offer II 052. 展平二叉搜索树](https://leetcode-cn.com/problems/NYBBNL) | EASY | 1 |
| 2022-05-26 07:33  | [剑指 Offer II 056. 二叉搜索树中两个节点之和](https://leetcode-cn.com/problems/opLdQZ) | EASY | 1 |
| 2022-05-26 07:29  | [剑指 Offer II 068. 查找插入位置](https://leetcode-cn.com/problems/N6YdxV) | EASY | 3 |
| 2022-05-26 03:43  | [剑指 Offer II 002. 二进制加法](https://leetcode-cn.com/problems/JFETK5) | EASY | 1 |
| 2022-05-26 03:31  | [剑指 Offer II 024. 反转链表](https://leetcode-cn.com/problems/UHnkqh) | EASY | 1 |
| 2022-05-26 02:57  | [剑指 Offer II 059. 数据流的第 K 大数值](https://leetcode-cn.com/problems/jBjn9C) | EASY | 1 |
| 2022-05-26 02:43  | [剑指 Offer II 012. 左右两边子数组的和相等](https://leetcode-cn.com/problems/tvdfij) | EASY | 1 |
| 2022-05-26 02:35  | [剑指 Offer II 003. 前 n 个数字二进制中 1 的个数](https://leetcode-cn.com/problems/w3tCBm) | EASY | 2 |
| 2022-05-25 09:25  | [LCP 55. 采集果实](https://leetcode-cn.com/problems/PTXy4P) | EASY | 1 |
| 2022-05-25 09:15  | [LCP 44. 开幕式焰火](https://leetcode-cn.com/problems/sZ59z6) | EASY | 1 |
| 2022-05-25 09:08  | [2278. 字母在字符串中的百分比](https://leetcode-cn.com/problems/percentage-of-letter-in-string) | EASY | 1 |
| 2022-05-25 09:04  | [2264. 字符串中最大的 3 位相同数字](https://leetcode-cn.com/problems/largest-3-same-digit-number-in-string) | EASY | 2 |
| 2022-05-25 08:53  | [2235. 两整数相加](https://leetcode-cn.com/problems/add-two-integers) | EASY | 2 |
| 2022-05-25 08:14  | [2194. Excel 表中某个范围内的单元格](https://leetcode-cn.com/problems/cells-in-a-range-on-an-excel-sheet) | EASY | 1 |
| 2022-05-25 08:04  | [2176. 统计数组中相等且可以被整除的数对](https://leetcode-cn.com/problems/count-equal-and-divisible-pairs-in-an-array) | EASY | 1 |
| 2022-05-25 08:01  | [2160. 拆分数位后四位数字的最小和](https://leetcode-cn.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits) | EASY | 1 |
| 2022-05-25 06:48  | [2154. 将找到的值乘以 2](https://leetcode-cn.com/problems/keep-multiplying-found-values-by-two) | EASY | 1 |
| 2022-05-25 06:43  | [2169. 得到 0 的操作数](https://leetcode-cn.com/problems/count-operations-to-obtain-zero) | EASY | 3 |
| 2022-05-25 06:26  | [剑指 Offer II 042. 最近请求次数](https://leetcode-cn.com/problems/H8086Q) | EASY | 1 |
| 2022-05-25 03:50  | [剑指 Offer II 075. 数组相对排序](https://leetcode-cn.com/problems/0H97ZC) | EASY | 1 |
| 2022-05-25 03:48  | [剑指 Offer II 088. 爬楼梯的最少成本](https://leetcode-cn.com/problems/GzCJIP) | EASY | 1 |
| 2022-05-25 03:44  | [剑指 Offer II 069. 山峰数组的顶部](https://leetcode-cn.com/problems/B1IidL) | EASY | 2 |
| 2022-05-25 03:13  | [467. 环绕字符串中唯一的子字符串](https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string) | MEDIUM | 2 |
| 2022-05-24 09:58  | [剑指 Offer II 072. 求平方根](https://leetcode-cn.com/problems/jJ0w9p) | EASY | 2 |
| 2022-05-24 09:23  | [剑指 Offer II 101. 分割等和子集](https://leetcode-cn.com/problems/NUPfPr) | EASY | 1 |
| 2022-05-24 03:25  | [401. 二进制手表](https://leetcode-cn.com/problems/binary-watch) | EASY | 2 |
| 2022-05-24 02:57  | [965. 单值二叉树](https://leetcode-cn.com/problems/univalued-binary-tree) | EASY | 2 |
| 2021-09-23 07:25  | [326. 3 的幂](https://leetcode-cn.com/problems/power-of-three) | EASY | 3 |
| 2021-09-22 08:35  | [725. 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts) | MEDIUM | 1 |
| 2021-09-22 08:26  | [LCP 39. 无人机方阵](https://leetcode-cn.com/problems/0jQkd0) | EASY | 3 |
| 2021-09-22 07:17  | [LCP 40. 心算挑战](https://leetcode-cn.com/problems/uOAnQW) | EASY | 1 |
| 2021-09-22 06:57  | [2006. 差的绝对值为 K 的数对数目](https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k) | EASY | 1 |
| 2021-09-22 06:37  | [2011. 执行操作后的变量值](https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations) | EASY | 1 |
| 2021-09-14 12:16  | [1984. 学生分数的最小差值](https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores) | EASY | 4 |
| 2021-09-14 12:04  | [1991. 找到数组的中间位置](https://leetcode-cn.com/problems/find-the-middle-index-in-array) | EASY | 1 |
| 2021-09-14 11:57  | [2000. 反转单词前缀](https://leetcode-cn.com/problems/reverse-prefix-of-word) | EASY | 5 |
| 2021-08-27 08:38  | [1974. 使用特殊打字机键入单词的最少时间](https://leetcode-cn.com/problems/minimum-time-to-type-word-using-special-typewriter) | EASY | 2 |
| 2021-08-27 08:23  | [1979. 找出数组的最大公约数](https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array) | EASY | 1 |
| 2021-08-26 06:24  | [881. 救生艇](https://leetcode-cn.com/problems/boats-to-save-people) | MEDIUM | 1 |
| 2021-08-16 08:25  | [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree) | EASY | 2 |
| 2021-08-16 08:23  | [155. 最小栈](https://leetcode-cn.com/problems/min-stack) | MEDIUM | 3 |
| 2021-08-16 02:28  | [1967. 作为子字符串出现在单词中的字符串数目](https://leetcode-cn.com/problems/number-of-strings-that-appear-as-substrings-in-word) | EASY | 1 |
| 2021-08-16 02:26  | [1961. 检查字符串是否为数组前缀](https://leetcode-cn.com/problems/check-if-string-is-a-prefix-of-array) | EASY | 2 |
| 2021-08-13 04:56  | [1957. 删除字符使字符串变好](https://leetcode-cn.com/problems/delete-characters-to-make-fancy-string) | EASY | 2 |
| 2021-08-10 01:57  | [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs) | MEDIUM | 1 |
| 2021-08-09 01:45  | [160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 5 |
| 2021-08-06 07:15  | [43. 字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | MEDIUM | 7 |
| 2021-08-05 09:38  | [119. 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 3 |
| 2021-08-05 09:24  | [706. 设计哈希映射](https://leetcode-cn.com/problems/design-hashmap) | EASY | 2 |
| 2021-08-05 09:22  | [415. 字符串相加](https://leetcode-cn.com/problems/add-strings) | EASY | 3 |
| 2021-08-05 09:19  | [290. 单词规律](https://leetcode-cn.com/problems/word-pattern) | EASY | 2 |
| 2021-08-04 23:23  | [518. 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2) | MEDIUM | 3 |
| 2021-08-03 08:01  | [剑指 Offer II 085. 生成匹配的括号](https://leetcode-cn.com/problems/IDBivT) | MEDIUM | 1 |
| 2021-08-03 07:57  | [1952. 三除数](https://leetcode-cn.com/problems/three-divisors) | EASY | 1 |
| 2021-08-03 07:07  | [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum) | MEDIUM | 1 |
| 2021-08-03 06:51  | [516. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence) | MEDIUM | 1 |
| 2021-08-03 06:36  | [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence) | MEDIUM | 1 |
| 2021-08-03 01:49  | [96. 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees) | MEDIUM | 1 |
| 2021-07-30 08:44  | [413. 等差数列划分](https://leetcode-cn.com/problems/arithmetic-slices) | MEDIUM | 1 |
| 2021-07-30 08:00  | [63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii) | MEDIUM | 1 |
| 2021-07-30 02:44  | [171. Excel 表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number) | EASY | 2 |
| 2021-07-30 02:24  | [1941. 检查是否所有字符出现次数相同](https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences) | EASY | 1 |
| 2021-07-30 02:18  | [1945. 字符串转化后的各位数字之和](https://leetcode-cn.com/problems/sum-of-digits-of-string-after-convert) | EASY | 1 |
| 2021-07-30 02:10  | [169. 多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 2 |
| 2021-07-30 02:08  | [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 6 |
| 2021-07-28 10:06  | [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle) | EASY | 4 |
| 2021-07-26 14:06  | [701. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree) | MEDIUM | 1 |
| 2021-07-26 14:02  | [139. 单词拆分](https://leetcode-cn.com/problems/word-break) | MEDIUM | 9 |
| 2021-07-26 06:11  | [191. 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 4 |
| 2021-07-26 06:10  | [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 6 |
| 2021-07-26 06:04  | [112. 路径总和](https://leetcode-cn.com/problems/path-sum) | EASY | 7 |
| 2021-07-26 06:01  | [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 8 |
| 2021-07-26 05:59  | [700. 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) | EASY | 3 |
| 2021-07-26 05:54  | [653. 两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst) | EASY | 2 |
| 2021-07-23 03:02  | [1893. 检查是否区域内所有整数都被覆盖](https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered) | EASY | 5 |
| 2021-07-23 03:00  | [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | MEDIUM | 1 |
| 2021-07-23 02:49  | [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | MEDIUM | 1 |
| 2021-07-23 02:38  | [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle) | MEDIUM | 1 |
| 2021-07-23 02:16  | [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber) | MEDIUM | 4 |
| 2021-07-23 02:02  | [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 8 |
| 2021-07-23 02:00  | [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 3 |
| 2021-07-22 07:10  | [1886. 判断矩阵经轮转后是否一致](https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation) | EASY | 1 |
| 2021-07-22 06:58  | [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 4 |
| 2021-07-22 03:51  | [784. 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation) | MEDIUM | 1 |
| 2021-07-22 03:27  | [46. 全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 4 |
| 2021-07-22 02:30  | [77. 组合](https://leetcode-cn.com/problems/combinations) | MEDIUM | 2 |
| 2021-07-22 02:25  | [1014. 最佳观光组合](https://leetcode-cn.com/problems/best-sightseeing-pair) | MEDIUM | 1 |
| 2021-07-22 02:15  | [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) | MEDIUM | 2 |
| 2021-07-22 02:14  | [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) | EASY | 8 |
| 2021-07-22 02:10  | [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | EASY | 4 |
| 2021-07-22 02:10  | [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) | EASY | 2 |
| 2021-07-21 02:41  | [1567. 乘积为正数的最长子数组长度](https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product) | MEDIUM | 1 |
| 2021-07-21 02:05  | [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | MEDIUM | 3 |
| 2021-07-21 02:01  | [232. 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks) | EASY | 4 |
| 2021-07-21 01:54  | [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 6 |
| 2021-07-20 09:57  | [1935. 可以输入的最大单词数](https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type) | EASY | 2 |
| 2021-07-20 09:52  | [1877. 数组中最大数对和的最小值](https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array) | MEDIUM | 2 |
| 2021-07-20 03:00  | [918. 环形子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-circular-subarray) | MEDIUM | 1 |
| 2021-07-20 02:32  | [994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges) | MEDIUM | 1 |
| 2021-07-20 02:05  | [53. 最大子数组和](https://leetcode-cn.com/problems/maximum-subarray) | MEDIUM | 5 |
| 2021-07-20 01:58  | [83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 4 |
| 2021-07-19 09:12  | [203. 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | EASY | 4 |
| 2021-07-19 02:14  | [116. 填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node) | MEDIUM | 1 |
| 2021-07-19 02:03  | [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game) | MEDIUM | 1 |
| 2021-07-19 01:56  | [45. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii) | MEDIUM | 4 |
| 2021-07-19 01:30  | [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 4 |
| 2021-07-19 01:24  | [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 4 |
| 2021-07-18 01:14  | [740. 删除并获得点数](https://leetcode-cn.com/problems/delete-and-earn) | MEDIUM | 2 |
| 2021-07-18 01:01  | [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii) | MEDIUM | 1 |
| 2021-07-18 00:32  | [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram) | EASY | 2 |
| 2021-07-18 00:29  | [383. 赎金信](https://leetcode-cn.com/problems/ransom-note) | EASY | 3 |
| 2021-07-18 00:15  | [387. 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string) | EASY | 4 |
| 2021-07-17 23:42  | [567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string) | MEDIUM | 1 |
| 2021-07-17 09:11  | [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | MEDIUM | 1 |
| 2021-07-17 03:59  | [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku) | MEDIUM | 2 |
| 2021-07-17 02:23  | [73. 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | MEDIUM | 7 |
| 2021-07-16 07:18  | [1137. 第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number) | EASY | 2 |
| 2021-07-16 07:08  | [1560. 圆形赛道上经过次数最多的扇区](https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track) | EASY | 1 |
| 2021-07-16 07:04  | [1763. 最长的美好子字符串](https://leetcode-cn.com/problems/longest-nice-substring) | EASY | 2 |
| 2021-07-16 06:50  | [剑指 Offer 53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | EASY | 7 |
| 2021-07-16 02:25  | [566. 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | EASY | 5 |
| 2021-07-16 02:09  | [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) | MEDIUM | 1 |
| 2021-07-15 01:34  | [557. 反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) | EASY | 2 |
| 2021-07-15 01:32  | [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string) | EASY | 8 |
| 2021-07-15 01:28  | [350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | EASY | 3 |
| 2021-07-13 09:33  | [783. 二叉搜索树节点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes) | EASY | 1 |
| 2021-07-13 08:51  | [572. 另一棵树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree) | EASY | 4 |
| 2021-07-13 08:05  | [1566. 重复至少 K 次且长度为 M 的模式](https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times) | EASY | 1 |
| 2021-07-13 02:43  | [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | EASY | 3 |
| 2021-07-13 00:00  | [189. 轮转数组](https://leetcode-cn.com/problems/rotate-array) | MEDIUM | 3 |
| 2021-07-12 23:51  | [977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array) | EASY | 2 |
| 2021-07-12 13:03  | [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | EASY | 6 |
| 2021-07-12 06:30  | [1925. 统计平方和三元组的数目](https://leetcode-cn.com/problems/count-square-sum-triples) | EASY | 1 |
| 2021-07-12 03:44  | [1933. 判断字符串是否可分解为值均等的子串](https://leetcode-cn.com/problems/check-if-string-is-decomposable-into-value-equal-substrings) | EASY | 6 |
| 2021-07-12 02:12  | [275. H 指数 II](https://leetcode-cn.com/problems/h-index-ii) | MEDIUM | 1 |
| 2021-07-12 01:58  | [1929. 数组串联](https://leetcode-cn.com/problems/concatenation-of-array) | EASY | 1 |
| 2021-07-09 05:57  | [671. 二叉树中第二小的节点](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree) | EASY | 1 |
| 2021-07-09 03:33  | [面试题 17.10. 主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci) | EASY | 8 |
| 2021-07-05 03:21  | [530. 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst) | EASY | 1 |
| 2021-07-05 02:40  | [1920. 基于排列构建数组](https://leetcode-cn.com/problems/build-array-from-permutation) | EASY | 1 |
| 2021-07-02 07:25  | [1128. 等价多米诺骨牌对的数量](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs) | EASY | 3 |
| 2021-07-02 07:08  | [1346. 检查整数及其两倍数是否存在](https://leetcode-cn.com/problems/check-if-n-and-its-double-exist) | EASY | 1 |
| 2021-07-02 06:46  | [598. 范围求和 II](https://leetcode-cn.com/problems/range-addition-ii) | EASY | 2 |
| 2021-07-02 06:36  | [796. 旋转字符串](https://leetcode-cn.com/problems/rotate-string) | EASY | 1 |
| 2021-07-02 03:49  | [404. 左叶子之和](https://leetcode-cn.com/problems/sum-of-left-leaves) | EASY | 1 |
| 2021-07-02 03:42  | [1576. 替换所有的问号](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters) | EASY | 1 |
| 2021-07-02 03:29  | [1833. 雪糕的最大数量](https://leetcode-cn.com/problems/maximum-ice-cream-bars) | MEDIUM | 2 |
| 2021-07-02 03:24  | [453. 最小操作次数使数组元素相等](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements) | MEDIUM | 2 |
| 2021-07-02 03:08  | [1668. 最大重复子字符串](https://leetcode-cn.com/problems/maximum-repeating-substring) | EASY | 4 |
| 2021-07-02 02:50  | [1758. 生成交替二进制字符串的最少操作数](https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string) | EASY | 1 |
| 2021-07-02 02:29  | [1736. 替换隐藏数字得到的最晚时间](https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits) | EASY | 2 |
| 2021-07-02 02:02  | [661. 图片平滑器](https://leetcode-cn.com/problems/image-smoother) | EASY | 2 |
| 2021-07-01 09:48  | [1909. 删除一个元素使数组严格递增](https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing) | EASY | 3 |
| 2021-07-01 08:22  | [LCS 02. 完成一半题目](https://leetcode-cn.com/problems/WqXACV) | EASY | 4 |
| 2021-07-01 08:02  | [1370. 上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string) | EASY | 1 |
| 2021-07-01 07:58  | [830. 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups) | EASY | 1 |
| 2021-07-01 07:50  | [1791. 找出星型图的中心节点](https://leetcode-cn.com/problems/find-center-of-star-graph) | EASY | 1 |
| 2021-07-01 07:46  | [1913. 两个数对之间的最大乘积差](https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs) | EASY | 1 |
| 2021-07-01 07:42  | [1005. K 次取反后最大化的数组和](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations) | EASY | 1 |
| 2021-07-01 07:04  | [1037. 有效的回旋镖](https://leetcode-cn.com/problems/valid-boomerang) | EASY | 1 |
| 2021-07-01 06:56  | [1103. 分糖果 II](https://leetcode-cn.com/problems/distribute-candies-to-people) | EASY | 2 |
| 2021-07-01 06:46  | [819. 最常见的单词](https://leetcode-cn.com/problems/most-common-word) | EASY | 2 |
| 2021-07-01 02:41  | [643. 子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i) | EASY | 1 |
| 2021-07-01 02:29  | [441. 排列硬币](https://leetcode-cn.com/problems/arranging-coins) | EASY | 1 |
| 2021-07-01 02:13  | [744. 寻找比目标字母大的最小字母](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target) | EASY | 1 |
| 2021-06-30 10:17  | [747. 至少是其他数字两倍的最大数](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others) | EASY | 2 |
| 2021-06-30 10:10  | [674. 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence) | EASY | 2 |
| 2021-06-30 02:46  | [1437. 是否所有 1 都至少相隔 k 个元素](https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away) | EASY | 1 |
| 2021-06-30 02:40  | [1544. 整理字符串](https://leetcode-cn.com/problems/make-the-string-great) | EASY | 1 |
| 2021-06-29 10:18  | [1496. 判断路径是否相交](https://leetcode-cn.com/problems/path-crossing) | EASY | 3 |
| 2021-06-29 08:21  | [78. 子集](https://leetcode-cn.com/problems/subsets) | MEDIUM | 4 |
| 2021-06-29 08:06  | [1282. 用户分组](https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to) | MEDIUM | 1 |
| 2021-06-29 07:49  | [1689. 十-二进制数的最少数目](https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers) | MEDIUM | 1 |
| 2021-06-29 07:41  | [1828. 统计一个圆中点的数目](https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle) | MEDIUM | 1 |
| 2021-06-27 15:13  | [495. 提莫攻击](https://leetcode-cn.com/problems/teemo-attacking) | EASY | 1 |
| 2021-06-25 07:24  | [219. 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii) | EASY | 1 |
| 2021-06-25 06:51  | [1154. 一年中的第几天](https://leetcode-cn.com/problems/day-of-the-year) | EASY | 1 |
| 2021-06-24 08:59  | [628. 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | EASY | 1 |
| 2021-06-24 08:57  | [1317. 将整数转换为两个无零整数的和](https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers) | EASY | 1 |
| 2021-06-24 08:41  | [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer) | EASY | 3 |
| 2021-06-24 06:21  | [1897. 重新分配字符使所有字符串都相等](https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal) | EASY | 1 |
| 2021-06-24 02:57  | [917. 仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters) | EASY | 1 |
| 2021-06-24 02:46  | [1784. 检查二进制字符串字段](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones) | EASY | 2 |
| 2021-06-24 02:40  | [1796. 字符串中第二大的数字](https://leetcode-cn.com/problems/second-largest-digit-in-a-string) | EASY | 1 |
| 2021-06-24 02:30  | [1903. 字符串中的最大奇数](https://leetcode-cn.com/problems/largest-odd-number-in-string) | EASY | 1 |
| 2021-06-24 02:06  | [551. 学生出勤记录 I](https://leetcode-cn.com/problems/student-attendance-record-i) | EASY | 1 |
| 2021-06-24 01:58  | [506. 相对名次](https://leetcode-cn.com/problems/relative-ranks) | EASY | 1 |
| 2021-06-23 10:32  | [520. 检测大写字母](https://leetcode-cn.com/problems/detect-capital) | EASY | 1 |
| 2021-06-23 10:16  | [705. 设计哈希集合](https://leetcode-cn.com/problems/design-hashset) | EASY | 1 |
| 2021-06-23 07:34  | [LCP 11. 期望个数统计](https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji) | EASY | 2 |
| 2021-06-23 07:23  | [面试题 08.10. 颜色填充](https://leetcode-cn.com/problems/color-fill-lcci) | EASY | 1 |
| 2021-06-23 07:03  | [面试题 01.09. 字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci) | EASY | 1 |
| 2021-06-23 06:51  | [面试题 16.15. 珠玑妙算](https://leetcode-cn.com/problems/master-mind-lcci) | EASY | 3 |
| 2021-06-23 06:37  | [面试题 10.05. 稀疏数组搜索](https://leetcode-cn.com/problems/sparse-array-search-lcci) | EASY | 1 |
| 2021-06-23 03:45  | [剑指 Offer 29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof) | EASY | 1 |
| 2021-06-23 03:22  | [剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 1 |
| 2021-06-23 03:22  | [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | MEDIUM | 6 |
| 2021-06-23 02:32  | [剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof) | EASY | 1 |
| 2021-06-23 02:26  | [面试题 03.01. 三合一](https://leetcode-cn.com/problems/three-in-one-lcci) | EASY | 1 |
| 2021-06-23 02:08  | [1523. 在区间范围内统计奇数数目](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range) | EASY | 1 |
| 2021-06-23 02:01  | [剑指 Offer 15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | EASY | 2 |
| 2021-06-23 01:57  | [1446. 连续字符](https://leetcode-cn.com/problems/consecutive-characters) | EASY | 1 |
| 2021-06-22 10:08  | [1417. 重新格式化字符串](https://leetcode-cn.com/problems/reformat-the-string) | EASY | 1 |
| 2021-06-22 09:46  | [1422. 分割字符串的最大得分](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string) | EASY | 1 |
| 2021-06-22 09:32  | [1360. 日期之间隔几天](https://leetcode-cn.com/problems/number-of-days-between-two-dates) | EASY | 1 |
| 2021-06-22 09:16  | [剑指 Offer 10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof) | EASY | 5 |
| 2021-06-22 09:09  | [面试题 17.12. BiNode](https://leetcode-cn.com/problems/binode-lcci) | EASY | 1 |
| 2021-06-22 07:39  | [面试题 10.01. 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci) | EASY | 1 |
| 2021-06-22 06:48  | [剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof) | MEDIUM | 1 |
| 2021-06-22 06:46  | [面试题 04.04. 检查平衡性](https://leetcode-cn.com/problems/check-balance-lcci) | EASY | 2 |
| 2021-06-22 06:36  | [面试题 01.06. 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | EASY | 5 |
| 2021-06-22 03:46  | [面试题 01.04. 回文排列](https://leetcode-cn.com/problems/palindrome-permutation-lcci) | EASY | 2 |
| 2021-06-22 03:33  | [LCS 01. 下载插件](https://leetcode-cn.com/problems/Ju9Xwi) | EASY | 5 |
| 2021-06-21 09:14  | [925. 长按键入](https://leetcode-cn.com/problems/long-pressed-name) | EASY | 4 |
| 2021-06-21 08:32  | [面试题 05.03. 翻转数位](https://leetcode-cn.com/problems/reverse-bits-lcci) | EASY | 1 |
| 2021-06-21 08:22  | [1013. 将数组分成和相等的三个部分](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum) | EASY | 1 |
| 2021-06-21 08:08  | [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii) | EASY | 1 |
| 2021-06-21 06:30  | [507. 完美数](https://leetcode-cn.com/problems/perfect-number) | EASY | 2 |
| 2021-06-21 03:34  | [1033. 移动石子直到连续](https://leetcode-cn.com/problems/moving-stones-until-consecutive) | MEDIUM | 3 |
| 2021-06-21 02:33  | [434. 字符串中的单词数](https://leetcode-cn.com/problems/number-of-segments-in-a-string) | EASY | 2 |
| 2021-06-21 02:26  | [面试题 08.01. 三步问题](https://leetcode-cn.com/problems/three-steps-problem-lcci) | EASY | 2 |
| 2021-06-21 02:19  | [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers) | EASY | 4 |
| 2021-06-21 01:48  | [1629. 按键持续时间最长的键](https://leetcode-cn.com/problems/slowest-key) | EASY | 1 |
| 2021-06-18 09:03  | [面试题 17.16. 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | EASY | 2 |
| 2021-06-18 08:42  | [1018. 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) | EASY | 3 |
| 2021-06-18 08:18  | [1805. 字符串中不同整数的数目](https://leetcode-cn.com/problems/number-of-different-integers-in-a-string) | EASY | 1 |
| 2021-06-18 07:43  | [501. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree) | EASY | 1 |
| 2021-06-18 07:22  | [504. 七进制数](https://leetcode-cn.com/problems/base-7) | EASY | 2 |
| 2021-06-18 06:56  | [面试题 05.01. 插入](https://leetcode-cn.com/problems/insert-into-bits-lcci) | EASY | 2 |
| 2021-06-18 03:54  | [594. 最长和谐子序列](https://leetcode-cn.com/problems/longest-harmonious-subsequence) | EASY | 3 |
| 2021-06-18 03:12  | [459. 重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern) | EASY | 2 |
| 2021-06-18 02:56  | [263. 丑数](https://leetcode-cn.com/problems/ugly-number) | EASY | 2 |
| 2021-06-18 02:46  | [717. 1 比特与 2 比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) | EASY | 3 |
| 2021-06-18 02:31  | [1646. 获取生成数组中的最大值](https://leetcode-cn.com/problems/get-maximum-in-generated-array) | EASY | 10 |
| 2021-06-18 02:02  | [599. 两个列表的最小索引总和](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists) | EASY | 3 |
| 2021-06-17 08:41  | [541. 反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii) | EASY | 7 |
| 2021-06-17 08:00  | [1089. 复写零](https://leetcode-cn.com/problems/duplicate-zeros) | EASY | 3 |
| 2021-06-17 07:40  | [1071. 字符串的最大公因子](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings) | EASY | 1 |
| 2021-06-17 06:47  | [896. 单调数列](https://leetcode-cn.com/problems/monotonic-array) | EASY | 6 |
| 2021-06-17 06:19  | [1408. 数组中的字符串匹配](https://leetcode-cn.com/problems/string-matching-in-an-array) | EASY | 5 |
| 2021-06-17 03:20  | [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies) | EASY | 1 |
| 2021-06-17 02:16  | [65. 有效数字](https://leetcode-cn.com/problems/valid-number) | HARD | 4 |
| 2021-06-16 14:37  | [剑指 Offer 10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 17 |
| 2021-06-16 14:28  | [1025. 除数博弈](https://leetcode-cn.com/problems/divisor-game) | EASY | 3 |
| 2021-06-16 14:20  | [877. 石子游戏](https://leetcode-cn.com/problems/stone-game) | MEDIUM | 2 |
| 2021-06-16 10:01  | [1184. 公交站间的距离](https://leetcode-cn.com/problems/distance-between-bus-stops) | EASY | 1 |
| 2021-06-16 09:52  | [1556. 千位分隔数](https://leetcode-cn.com/problems/thousand-separator) | EASY | 1 |
| 2021-06-16 09:18  | [剑指 Offer 58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof) | EASY | 2 |
| 2021-06-16 09:12  | [1592. 重新排列单词间的空格](https://leetcode-cn.com/problems/rearrange-spaces-between-words) | EASY | 1 |
| 2021-06-16 08:45  | [482. 密钥格式化](https://leetcode-cn.com/problems/license-key-formatting) | EASY | 1 |
| 2021-06-16 08:15  | [1232. 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) | EASY | 2 |
| 2021-06-16 07:58  | [788. 旋转数字](https://leetcode-cn.com/problems/rotated-digits) | MEDIUM | 1 |
| 2021-06-16 07:46  | [面试题 16.05. 阶乘尾数](https://leetcode-cn.com/problems/factorial-zeros-lcci) | EASY | 3 |
| 2021-06-16 07:40  | [1009. 十进制整数的反码](https://leetcode-cn.com/problems/complement-of-base-10-integer) | EASY | 1 |
| 2021-06-16 07:35  | [面试题 03.06. 动物收容所](https://leetcode-cn.com/problems/animal-shelter-lcci) | EASY | 3 |
| 2021-06-16 07:11  | [985. 查询后的偶数和](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries) | MEDIUM | 2 |
| 2021-06-16 06:57  | [868. 二进制间距](https://leetcode-cn.com/problems/binary-gap) | EASY | 2 |
| 2021-06-16 06:43  | [1078. Bigram 分词](https://leetcode-cn.com/problems/occurrences-after-bigram) | EASY | 1 |
| 2021-06-16 02:36  | [LCP 07. 传递信息](https://leetcode-cn.com/problems/chuan-di-xin-xi) | EASY | 3 |
| 2021-06-16 01:54  | [892. 三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes) | EASY | 2 |
| 2021-06-15 12:46  | [面试题 16.17. 连续数列](https://leetcode-cn.com/problems/contiguous-sequence-lcci) | EASY | 1 |
| 2021-06-15 12:42  | [976. 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle) | EASY | 2 |
| 2021-06-15 10:02  | [929. 独特的电子邮件地址](https://leetcode-cn.com/problems/unique-email-addresses) | EASY | 2 |
| 2021-06-15 09:52  | [1441. 用栈操作构建数组](https://leetcode-cn.com/problems/build-an-array-with-stack-operations) | EASY | 1 |
| 2021-06-15 09:33  | [1337. 矩阵中战斗力最弱的 K 行](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix) | EASY | 3 |
| 2021-06-15 07:49  | [1790. 仅执行一次字符串交换能否使两个字符串相等](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal) | EASY | 2 |
| 2021-06-15 07:37  | [1399. 统计最大组的数目](https://leetcode-cn.com/problems/count-largest-group) | EASY | 1 |
| 2021-06-15 07:05  | [412. Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | EASY | 1 |
| 2021-06-15 06:57  | [1640. 能否连接形成数组](https://leetcode-cn.com/problems/check-array-formation-through-concatenation) | EASY | 2 |
| 2021-06-15 06:31  | [1491. 去掉最低工资和最高工资后的工资平均值](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary) | EASY | 1 |
| 2021-06-15 06:27  | [1582. 二进制矩阵中的特殊位置](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix) | EASY | 1 |
| 2021-06-15 02:56  | [1716. 计算力扣银行的钱](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank) | EASY | 3 |
| 2021-06-15 01:45  | [852. 山脉数组的峰顶索引](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array) | MEDIUM | 5 |
| 2021-06-11 19:05  | [806. 写字符串需要的行数](https://leetcode-cn.com/problems/number-of-lines-to-write-string) | EASY | 5 |
| 2021-06-11 18:26  | [867. 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix) | EASY | 1 |
| 2021-06-11 18:16  | [1598. 文件夹操作日志搜集器](https://leetcode-cn.com/problems/crawler-log-folder) | EASY | 1 |
| 2021-06-11 17:15  | [961. 在长度 2N 的数组中找出重复 N 次的元素](https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array) | EASY | 1 |
| 2021-06-11 17:06  | [剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 7 |
| 2021-06-11 16:47  | [1332. 删除回文子序列](https://leetcode-cn.com/problems/remove-palindromic-subsequences) | EASY | 2 |
| 2021-06-11 16:18  | [999. 可以被一步捕获的棋子数](https://leetcode-cn.com/problems/available-captures-for-rook) | EASY | 2 |
| 2021-06-11 09:55  | [1694. 重新格式化电话号码](https://leetcode-cn.com/problems/reformat-phone-number) | EASY | 5 |
| 2021-06-11 09:35  | [1455. 检查单词是否为句中其他单词的前缀](https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence) | EASY | 1 |
| 2021-06-11 09:16  | [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof) | EASY | 1 |
| 2021-06-11 09:13  | [1742. 盒子中小球的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box) | EASY | 2 |
| 2021-06-11 09:01  | [883. 三维形体投影面积](https://leetcode-cn.com/problems/projection-area-of-3d-shapes) | EASY | 2 |
| 2021-06-11 08:41  | [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i) | EASY | 1 |
| 2021-06-11 08:29  | [1122. 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array) | EASY | 2 |
| 2021-06-11 08:17  | [521. 最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i) | EASY | 1 |
| 2021-06-11 08:12  | [1403. 非递增顺序的最小子序列](https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order) | EASY | 3 |
| 2021-06-11 07:58  | [821. 字符的最短距离](https://leetcode-cn.com/problems/shortest-distance-to-a-character) | EASY | 2 |
| 2021-06-11 07:43  | [1413. 逐步求和得到正数的最小值](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum) | EASY | 1 |
| 2021-06-11 07:29  | [1160. 拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) | EASY | 1 |
| 2021-06-11 07:16  | [剑指 Offer 39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof) | EASY | 1 |
| 2021-06-11 07:14  | [面试题 02.01. 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci) | EASY | 2 |
| 2021-06-11 06:55  | [1800. 最大升序子数组和](https://leetcode-cn.com/problems/maximum-ascending-subarray-sum) | EASY | 1 |
| 2021-06-11 06:50  | [1200. 最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference) | EASY | 1 |
| 2021-06-11 06:42  | [575. 分糖果](https://leetcode-cn.com/problems/distribute-candies) | EASY | 1 |
| 2021-06-11 06:30  | [LCP 02. 分式化简](https://leetcode-cn.com/problems/deep-dark-fraction) | EASY | 1 |
| 2021-06-11 06:17  | [811. 子域名访问计数](https://leetcode-cn.com/problems/subdomain-visit-count) | MEDIUM | 1 |
| 2021-06-11 03:53  | [682. 棒球比赛](https://leetcode-cn.com/problems/baseball-game) | EASY | 1 |
| 2021-06-11 03:38  | [1752. 检查数组是否经排序和轮转得到](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated) | EASY | 1 |
| 2021-06-11 03:23  | [908. 最小差值 I](https://leetcode-cn.com/problems/smallest-range-i) | EASY | 1 |
| 2021-06-11 03:10  | [1710. 卡车上的最大单元数](https://leetcode-cn.com/problems/maximum-units-on-a-truck) | EASY | 1 |
| 2021-06-11 03:00  | [1848. 到目标元素的最小距离](https://leetcode-cn.com/problems/minimum-distance-to-the-target-element) | EASY | 1 |
| 2021-06-11 02:42  | [476. 数字的补数](https://leetcode-cn.com/problems/number-complement) | EASY | 1 |
| 2021-06-11 02:32  | [面试题 05.07. 配对交换](https://leetcode-cn.com/problems/exchange-lcci) | EASY | 1 |
| 2021-06-11 02:27  | [1636. 按照频率将数组升序排序](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency) | EASY | 1 |
| 2021-06-11 02:16  | [剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof) | EASY | 1 |
| 2021-06-10 15:30  | [1287. 有序数组中出现次数超过25%的元素](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array) | EASY | 1 |
| 2021-06-10 15:26  | [1185. 一周中的第几天](https://leetcode-cn.com/problems/day-of-the-week) | EASY | 1 |
| 2021-06-10 15:23  | [面试题 03.02. 栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci) | EASY | 1 |
| 2021-06-10 15:03  | [1779. 找到最近的有相同 X 或 Y 坐标的点](https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate) | EASY | 3 |
| 2021-06-10 14:36  | [448. 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 1 |
| 2021-06-10 14:26  | [1189. “气球” 的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balloons) | EASY | 1 |
| 2021-06-10 14:09  | [1652. 拆炸弹](https://leetcode-cn.com/problems/defuse-the-bomb) | EASY | 2 |
| 2021-06-10 13:42  | [剑指 Offer 57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof) | EASY | 2 |
| 2021-06-10 13:33  | [1550. 存在连续三个奇数的数组](https://leetcode-cn.com/problems/three-consecutive-odds) | EASY | 2 |
| 2021-06-10 13:30  | [1394. 找出数组中的幸运数](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) | EASY | 2 |
| 2021-06-10 13:27  | [剑指 Offer 50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof) | EASY | 1 |
| 2021-06-10 13:02  | [922. 按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii) | EASY | 1 |
| 2021-06-10 12:53  | [剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 1 |
| 2021-06-10 10:18  | [1385. 两个数组间的距离值](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays) | EASY | 1 |
| 2021-06-10 10:10  | [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity) | EASY | 1 |
| 2021-06-10 10:05  | [500. 键盘行](https://leetcode-cn.com/problems/keyboard-row) | EASY | 1 |
| 2021-06-10 09:52  | [1380. 矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix) | EASY | 1 |
| 2021-06-10 09:45  | [893. 特殊等价字符串组](https://leetcode-cn.com/problems/groups-of-special-equivalent-strings) | MEDIUM | 3 |
| 2021-06-10 09:07  | [766. 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix) | EASY | 1 |
| 2021-06-10 08:46  | [面试题 03.04. 化栈为队](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci) | EASY | 1 |
| 2021-06-10 08:42  | [933. 最近的请求次数](https://leetcode-cn.com/problems/number-of-recent-calls) | EASY | 2 |
| 2021-06-10 08:33  | [1502. 判断能否形成等差数列](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence) | EASY | 1 |
| 2021-06-10 07:09  | [1047. 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) | EASY | 1 |
| 2021-06-10 06:58  | [1304. 和为零的 N 个不同整数](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero) | EASY | 2 |
| 2021-06-10 06:41  | [1002. 查找共用字符](https://leetcode-cn.com/problems/find-common-characters) | EASY | 1 |
| 2021-06-10 05:11  | [897. 递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree) | EASY | 2 |
| 2021-06-10 05:07  | [1351. 统计有序矩阵中的负数](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix) | EASY | 4 |
| 2021-06-10 04:41  | [1323. 6 和 9 组成的最大数字](https://leetcode-cn.com/problems/maximum-69-number) | EASY | 2 |
| 2021-06-10 03:08  | [1460. 通过翻转子数组使两个数组相等](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays) | EASY | 1 |
| 2021-06-10 02:31  | [1876. 长度为三且各字符不同的子字符串](https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters) | EASY | 1 |
| 2021-06-09 10:02  | [剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 1 |
| 2021-06-09 10:00  | [1816. 截断句子](https://leetcode-cn.com/problems/truncate-sentence) | EASY | 1 |
| 2021-06-09 09:58  | [728. 自除数](https://leetcode-cn.com/problems/self-dividing-numbers) | EASY | 2 |
| 2021-06-09 09:37  | [1309. 解码字母到整数映射](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping) | EASY | 2 |
| 2021-06-09 09:10  | [1656. 设计有序流](https://leetcode-cn.com/problems/design-an-ordered-stream) | EASY | 1 |
| 2021-06-09 08:50  | [1464. 数组中两元素的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array) | EASY | 1 |
| 2021-06-09 08:48  | [1880. 检查某单词是否等于两单词之和](https://leetcode-cn.com/problems/check-if-word-equals-summation-of-two-words) | EASY | 3 |
| 2021-06-09 08:26  | [1812. 判断国际象棋棋盘中一个格子的颜色](https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square) | EASY | 1 |
| 2021-06-09 08:17  | [1725. 可以形成最大正方形的矩形数目](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square) | EASY | 1 |
| 2021-06-09 08:11  | [1827. 最少操作使数组递增](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing) | EASY | 1 |
| 2021-06-09 08:04  | [338. 比特位计数](https://leetcode-cn.com/problems/counting-bits) | EASY | 2 |
| 2021-06-09 07:54  | [面试题 04.02. 最小高度树](https://leetcode-cn.com/problems/minimum-height-tree-lcci) | EASY | 2 |
| 2021-06-09 07:49  | [832. 翻转图像](https://leetcode-cn.com/problems/flipping-an-image) | EASY | 2 |
| 2021-06-09 07:37  | [1837. K 进制表示下的各位数字总和](https://leetcode-cn.com/problems/sum-of-digits-in-base-k) | EASY | 1 |
| 2021-06-09 07:27  | [1450. 在既定时间做作业的学生人数](https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time) | EASY | 2 |
| 2021-06-09 07:20  | [1221. 分割平衡字符串](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings) | EASY | 2 |
| 2021-06-09 06:48  | [1572. 矩阵对角线元素的和](https://leetcode-cn.com/problems/matrix-diagonal-sum) | EASY | 1 |
| 2021-06-09 06:41  | [1389. 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | EASY | 3 |
| 2021-06-09 03:25  | [1266. 访问所有点的最小时间](https://leetcode-cn.com/problems/minimum-time-visiting-all-points) | EASY | 1 |
| 2021-06-09 02:47  | [1773. 统计匹配检索规则的物品数量](https://leetcode-cn.com/problems/count-items-matching-a-rule) | EASY | 1 |
| 2021-06-09 02:37  | [1863. 找出所有子集的异或总和再求和](https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals) | EASY | 2 |
| 2021-06-09 02:33  | [1486. 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array) | EASY | 1 |
| 2021-06-08 14:45  | [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree) | MEDIUM | 1 |
| 2021-06-08 09:53  | [1869. 哪种连续子字符串更长](https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros) | EASY | 1 |
| 2021-06-08 09:26  | [1769. 移动所有球到每个盒子所需的最小操作数](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box) | MEDIUM | 1 |
| 2021-06-08 07:21  | [剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof) | MEDIUM | 1 |
| 2021-06-08 07:20  | [1672. 最富有客户的资产总量](https://leetcode-cn.com/problems/richest-customer-wealth) | EASY | 1 |
| 2021-06-08 07:17  | [807. 保持城市天际线](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline) | MEDIUM | 2 |
| 2021-06-08 06:35  | [535. TinyURL 的加密与解密](https://leetcode-cn.com/problems/encode-and-decode-tinyurl) | MEDIUM | 3 |
| 2021-06-08 06:21  | [面试题 16.01. 交换数字](https://leetcode-cn.com/problems/swap-numbers-lcci) | MEDIUM | 2 |
| 2021-06-08 06:18  | [1281. 整数的各位积和之差](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer) | EASY | 1 |
| 2021-06-08 03:12  | [剑指 Offer 17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof) | EASY | 1 |
| 2021-06-08 03:03  | [1436. 旅行终点站](https://leetcode-cn.com/problems/destination-city) | EASY | 1 |
| 2021-06-08 02:48  | [657. 机器人能否返回原点](https://leetcode-cn.com/problems/robot-return-to-origin) | EASY | 1 |
| 2021-06-08 02:38  | [面试题 02.02. 返回倒数第 k 个节点](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci) | EASY | 1 |
| 2021-06-08 02:26  | [1768. 交替合并字符串](https://leetcode-cn.com/problems/merge-strings-alternately) | EASY | 1 |
| 2021-06-08 02:17  | [1049. 最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii) | MEDIUM | 1 |
| 2021-06-07 10:13  | [1299. 将每个元素替换为右侧最大元素](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side) | EASY | 1 |
| 2021-06-07 10:05  | [1859. 将句子排序](https://leetcode-cn.com/problems/sorting-the-sentence) | EASY | 1 |
| 2021-06-07 09:46  | [1732. 找到最高海拔](https://leetcode-cn.com/problems/find-the-highest-altitude) | EASY | 2 |
| 2021-06-07 09:04  | [1720. 解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array) | EASY | 1 |
| 2021-06-07 08:55  | [859. 亲密字符串](https://leetcode-cn.com/problems/buddy-strings) | EASY | 1 |
| 2021-06-07 08:29  | [665. 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array) | MEDIUM | 1 |
| 2021-06-07 08:16  | [LCP 33. 蓄水](https://leetcode-cn.com/problems/o8SXZn) | EASY | 8 |
| 2021-06-07 06:54  | [494. 目标和](https://leetcode-cn.com/problems/target-sum) | MEDIUM | 1 |
| 2021-06-07 03:47  | [563. 二叉树的坡度](https://leetcode-cn.com/problems/binary-tree-tilt) | EASY | 2 |
| 2021-06-07 02:42  | [561. 数组拆分](https://leetcode-cn.com/problems/array-partition) | EASY | 1 |
| 2021-06-04 09:31  | [1684. 统计一致字符串的数目](https://leetcode-cn.com/problems/count-the-number-of-consistent-strings) | EASY | 1 |
| 2021-06-04 08:18  | [1365. 有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number) | EASY | 2 |
| 2021-06-04 07:53  | [1832. 判断句子是否为全字母句](https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram) | EASY | 1 |
| 2021-06-04 07:46  | [1822. 数组元素积的符号](https://leetcode-cn.com/problems/sign-of-the-product-of-an-array) | EASY | 1 |
| 2021-06-04 07:43  | [1854. 人口最多的年份](https://leetcode-cn.com/problems/maximum-population-year) | EASY | 2 |
| 2021-06-04 07:09  | [938. 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst) | EASY | 3 |
| 2021-06-04 06:48  | [1662. 检查两个字符串数组是否相等](https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent) | EASY | 1 |
| 2021-06-04 06:46  | [1295. 统计位数为偶数的数字](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits) | EASY | 2 |
| 2021-06-04 06:36  | [1844. 将所有数字用字符替换](https://leetcode-cn.com/problems/replace-all-digits-with-characters) | EASY | 1 |
| 2021-06-04 02:47  | [888. 公平的糖果交换](https://leetcode-cn.com/problems/fair-candy-swap) | EASY | 1 |
| 2021-06-03 03:03  | [885. 螺旋矩阵 III](https://leetcode-cn.com/problems/spiral-matrix-iii) | MEDIUM | 1 |
| 2021-06-03 02:14  | [884. 两句话中的不常见单词](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences) | EASY | 1 |
| 2021-06-02 07:12  | [698. 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets) | MEDIUM | 1 |
| 2021-06-02 06:39  | [697. 数组的度](https://leetcode-cn.com/problems/degree-of-an-array) | EASY | 1 |
| 2021-06-02 03:37  | [696. 计数二进制子串](https://leetcode-cn.com/problems/count-binary-substrings) | EASY | 1 |
| 2021-06-02 03:23  | [693. 交替位二进制数](https://leetcode-cn.com/problems/binary-number-with-alternating-bits) | EASY | 2 |
| 2021-06-02 02:23  | [690. 员工的重要性](https://leetcode-cn.com/problems/employee-importance) | MEDIUM | 2 |
| 2021-06-01 07:11  | [面试题 08.08. 有重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-ii-lcci) | MEDIUM | 1 |
| 2021-06-01 02:53  | [面试题 08.07. 无重复字符串的排列组合](https://leetcode-cn.com/problems/permutation-i-lcci) | MEDIUM | 1 |
| 2021-06-01 02:35  | [面试题 08.06. 汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci) | EASY | 2 |
| 2021-05-31 09:54  | [面试题 08.05. 递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci) | MEDIUM | 2 |
| 2021-05-31 09:11  | [面试题 08.04. 幂集](https://leetcode-cn.com/problems/power-set-lcci) | MEDIUM | 2 |
| 2021-05-31 08:08  | [面试题 08.03. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci) | EASY | 1 |
| 2021-05-31 07:47  | [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) | HARD | 1 |
| 2021-05-31 07:44  | [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) | MEDIUM | 2 |
| 2021-05-28 09:09  | [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | MEDIUM | 3 |
| 2021-05-28 07:37  | [477. 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance) | MEDIUM | 11 |
| 2021-05-28 07:34  | [面试题 02.06. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci) | EASY | 1 |
| 2021-05-28 07:33  | [234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 1 |
| 2021-05-28 07:26  | [剑指 Offer 52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | EASY | 1 |
| 2021-05-28 07:24  | [剑指 Offer 22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | EASY | 1 |
| 2021-05-28 07:08  | [面试题 02.07. 链表相交](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci) | EASY | 2 |
| 2021-05-28 06:47  | [剑指 Offer 25. 合并两个排序的链表](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof) | EASY | 1 |
| 2021-05-28 06:29  | [剑指 Offer 06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 1 |
| 2021-05-28 05:55  | [1290. 二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) | EASY | 3 |
| 2021-05-28 05:02  | [237. 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | EASY | 3 |
| 2021-05-28 04:46  | [剑指 Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof) | EASY | 2 |
| 2021-05-28 03:47  | [剑指 Offer 24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof) | EASY | 2 |
| 2021-05-27 07:42  | [1704. 判断字符串的两半是否相似](https://leetcode-cn.com/problems/determine-if-string-halves-are-alike) | EASY | 1 |
| 2021-05-27 07:29  | [1701. 平均等待时间](https://leetcode-cn.com/problems/average-waiting-time) | MEDIUM | 3 |
| 2021-05-27 03:48  | [1700. 无法吃午餐的学生数量](https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch) | EASY | 3 |
| 2021-05-26 09:19  | [1678. 设计 Goal 解析器](https://leetcode-cn.com/problems/goal-parser-interpretation) | EASY | 2 |
| 2021-05-26 09:09  | [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers) | MEDIUM | 2 |
| 2021-05-26 06:34  | [面试题 17.14. 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci) | MEDIUM | 1 |
| 2021-05-26 03:50  | [486. 预测赢家](https://leetcode-cn.com/problems/predict-the-winner) | MEDIUM | 1 |
| 2021-05-26 03:04  | [292. Nim 游戏](https://leetcode-cn.com/problems/nim-game) | EASY | 1 |
| 2021-05-26 02:53  | [382. 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node) | MEDIUM | 1 |
| 2021-05-26 02:47  | [398. 随机数索引](https://leetcode-cn.com/problems/random-pick-index) | MEDIUM | 2 |
| 2021-05-26 02:22  | [709. 转换成小写字母](https://leetcode-cn.com/problems/to-lower-case) | EASY | 2 |
| 2021-05-25 06:39  | [390. 消除游戏](https://leetcode-cn.com/problems/elimination-game) | MEDIUM | 4 |
| 2021-05-25 03:48  | [面试题 01.03. URL化](https://leetcode-cn.com/problems/string-to-url-lcci) | EASY | 2 |
| 2021-05-25 03:44  | [225. 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues) | EASY | 3 |
| 2021-05-23 14:31  | [374. 猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower) | EASY | 5 |
| 2021-05-18 07:37  | [LCP 17. 速算机器人](https://leetcode-cn.com/problems/nGK0Fy) | EASY | 1 |
| 2021-05-18 07:33  | [LCP 29. 乐团站位](https://leetcode-cn.com/problems/SNJvJP) | MEDIUM | 1 |
| 2021-05-18 07:13  | [LCP 18. 早餐组合](https://leetcode-cn.com/problems/2vYnGI) | EASY | 2 |
| 2021-05-18 06:39  | [LCP 28. 采购方案](https://leetcode-cn.com/problems/4xy4Wx) | EASY | 1 |
| 2021-05-18 06:16  | [面试题 16.11. 跳水板](https://leetcode-cn.com/problems/diving-board-lcci) | EASY | 4 |
| 2021-05-18 05:06  | [剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | EASY | 1 |
| 2021-05-18 05:00  | [剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof) | EASY | 2 |
| 2021-05-18 04:44  | [剑指 Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof) | EASY | 3 |
| 2021-05-18 04:41  | [剑指 Offer 53 - II. 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof) | EASY | 2 |
| 2021-05-18 03:47  | [1442. 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) | MEDIUM | 2 |
| 2021-05-17 02:25  | [993. 二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) | EASY | 2 |
| 2021-05-17 02:00  | [面试题 05.06. 整数转换](https://leetcode-cn.com/problems/convert-integer-lcci) | EASY | 8 |
| 2021-05-15 08:33  | [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 10 |
| 2021-05-14 11:06  | [面试题 16.07. 最大数值](https://leetcode-cn.com/problems/maximum-lcci) | EASY | 1 |
| 2021-05-14 11:03  | [面试题 17.01. 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci) | EASY | 1 |
| 2021-05-14 11:02  | [面试题 17.04. 消失的数字](https://leetcode-cn.com/problems/missing-number-lcci) | EASY | 1 |
| 2021-05-14 10:37  | [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | MEDIUM | 5 |
| 2021-05-14 10:36  | [762. 二进制表示中质数个计算置位](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation) | EASY | 1 |
| 2021-05-14 10:22  | [1342. 将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero) | EASY | 4 |
| 2021-05-14 09:22  | [268. 丢失的数字](https://leetcode-cn.com/problems/missing-number) | EASY | 4 |
| 2021-05-14 09:09  | [231. 2 的幂](https://leetcode-cn.com/problems/power-of-two) | EASY | 1 |
| 2021-05-14 08:44  | [342. 4的幂](https://leetcode-cn.com/problems/power-of-four) | EASY | 5 |
| 2021-05-13 03:27  | [944. 删列造序](https://leetcode-cn.com/problems/delete-columns-to-make-sorted) | EASY | 1 |
| 2021-05-13 03:12  | [1269. 停在原地的方案数](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) | HARD | 4 |
| 2021-05-13 02:38  | [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | MEDIUM | 3 |
| 2021-05-13 02:30  | [1688. 比赛中的配对次数](https://leetcode-cn.com/problems/count-of-matches-in-tournament) | EASY | 3 |
| 2021-05-13 02:18  | [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii) | MEDIUM | 3 |
| 2021-05-12 08:20  | [461. 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 6 |
| 2021-05-11 08:33  | [剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 |
| 2021-05-11 08:25  | [剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) | EASY | 1 |
| 2021-05-11 08:16  | [814. 二叉树剪枝](https://leetcode-cn.com/problems/binary-tree-pruning) | MEDIUM | 1 |
| 2021-05-11 08:08  | [543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree) | EASY | 1 |
| 2021-05-10 09:23  | [872. 叶子相似的树](https://leetcode-cn.com/problems/leaf-similar-trees) | EASY | 2 |
| 2021-05-10 09:15  | [剑指 Offer 55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof) | EASY | 2 |
| 2021-05-10 09:06  | [剑指 Offer 28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof) | EASY | 4 |
| 2021-05-10 08:56  | [剑指 Offer 32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) | EASY | 1 |
| 2021-05-10 08:42  | [剑指 Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof) | EASY | 2 |
| 2021-05-10 08:31  | [剑指 Offer 27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof) | EASY | 3 |
| 2021-03-29 08:12  | [1748. 唯一元素的和](https://leetcode-cn.com/problems/sum-of-unique-elements) | EASY | 2 |
| 2021-03-25 02:41  | [1116. 打印零与奇偶数](https://leetcode-cn.com/problems/print-zero-even-odd) | MEDIUM | 2 |
| 2021-03-23 08:26  | [1621. 大小为 K 的不重叠线段的数目](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments) | MEDIUM | 1 |
| 2021-03-22 08:13  | [1620. 网络信号最好的坐标](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality) | MEDIUM | 5 |
| 2021-03-22 02:54  | [1619. 删除某些元素后的数组均值](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements) | EASY | 1 |
| 2021-03-19 15:50  | [1603. 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 3 |
| 2021-03-19 15:32  | [剑指 Offer 54. 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof) | EASY | 3 |
| 2020-12-18 08:42  | [389. 找不同](https://leetcode-cn.com/problems/find-the-difference) | EASY | 6 |
| 2020-12-04 07:12  | [793. 阶乘函数后 K 个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function) | HARD | 1 |
| 2020-12-03 15:48  | [825. 适龄的朋友](https://leetcode-cn.com/problems/friends-of-appropriate-ages) | MEDIUM | 1 |
| 2020-12-03 15:02  | [824. 山羊拉丁文](https://leetcode-cn.com/problems/goat-latin) | EASY | 2 |
| 2020-12-02 07:28  | [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 1 |
| 2020-11-30 16:12  | [LCP 22. 黑白方格画](https://leetcode-cn.com/problems/ccw6C7) | EASY | 1 |
| 2020-11-26 08:42  | [371. 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | MEDIUM | 3 |
| 2020-11-26 06:48  | [367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square) | EASY | 5 |
| 2020-11-26 06:22  | [357. 统计各位数字都不同的数字个数](https://leetcode-cn.com/problems/count-numbers-with-unique-digits) | MEDIUM | 4 |
| 2020-11-26 02:41  | [349. 两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays) | EASY | 4 |
| 2020-11-24 06:33  | [201. 数字范围按位与](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range) | MEDIUM | 1 |
| 2020-11-23 13:11  | [1475. 商品折扣后的最终价格](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop) | EASY | 1 |
| 2020-11-23 12:54  | [1471. 数组中的 k 个最强值](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array) | MEDIUM | 2 |
| 2020-11-23 11:52  | [1470. 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array) | EASY | 2 |
| 2020-11-23 06:39  | [204. 计数质数](https://leetcode-cn.com/problems/count-primes) | MEDIUM | 3 |
| 2020-11-20 09:21  | [202. 快乐数](https://leetcode-cn.com/problems/happy-number) | EASY | 3 |
| 2020-11-20 08:12  | [230. 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) | MEDIUM | 4 |
| 2020-11-20 07:18  | [229. 多数元素 II](https://leetcode-cn.com/problems/majority-element-ii) | MEDIUM | 5 |
| 2020-11-20 06:25  | [228. 汇总区间](https://leetcode-cn.com/problems/summary-ranges) | EASY | 6 |
| 2020-11-18 17:51  | [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) | MEDIUM | 3 |
| 2020-11-18 12:35  | [135. 分发糖果](https://leetcode-cn.com/problems/candy) | HARD | 2 |
| 2020-11-18 12:12  | [134. 加油站](https://leetcode-cn.com/problems/gas-station) | MEDIUM | 5 |
| 2020-11-18 09:04  | [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree) | EASY | 10 |
| 2020-11-18 03:45  | [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths) | EASY | 3 |
| 2020-11-18 02:29  | [1079. 活字印刷](https://leetcode-cn.com/problems/letter-tile-possibilities) | MEDIUM | 1 |
| 2020-11-17 07:08  | [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | MEDIUM | 2 |
| 2020-11-16 23:46  | [1030. 距离顺序排列矩阵单元格](https://leetcode-cn.com/problems/matrix-cells-in-distance-order) | EASY | 2 |
| 2020-11-16 23:16  | [1588. 所有奇数长度子数组的和](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays) | EASY | 2 |
| 2020-11-15 01:04  | [面试题 02.03. 删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci) | EASY | 2 |
| 2020-11-14 15:37  | [771. 宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones) | EASY | 2 |
| 2020-11-13 15:50  | [1313. 解压缩编码列表](https://leetcode-cn.com/problems/decompress-run-length-encoded-list) | EASY | 2 |
| 2020-11-12 13:54  | [1539. 第 k 个缺失的正整数](https://leetcode-cn.com/problems/kth-missing-positive-number) | EASY | 2 |
| 2020-11-12 11:16  | [1528. 重新排列字符串](https://leetcode-cn.com/problems/shuffle-string) | EASY | 4 |
| 2020-11-12 11:05  | [1518. 换酒问题](https://leetcode-cn.com/problems/water-bottles) | EASY | 4 |
| 2020-11-12 06:51  | [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome) | EASY | 7 |
| 2020-11-11 14:49  | [1507. 转变日期格式](https://leetcode-cn.com/problems/reformat-date) | EASY | 5 |
| 2020-11-11 14:30  | [1512. 好数对的数目](https://leetcode-cn.com/problems/number-of-good-pairs) | EASY | 1 |
| 2020-11-11 08:44  | [168. Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title) | EASY | 7 |
| 2020-11-11 07:30  | [69. x 的平方根 ](https://leetcode-cn.com/problems/sqrtx) | EASY | 10 |
| 2020-11-11 03:53  | [172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes) | MEDIUM | 4 |
| 2020-11-11 03:37  | [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion) | MEDIUM | 8 |
| 2020-11-10 03:12  | [31. 下一个排列](https://leetcode-cn.com/problems/next-permutation) | MEDIUM | 3 |
| 2020-11-09 15:25  | [剑指 Offer 30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof) | EASY | 2 |
| 2020-11-09 15:09  | [剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof) | EASY | 2 |
| 2020-11-09 15:06  | [1431. 拥有最多糖果的孩子](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) | EASY | 3 |
| 2020-11-09 06:10  | [973. 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin) | MEDIUM | 8 |
| 2020-11-06 08:47  | [238. 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | MEDIUM | 8 |
| 2020-11-06 08:13  | [1356. 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits) | EASY | 1 |
| 2020-11-06 07:36  | [LCP 01. 猜数字](https://leetcode-cn.com/problems/guess-numbers) | EASY | 1 |
| 2020-11-06 07:33  | [1608. 特殊数组的特征值](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x) | EASY | 1 |
| 2020-11-06 04:57  | [1604. 警告一小时内使用相同员工卡大于等于三次的人](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period) | MEDIUM | 6 |
| 2020-11-05 08:30  | [1624. 两个相同字符之间的最长子字符串](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters) | EASY | 3 |
| 2020-11-05 02:38  | [LCP 06. 拿硬币](https://leetcode-cn.com/problems/na-ying-bi) | EASY | 3 |
| 2020-11-04 15:40  | [57. 插入区间](https://leetcode-cn.com/problems/insert-interval) | MEDIUM | 1 |
| 2020-11-04 15:09  | [937. 重新排列日志文件](https://leetcode-cn.com/problems/reorder-data-in-log-files) | MEDIUM | 1 |
| 2020-11-04 14:58  | [942. 增减字符串匹配](https://leetcode-cn.com/problems/di-string-match) | EASY | 2 |
| 2020-11-04 09:18  | [1614. 括号的最大嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses) | EASY | 2 |
| 2020-11-03 14:57  | [941. 有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array) | EASY | 3 |
| 2020-11-02 15:56  | [66. 加一](https://leetcode-cn.com/problems/plus-one) | EASY | 2 |
| 2020-11-02 15:33  | [58. 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | EASY | 2 |
| 2020-11-02 07:45  | [258. 各位相加](https://leetcode-cn.com/problems/add-digits) | EASY | 2 |
| 2020-11-02 07:37  | [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | MEDIUM | 1 |
| 2020-10-31 02:29  | [381. O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed) | HARD | 8 |
| 2020-10-30 08:08  | [463. 岛屿的周长](https://leetcode-cn.com/problems/island-perimeter) | EASY | 2 |
| 2020-10-29 13:53  | [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | HARD | 1 |
| 2020-10-29 13:23  | [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | HARD | 5 |
| 2020-10-29 12:25  | [面试题 01.01. 判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci) | EASY | 4 |
| 2020-10-29 11:00  | [129. 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 4 |
| 2020-10-28 11:19  | [1207. 独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences) | EASY | 3 |
| 2020-09-09 15:21  | [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | HARD | 1 |
| 2020-09-09 15:00  | [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive) | HARD | 2 |
| 2020-09-09 14:02  | [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii) | MEDIUM | 2 |
| 2020-09-09 13:34  | [39. 组合总和](https://leetcode-cn.com/problems/combination-sum) | MEDIUM | 1 |
| 2020-09-09 13:18  | [面试题 01.02. 判定是否互为字符重排](https://leetcode-cn.com/problems/check-permutation-lcci) | EASY | 3 |
| 2020-08-16 12:43  | [1535. 找出数组游戏的赢家](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game) | MEDIUM | 1 |
| 2020-08-16 10:42  | [1534. 统计好三元组](https://leetcode-cn.com/problems/count-good-triplets) | EASY | 1 |
| 2020-08-16 10:33  | [405. 数字转换为十六进制数](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal) | EASY | 6 |
| 2020-07-30 16:18  | [1114. 按序打印](https://leetcode-cn.com/problems/print-in-order) | EASY | 7 |
| 2020-07-30 15:49  | [1179. 重新格式化部门表](https://leetcode-cn.com/problems/reformat-department-table) | EASY | 2 |
| 2019-04-06 15:23  | [703. 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | EASY | 5 |
| 2019-04-06 15:13  | [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | MEDIUM | 5 |
| 2019-04-06 12:17  | [194. 转置文件](https://leetcode-cn.com/problems/transpose-file) | MEDIUM | 1 |
| 2018-09-28 07:47  | [492. 构造矩形](https://leetcode-cn.com/problems/construct-the-rectangle) | EASY | 1 |
| 2018-09-26 13:47  | [380. O(1) 时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) | MEDIUM | 1 |
| 2018-09-26 13:34  | [414. 第三大的数](https://leetcode-cn.com/problems/third-maximum-number) | EASY | 1 |
| 2018-09-21 08:24  | [67. 二进制求和](https://leetcode-cn.com/problems/add-binary) | EASY | 1 |
| 2018-08-31 07:01  | [307. 区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable) | MEDIUM | 1 |
| 2018-08-31 06:57  | [303. 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable) | EASY | 1 |
| 2018-08-31 06:41  | [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n) | MEDIUM | 6 |
| 2018-08-29 10:23  | [443. 压缩字符串](https://leetcode-cn.com/problems/string-compression) | MEDIUM | 2 |
| 2018-08-29 09:33  | [38. 外观数列](https://leetcode-cn.com/problems/count-and-say) | MEDIUM | 14 |
| 2018-08-29 07:48  | [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 4 |
| 2018-08-27 08:44  | [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 7 |
| 2018-08-27 08:21  | [107. 二叉树的层序遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) | MEDIUM | 1 |
| 2018-08-27 08:11  | [637. 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) | EASY | 3 |
| 2018-08-27 03:01  | [804. 唯一摩尔斯密码词](https://leetcode-cn.com/problems/unique-morse-code-words) | EASY | 1 |
| 2018-08-25 02:48  | [645. 错误的集合](https://leetcode-cn.com/problems/set-mismatch) | EASY | 11 |
| 2018-08-23 17:45  | [100. 相同的树](https://leetcode-cn.com/problems/same-tree) | EASY | 1 |
| 2018-08-23 17:33  | [485. 最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | EASY | 1 |
| 2018-08-22 12:23  | [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 7 |
| 2018-08-22 08:28  | [262. 行程和用户](https://leetcode-cn.com/problems/trips-and-users) | HARD | 1 |
| 2018-08-22 08:13  | [601. 体育馆的人流量](https://leetcode-cn.com/problems/human-traffic-of-stadium) | HARD | 2 |
| 2018-08-22 08:07  | [177. 第N高的薪水](https://leetcode-cn.com/problems/nth-highest-salary) | MEDIUM | 4 |
| 2018-08-22 07:53  | [180. 连续出现的数字](https://leetcode-cn.com/problems/consecutive-numbers) | MEDIUM | 3 |
| 2018-08-22 07:32  | [185. 部门工资前三高的所有员工](https://leetcode-cn.com/problems/department-top-three-salaries) | HARD | 1 |
| 2018-08-22 07:12  | [626. 换座位](https://leetcode-cn.com/problems/exchange-seats) | MEDIUM | 1 |
| 2018-08-22 06:55  | [184. 部门工资最高的员工](https://leetcode-cn.com/problems/department-highest-salary) | MEDIUM | 9 |
| 2018-08-22 06:49  | [178. 分数排名](https://leetcode-cn.com/problems/rank-scores) | MEDIUM | 1 |
| 2018-08-22 06:22  | [9. 回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 1 |
| 2018-08-22 06:17  | [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer) | MEDIUM | 3 |
| 2018-08-22 03:44  | [182. 查找重复的电子邮箱](https://leetcode-cn.com/problems/duplicate-emails) | EASY | 1 |
| 2018-08-22 03:41  | [181. 超过经理收入的员工](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers) | EASY | 2 |
| 2018-08-22 03:35  | [596. 超过5名学生的课](https://leetcode-cn.com/problems/classes-more-than-5-students) | EASY | 2 |
| 2018-08-22 02:52  | [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change) | EASY | 1 |
| 2018-08-21 16:03  | [620. 有趣的电影](https://leetcode-cn.com/problems/not-boring-movies) | EASY | 3 |
| 2018-08-21 11:05  | [192. 统计词频](https://leetcode-cn.com/problems/word-frequency) | MEDIUM | 1 |
| 2018-08-21 10:59  | [193. 有效电话号码](https://leetcode-cn.com/problems/valid-phone-numbers) | EASY | 8 |
| 2018-08-21 10:36  | [195. 第十行](https://leetcode-cn.com/problems/tenth-line) | EASY | 12 |
