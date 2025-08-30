---
aliases:
  - Java Lambda
  - Java Lambda (since java08)
created: 2024-08-05T00:00:00
modified: 2025-08-30T17:10:41
title: Java Lambda (since java08)
---

# Java Lambda (since java08)

## Why

## How

- java-stream

## What

Lambda 表达式是一种用于取代匿名类，把函数行为表述为函数式编程风格的一种匿名函数，Lambda 表达式的执行结果是函数式接口的一个匿名对象；Lambda 允许把函数作为一个方法的参数（函数作为参数传递到方法中）

- 来源
  - λ[læ:mdə] 演算
- 使用前提
  - 函数式接口
    - 只有一个（抽象方法）的接口
- 函数式编程
  - 函数是“第一等公民”
    - 级别和 Java 类相同
  - 效果
    - 可以赋值给变量
    - 可以作为（其它函数的）参数进行传递
    - 可以作为（其它函数的）返回值
- 语法

```shell
(parameters) -> { statements; }
(parameters) -> expression
```

- 局限
  - Lambda **不算 Java 中的语法糖**；
    - 在敏感场景，如初始化开销时会体现差距
      - 原因：在首次调用时，JVM 需要为其构建 [CallSite](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/CallSite.html) 实例；
  - Lambda 打断点复杂，程序栈很复杂；
- 用例
    - 匿名内部类

```java
public class AnonymousInnerClass {
  public static void main(String... args) {
    List<String> strList = Arrays.asList("1", "2", "3");
    strList.forEach(new Consumer<String>() {
      @Override
      public void accept(String s) {
        System.out.println(s);
      }
    });
  }
}
```

- `Lambda` 表达式

```java
public class LambdaTest {
  public static void main(String... args) {
    List<String> strList = Arrays.asList("1", "2", "3");
    strList.forEach(s -> {
      System.out.println(s);
    });
  }
}
```

- 原理
  - > 1. Lambda 表达式底层是用内部类来实现的
    2. 该内部类实现了 * 某个（根据 Lambda 所属的代码指定）* 函数式接口，并重写了该接口的抽象方法
    3. 该内部类是在程序运行时使用 ASM 技术动态生成的，所以编译期没有对应的.class 文件，但是我们可以通过设置系统属性将该内部类文件转储出来
  - Java07 在 [JSR 292](https://jcp.org/en/jsr/detail?id=292) 中增加了对动态类型语言的支持，使得 Java 也可以像*C 语言*那样将方法作为参数传递，其实现在 `java.lang.invoke` 包中。它的核心就是 `invokedynamic` 指令，为后面**函数式编程**和**响应式编程**提供了前置支持。
  - `invokedynamic` 指令对应的执行方法会关联到一个*动态*调用点对象（`java.lang.invoke.CallSite`），一个调用点（`call site`）是一个方法句柄（method handle，调用点的目标）的持有者，这个调用点对象会指向一个具体的引导方法（`bootstrap method`，比如 `metafactory()`），引导方法成功调用之后，调用点的目标将会与它持有的方法句柄的引用永久绑定，最终得到一个实现了函数式接口（比如 `Consumer`）的对象
  - Lambda 表达式在编译期进行脱糖（desugar），它的主体部分会被转换成一个脱糖方法（desugared method，即 `lambda$main$0`），这是一个合成方法，如果 Lambda 没有用到外部变量，则是一个私有的静态方法，否则将是个私有的实例方法——synthetic 表示不在源码中显示，并在 Lambda 所属的方法（比如 main 方法）中生成 `invokedynamic` 指令
  - **进入运行期**，`invokedynamic` 指令会调用引导方法 `metafactory()` 初始化 ASM 生成内部类所需的各项属性，然后由 `spinInnerClass()` 方法组装内部类并用 Unsafe 加载到 JVM，通过构造方法实例化内部类的实例（Lambda 的实现内部类的构造是私有的，需要手动设置可访问属性为 true），最后绑定到方法句柄，完成调用点的创建
  - 你可以把调用点看成是函数式接口（例如 Consumer 等）的匿名对象，当然，内部类是确实存在的——比如 `final class LambdaTest$$Lambda$1 implements Consumer`。值得注意的是，内部类的实现方法里并没有 Lambda 表达式的任何操作，它不过是调用了脱糖后定义在调用点目标类（`targetClass`，即 `LambdaTest` 类）中的合成方法（即 `lambda$main$0`）而已，这样做使得内部类的代码量尽可能的减少，降低内存占用，对效率的提升更加稳定和可控
  - > Lambda 表达式在编译期脱去糖衣语法，生成了一个“合成方法”，在运行期，`invokedynamic` 指令通过引导方法创建调用点，过程中生成一个实现了函数式接口的内部类并返回它的对象，最终通过调用点所持有的方法句柄完成对合成方法的调用，实现具体的功能。
- 常用接口

```shell
Runnable / Callable
Supplier / Consumer
Comparator
Predicate
Function
```

## Reference

  - 马士兵
