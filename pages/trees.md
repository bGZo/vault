---
draft: true
title: Trees
aliases:
  - trees
  - 树
created: 2025-02-03T15:17:52
modified: 2025-02-03T16:14:50
description: 这种数据结构看起来像是一个倒挂的树，因此得名
tags: 
type: data-structure
---
## 应用

- 树是分层 (Hierarchical) 结构，和其他线性结构不同，用处主要有：
    - organization hierarchy
    - directory structure
    - database indexes

## 定义

- **森林 (forest)**：每个连通分量（连通块）都是树的图。按照定义，一棵树也是森林
- 连通分量 (Connected Component), 任何连通图的连通分量只有一个，即是其自身，非连通的无向图有多个连通分量
- **生成树（spanning tree）**：一个连通无向图的生成子图，同时要求是树。也即在图的边集中选择 $n-1$ 条，将所有顶点连通
- **无根树的叶结点（leaf node）**：度数不超过 $1$ 的结点
- **有根树的叶结点（leaf node）**：没有子结点的结点

### **无根树** (unrooted tree): 一个没有固定根结点的树

![sm](https://raw.githack.com/bGZo/assets/dev/2025/202502031535628.png)

- 无根树有几种等价的形式化定义：
    - 有 $n$ 个结点，$n-1$ 条边的连通无向图
    - 无向无环的连通图
    - 任意两个结点之间有且仅有一条简单路径的无向图
    - 任何边均为桥的连通图
    - 没有圈，且在任意不同两点间添加一条边之后所得图含唯一的一个圈的图

### 有根树 (rooted tree): 在无根树的基础上，指定一个结点称为根

有根树在很多时候仍以无向图表示，只是规定了结点之间的上下级关系

#### 只适用于有根树的定义

- 节点 Nodes
- 边 Edges
- 叶子节点 Leaf nodes
- 根节点 Root nodes
- 父节点 Parent nodes
    - 子节点 Child nodes
        - 子结点的顺序一般不加以区分，二叉树是一个例外。
- 树高 height

![Tree Data Structure _ Illustrated Data Structures - YouTube_1'48.481''.jpg](https://raw.githack.com/bGZo/assets/dev/2025/202502031526306.png)

- **祖先 (ancestor)**：一个结点到根结点的路径上，除了它本身外的结点。 根结点的祖先集合为空。
- **结点的深度 (depth)**：到根结点的路径上的边数。
- **兄弟 (sibling)**：同一个父亲的多个子结点互为兄弟。
- **后代 (descendant)**：子结点和子结点的后代；
    - 或者理解成：如果 $u$ 是 $v$ 的祖先，那么 $v$ 是 $u$ 的后代。

![](https://raw.githack.com/bGZo/assets/dev/2025/202502031544603.png)

- **子树 (subtree)**：删掉与父亲相连的边后，该结点所在的子图

![](https://raw.githack.com/bGZo/assets/dev/2025/202502031546748.png)

### 特殊的树

#### 有根二叉树（rooted binary tree）

每个结点最多只有两个儿子（子结点）的有根树称为二叉树。常常对两个子结点的顺序加以区分，分别称之为左子结点和右子结点

大多数情况下，**二叉树** 一词均指有根二叉树

#### 完整二叉树（full/proper binary tree）

每个结点的子结点数量均为 0 或者 2 的二叉树

换言之，每个结点或者是树叶，或者左右子树均非空

![](https://raw.githack.com/bGZo/assets/dev/2025/202502031553059.png)

#### **完全二叉树（complete binary tree）**

只有最下面两层结点的度数可以小于 2，且最下面一层的结点都集中在该层最左边的连续位置上

![](https://raw.githack.com/bGZo/assets/dev/2025/202502031558817.png)

#### 完美二叉树（perfect binary tree）

所有叶结点的深度均相同的二叉树称为完美二叉树

![](https://raw.githack.com/bGZo/assets/dev/2025/202502031559785.png)

#### 搜索二叉树（Binary search tree）

![Tree Data Structure _ Illustrated Data Structures - YouTube_3'59.092''.jpg](https://raw.githack.com/bGZo/assets/dev/2025/202502031611778.png)

- 平衡搜索二叉树
- 非平衡搜索二叉树

![Tree Data Structure _ Illustrated Data Structures - YouTube_7'1.934''.jpg](https://raw.githack.com/bGZo/assets/dev/2025/202502031614672.png)

#### Others

- **链（chain/path graph）**：满足与任一结点相连的边不超过 $2$ 条的树称为链。
- **菊花/星星（star）**：满足存在 $u$ 使得所有除 $u$ 以外结点均与 $u$ 相连的树称为菊花

## 存储

  - 邻接表
    - 无根树: 为每个结点开辟一个线性列表，记录所有与之相连的结点
    - 有根树
      - 无向图: 可以用上述线性列表形式存储,
      - 若输入数据能够确保结点的上下关系，则可以利用这个信息。为每个结点开辟一个线性列表，记录其所有子结点；若有需要，还可在另一个数组中记录其父结点。
        - 链表也可以替代 `std:vector`
  - ?左孩子右兄弟表示法
    - 有根树
    - 步骤
      - 看给每个结点的所有子结点任意确定一个顺序。
      - 此后为每个结点记录两个值：其 **第一个子结点** `child[u]` 和其 **下一个兄弟结点** `sib[u]`
        - 若没有子结点，则 `child[u]` 为空
        - 若该结点是其父结点的最后一个子结点，则 `sib[u]` 为空
    - 遍历可实现
  - ?只记录父结点
    - 用一个数组 `parent[N]` 记录每个结点的父亲结点。
    - 这种方式可以获得的信息较少，不便于进行自顶向下的遍历。常用于自底向上的递推问题中。
  - ?二叉树
    - 需要记录每个结点的左右子结点

## 遍历

- 树上 DFS
- 二叉树上 DFS
    - 先序遍历 (Inorder)
    - 中序遍历 (Preorder)
    - 后序遍历 (Postorder)
- 反推: 已知中序遍历序列和另外一个序列可以求第三个序列
- 树上 BFS
- 无根树
    - 由于树是无环图，因此只需记录当前结点是由哪个结点访问而来，此后进入除该结点外的所有相邻结点，即可避免重复访问
- 有根树

## References

<iframe src="https://www.youtube.com/embed/S2W3SXGPVyU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<center>via: <a href='https://www.youtube.com/watch?v=S2W3SXGPVyU' target='_blank' class='external-link'>https://www.youtube.com/watch?v=S2W3SXGPVyU</a></center>

- [树基础 - OI Wiki](https://oi-wiki.org/graph/tree-basic/#%E6%A0%91%E4%B8%8A-dfs)
- [二叉树：前序遍历、中序遍历、后续遍历 图：深度优先（DFS）、广度优先（BFS）](https://blog.csdn.net/weixin_43357638/article/details/99730284)

aliases: maths/graph/tree
