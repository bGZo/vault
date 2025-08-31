---
aliases:
  - java 集合
  - java 容器
  - Java 容器
  - java collections
created: 2025-06-10T22:36:41
modified: 2025-08-30T18:26:21
title: Java 容器
---

# Java 容器

a framework that provides an architecture to store and manipulate(操纵) the group of objects, start from java02

> [!note]
> 灵活性 (存储, 类型, 数量, 映射关系) > 数组

## - Map/Hierarchy of Collection Framework
  - Iterable
    - Collection
      - List
        - Vector
          - Stack
        - ArrayList
        - LinkedList
      - Queue
        - Deque
          - LinkedList
          - ArrayDeque
        - PriorityQueue
      - Set
        - SortedSet
          - TreeSet
        - HashSet
          - LinkedHashSet
  - Map
    - HashTable
    - HashMap
    - SortedMap
      - TreeMap
  - ![[image_1652522212837_0.png]]
    (省略了 AbstractList, NavigableSet 等抽象类以及其他的一些辅助)
  - [[java-interview]]
    - Map 没有继承 iterable, 却可以使用迭代器?
      - Map 及其子类虽然没有实现 Interable、Iterator，但是，Map 内部生成 Collection，从而间接实现 Iterable 接口和生成 Iterator，所以，Map 也可以使用迭代器。
      - via: [map没有继承iterable，为什么可以使用迭代器_百度知道](https://zhidao.baidu.com/question/1771462425941801540.html)
## - Implements
  - Collection
    - List
      - **List** 均按添加时的顺序存放，不自动排序
      - Vector vs ArrayList
        - | **Items** | **Vector**| **Arraylist** |
          | **底层** | `Object[]`|
          | **地位** | 古老实现 | 主要实现 |
          | **线程安全** | ✖ | ✔ |
      - ArrayList vs LinkedList
        - | **Items** | **Arraylist** | **LinkedList** |
          | **线程安全** | ✖| ✖|
          | **底层** | Object [] | ~~循环链表~~ 双向链表 (>=JDK1.7) |
          | **插/删 受元素位置影响** | ✔ O(n/2) | ✖ O(1) |
          | **快速随机访问** | ✔| ✖|
          | **内存占用** | 结尾需要预留出空间 | 原子元素更多 (前驱后继)|
      - Vector vs ArrayList vs LinkedList
        - 三者都是有序集合, 功能也比较近似, 但在行为、性能、线程安全等方面，有很大不同 (具体设计)
        - Vector 是 Java 早期提供的 **线程安全的动态数组** ，如果不需要线程安全，并不建议选择，毕竟同步是有额外开销的。Vector 内部是使用对象数组来保存数据，可以根据需要自动的增加容量，当数组已满时，会创建新的数组，并拷贝原有数组数据。
        - ArrayList 是应用更加广泛的 **动态数组** 实现，它本身不是线程安全的，所以性能要好很多。与 Vector 近似，ArrayList 也是可以根据需要调整容量，不过两者的调整逻辑有所区别，Vector 在扩容时会提高 1 倍，而 ArrayList 则是增加 50%。
        - LinkedList 顾名思义是 Java 提供的 **双向链表** ，所以它不需要像上面两种那样调整容量，它也不是线程安全的。
      - ArrayList 的扩容机制
      - RandomAccess 接口
    - Queue
      - Queue vs Deque
        - | **Queue 接口** | **抛出异常** | **返回特殊值** |
            | ------------ | --------- | ---------- |
            | **插入队尾** | add(E e) | offer(E e) |
            | **删除队首** | remove() | poll() |
            | **查询队首元素** | element() | peek() |
        - | **Deque 接口** | **抛出异常** | **返回特殊值** |
            | ------------ | ------------- | --------------- |
            | **插入队首** | addFirst(E e) | offerFirst(E e) |
            | **插入队尾** | addLast(E e) | offerLast(E e) |
            | **删除队首** | removeFirst() | pollFirst() |
            | **删除队尾** | removeLast() | pollLast() |
            | **查询队首元素** | getFirst() | peekFirst() |
            | **查询队尾元素** | getLast() | peekLast() |
          - Deque 还提供有 push() 和 pop() 等其他方法，可用于模拟栈
      - ArrayDeque vs LinkedList
        - | **Items** | **ArrayDeque** | **LinkedList** |
          | **Deque 接口** | ✔|✔|
          | **队列性质**| ✔|✔|
          | **底层** | 可变长数组和双指针 | 链表 |
          | **存储 NULL 数据** | ✖|✔|
          | **JDK** | >=1.6 | >=1.2|
          | **性能**|除扩容外, O(1)| 申请堆空间, 更慢|
        - ArrayDeque 也可以用于实现栈
      - PriorityQueue
        - \>= JDK1.5
        - 二叉堆
          - 底层使用可变长的数组来存储数据
        - 堆元素的上浮和下沉
          - O(logn) 的时间复杂度内插入元素和删除堆顶元素
        - 非线程安全的
          - 不支持存储 NULL 和 non-comparable 的对象
        - 默认是小顶堆，但可以接收一个 Comparator 作为构造参数，从而来自定义元素优先级的先后
      - [ ] #gtd/todo 手撕算法, 堆排序、求第 K 大的数、带权图的遍历
    - Set
      - **Set** 默认按自然顺序排序，可通过构造器传入自定义的比较器自定义排序策略，**但是，**LinkedHashSet 无序
      - HashSet vs LinkedHashSet vs TreeSet
        - | **Items** | **HashSet** | **LinkedHashSet** | **TreeSet**|
          | **Set 接口实现**| ✔|✔ |✔ |
          | **元素唯一**| ✔| ✔| ✔|
          | **线程安全**|✖|✖|✖|
          | **底层** | 哈希表 `HashMap` | 链表 (FIFO) + 哈希表 | 红黑树 (有序) |
          | **应用场景** | 不保证元素顺序| 保证顺序满足 FIFO | 自定义排序 |
      - `comparable` vs `Comparator`
        - `comparable` 接口
          - from: java.lang 包
          - `compareTo(Object obj)` 排序
        - `comparator` 接口
          - from: `java.util` 包
          - `compare(Object obj1, Object obj2)` 排序
      - 无序性 / 不可重复性 含义
        - 无序性
          - 存储的数据在底层数组中并非按照数组索引的顺序添加 ，而是根据数据的哈希值决定的
        - 不可重复性
          - 添加的元素按照 equals() 判断时 ，返回 false，需要同时重写 equals() 方法和 HashCode() 方法
  - Map
    - **HashMap, TreeMap, ConcurrentHashMap 是有序的**
    - ~~**Hashtable, LinkedHashMap 不是有序的**~~
    - HashMap vs HashTable
      - | **Items** | **HashMap** | **Hashtable** |
        | **线程安全** | ✖ | ✔ (`synchronized` 修饰)|
        | **效率**(基于第一点) | 较高 | 遗留类, 很多冗余, 不如用<br> `ConcurrentHashMap`|
        | **Null key / Null value** | ✔|✖|
        | **初始 / 扩容 容量**| 16-> 16*2; N->$$2^{N}$$(`tableSizeFor()`) | 11->2n+1|
        | **底层** | >=1.8, 链表长>8, 数组>64, 转换红黑树 | ✖|
    - HashMap vs HashSet
      - | **HashMap** | **HashSet** |
        | :------------------------------------: | :----------------------------------------------------------: |
        | 实现了 `Map` 接口 | 实现 `Set` 接口 |
        | 存储键值对 | 仅存储对象 |
        | 调用 `put()` 向 map 中添加元素 | 调用 `add()` 方法向 `Set` 中添加元素 |
        | `HashMap` 使用键（Key）计算 `hashcode` | `HashSet` 使用成员对象来计算 `hashcode` 值，对于两个对象来说 `hashcode` 可能相同，所以 `equals()` 方法用来判断对象的相等性 |
    - HashMap vs TreeMap
      - ![[image_1652685166712_0.png]]
  - 底层 -> List vs Set vs Queue vs Map
    - List
      - `Arraylist`
        - `Object[]` 数组
      - `Vector`
        - `Object[]` 数组
      - `LinkedList`
        - 双向链表 (JDK1.6 之前为循环链表，JDK1.7 取消了循环)
    - Set
      - `HashSet`(无序，唯一)
        - 基于 `HashMap` 实现的，底层采用 `HashMap` 来保存元素
      - `LinkedHashSet`
        - `HashSet` 的子类
        - 内部是通过 `LinkedHashMap` 实现的。有点类似于我们之前说的 `LinkedHashMap` 其内部是基于 `HashMap` 实现一样，不过还是有一点点区别的
      - `TreeSet`(有序，唯一)
        - 红黑树 (自平衡的排序二叉树)
    - Queue
      - `PriorityQueue`
        - `Object[]` 数组来实现二叉堆
      - `ArrayQueue`
        - `Object[]` 数组 + 双指针
    - Map
      - `HashMap`
        - [[java08]] 之前：数组 + 链表
          - 数组是主体
          - 链表为了解决哈希冲突而存在（“拉链法”解决冲突）
        - [[java08]] 之后，当链表长度 (冲突长度) > 阈值 (8)
          - 将链表转化为红黑树
          - > [!note]
            > 转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树

      - `LinkedHashMap` extends HashMap
        - 继承自 ``
        - 底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成
        - 另外，`LinkedHashMap` 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。
        - [《LinkedHashMap 源码详细分析（JDK1.8）》](https://www.imooc.com/article/22931)
      - `Hashtable`
        - 数组 + 链表组成的，数组是 `Hashtable` 的主体，链表则是主要为了解决哈希冲突而存在的
      - `TreeMap`
        - 红黑树（自平衡的排序二叉树）
## Refs
- [Collections in Java - javatpoint](https://www.javatpoint.com/collections-in-java)
- [极客时间 | Java核心技术36讲](http://www.gcjlovecl.ltd/02-Java%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF36%E8%AE%B2/02-%E6%A8%A1%E5%9D%97%E4%B8%80%20Java%E5%9F%BA%E7%A1%80%20%2814%E8%AE%B2%29/%E7%AC%AC08%E8%AE%B2%E4%B8%A8%E5%AF%B9%E6%AF%94Vector%E3%80%81ArrayList%E3%80%81LinkedList%E6%9C%89%E4%BD%95%E5%8C%BA%E5%88%AB%EF%BC%9F.html)
- [你必须知道的几种java容器（集合类）_晚秋星辰的博客-CSDN博客](https://blog.csdn.net/dengpeng0419/article/details/47983033)
- [Java 集合存入数据时会自动排序吗？ - 知乎](https://zhuanlan.zhihu.com/p/55840526)
- [ConcurrentMap 是一个接口，它是 Map 接口的扩展](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[。它的目的是提供一个结构和指导，来解决吞吐量和线程安全之间的问题](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[。通过覆盖一些接口默认方法，ConcurrentMap 给出了有效实现的指导，以提供线程安全和内存一致性的原子操作](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[2](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html)[1](https://www.baeldung.com/java-concurrent-map)。
- [ConcurrentHashMap 是一个 Java 类，它实现了 ConcurrentMap 和 Serializable 接口](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[1](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[。它是 HashMap 的一个改进，可以在多线程环境下提高性能](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[1](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[2](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[。ConcurrentHashMap 允许多个线程并发地访问 map，而不需要对整个 map 加锁，只需要对 map 的一部分（称为 Segment）加锁](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[2](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[3](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)[。ConcurrentHashMap 还可以用作可扩展的频率 map（一种直方图或多重集合），通过使用 LongAdder 值和 computeIfAbsent 方法](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)[3](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)。
