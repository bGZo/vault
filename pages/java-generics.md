---
aliases:
  - Java Generics
  - java泛型
created: 2024-08-02T00:00:00
description: 
modified: 2025-08-30T16:50:42
title: Java Generics
wikipedia: https://en.wikipedia.org/wiki/Generics_in_Java
---

# Java Generics

拓展 Java 类型系统，允许对各类型对象进行操作，提供编译时类型安全；

## Motivation1 / 问题代码 1

```java
final List v = new ArrayList();
v.add("test"); // A String that cannot be cast to an Integer
final Integer i = (Integer) v.get(0); // Run time error
```

### Better way on java05

```java
final List<String> v = new ArrayList<String>();
v.add("test");
final Integer i = (Integer) v.get(0); // (type error)  compilation-time error
```

### Better `type inference`(类型推断) on java07

```java
final Entry<String, String> grade = new Entry<>("Mike", "A");
final Entry<String, Integer> mark = new Entry<>("Mike", 100);
System.out.println("grade: " + grade);
System.out.println("mark: " + mark);

final Entry<Integer, Boolean> prime = new Entry<>(13, true);
if (prime.getValue()) System.out.println(prime.getKey() + " is prime.");
else System.out.println(prime.getKey() + " is not prime.");
```

### Type wildcards (类型通配符)

```java
final Collection<?> c = new ArrayList<String>();
c.add(new Object()); // compile-time error
c.add(null); // allowed
```

## 问题代码 2

```java
final List<Integer> ints = new ArrayList<>();
ints.add(2);
final List<Number> nums = ints;  // valid if List<Integer> were a subtype of List<Number> according to substitution rule. 
nums.add(3.14);  
final Integer x = ints.get(1); // now 3.14 is assigned to an Integer variable!
```

### 规定上限 => `extends` => 保证读取安全，但限制了写操作 (只能存入)

```java
final List<? extends Number> nums = ints;  // OK
nums.add(3.14); // compile-time error
nums.add(null); // allowed
```

### 规定下限 => `super` => Number 的任何子类 => 保证了写操作，但限制了读操作

```java
List<? super Integer> list = new ArrayList<Number>();
list.add(1);    // OK
list.add(2);    // OK

Number n = list.get(0);  // 编译错误
Integer i = list.get(0); // 编译错误
Object o = list.get(0);  // OK
```

### **Type erasure** (类型擦除)

```java
final List<Integer> li = new ArrayList<>();
final List<Float> lf = new ArrayList<>();
if (li.getClass() == lf.getClass()) { // evaluates to true
  System.out.println("Equal");
}
```

  - 以上代码片段将输出 `Equal`，类型检查只会发生在编译期，运行时的代码无法判断泛型的具体内容；
  - **不支持 `extends Throwable`**，当走到 catch 块之后，无法判断进入到哪一分支

```java
try {
  throw new GenericException<Integer>();
} catch (GenericException<Integer> e) {
  System.err.println("Integer");
} catch (GenericException<String> e) {
  System.err.println("String");
}
```

  - **不支持实例化泛型**，如下述代码将无法通过编译

```java
<T> T instantiateElementType(List<T> arg) {
return new T(); //causes a compile error
}
```

### **Vs Array** (比较于数组)

- 因为类型擦除，运行时的数组的类型信息要比泛型更加具体；
- > Arrays are reified, meaning that an array object enforces its type information at run-time, whereas generics in Java are not reified.

## Reference

- [泛型和反射 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1265105940850016)
	- 我们不能直接创建泛型数组 `T[]`，因为擦拭后代码变为 `Object[]`
	- 带泛型的数组实际上是编译器的类型擦除
