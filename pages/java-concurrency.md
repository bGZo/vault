---
draft: true
aliases:
  - Java 并发
  - Java Concurrency
created: 2024-12-08T21:26:22
modified: 2025-08-30T17:07:55
title: Java 并发
---
# Java 并发

## `sleep()` #vs `wait()` [[java-interview]]

| **Items**  | `sleep()`                       | `wait()`                                    |
| ---------- | ------------------------------- | ------------------------------------------- |
| **暂停执行线程** | ✔                               | ✔                                           |
| **释放锁**    | ❌                               | ✔                                           |
| **使用场景**   | 暂停执行                            | 线程间交互/通信                                    |
| **线程苏醒**   | `wait(long timeout)` <br> 自动苏醒 | 其他线程调用同一个对象上的 <br>`notify()`/`notifyAll()` |
| **方法包名**   | `Thread` 类的静态本地方法　              | `Object` 类的本地方法                             |

- 释放锁意味着其他线程可以访问该资源, 两者都会让出 CPU 给其他线程使用, Sleep() 等待结束后进入就绪状态, wait() 则持续等待唤醒.
- 包名为什么这么设计?
  - `wait()` 让获得对象锁的线程实现等待，会自动释放当前线程占有的对象锁
    - 每个对象（ `Object` ）都拥有对象锁，既然要释放当前线程占有的对象锁并让其进入 [ ] #gtd/wait 状态，自然是要操作对应的对象（ `Object` ）而非当前的线程（ `Thread` ）。
  - `sleep()` 是让当前线程暂停执行，不涉及到对象类，也不需要获得对象锁。

## References

- GeekBang - Java 核心技术 36 讲 - 杨晓峰 - 第 19 讲 | Java 并发包提供了哪些并发工具类
- [Java 并发常见面试题总结（上） | JavaGuide](https://javaguide.cn/java/concurrent/java-concurrent-questions-01.html#%E8%AE%A4%E8%AF%86%E7%BA%BF%E7%A8%8B%E6%AD%BB%E9%94%81)
