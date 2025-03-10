---
description: Java is a general-purpose, class-based, object-oriented programming language designed for having lesser implementation dependencies. It is a computing platform for application development. Java is fast, secure, and reliable. Therefore, it is widely used for developing Java applications in laptops, data centers, game consoles, scientific supercomputers, cell phones, etc. 静态强类型，但因为提供了类似反射等机制，也具备了部分动态类型语言的能力；
type: lang/programming
created: 2024-12-08T21:26:22
modified: 2025-03-10T21:25:43
---

## Roadmap

![[java.pdf]]

## Basics

### Basic Syntax

- To print output use —> `System.out.println();`
- To take input from user —> `Scanner` or `BufferedReader` class can be used

### Lifecycle of a Program 程序的生命周期

![](https://raw.githack.com/bGZo/assets/dev/2025/202503102006777.png)

When the program runs, the Java Virtual Machine (JVM) loads these compiled class files into memory through a process involving loading of binary data, linking for verification and preparation, and initialization of class elements.

The JVM then verifies the bytecode’s security compliance, performs Just-In-Time (JIT) compilation to translate bytecode into native machine code for better performance, and executes the program instructions while managing system resources.

More via: https://www.cesarsotovalero.net/blog/how-the-jvm-executes-java-code.html

### Data Types (two group)

- Primitive (原始类型) - `byte`,`short`,`int`,`long`,`float`,`double`,`boolean` and `char`
- Non-Primitive - `String`, `Arrays`, `Classes`, `Enums` and `Records`

### Variables and Scopes  变量和作用域

Variable in Java is a data container that stores the data values during Java program execution.

The Java variables have mainly three types:

1. Local
2. Instance
3. Static

### Type Casting 类型转换

In Java, type casting can be either implicit (automatic) or explicit (requiring a cast operator).

### Strings and Methods  字符串和方法

### Math Operations  数学运算

https://jenkov.com/tutorials/java/math-operators-and-math-class.html

#### Java Floating Point Math  Java 浮点数学

```java
double result = 100 / 8;
```

Even though the `result` variable is now a floating point type (`double`), the final result is still just 12 instead of 12.5 . The reason for that is that the two values in the math expression (100 and 8) are both integers. Thus, the result of dividing one by the other is first converted to an integer (12) before being assigned to the `result` variable.

> [!NOTE] Floating Point Precision  浮点精度
> Usually the Java floating point imprecision is insignificant, but it is still important to be aware of it.

```java
double resultDbl3 = 0D;
System.out.println("resultDbl3 = " + resultDbl3);

for(int i=0; i<100; i++){
    resultDbl3 += 0.01D;
}
System.out.println("resultDbl3 = " + resultDbl3);
/**
resultDbl3 = 0.0
resultDbl3 = 1.0000000000000007
*/
```

### Arrays

Store a collection of elements of the same data type in contiguous memory locations(连续的内存位置).

#### Java Array Literals  Java 数组文字

```
int[] ints2 = { 1,2,3,4,5,6,7,8,9,10 };
```

### Conditionals

- `if`
- `else`
- `else if`
- `switch`
- `?,:`

### Loops

1. `for`
2. `forEach`
3. `while`
4. `do...while`.

### Functions

A block of code written to perform a specific task repeatedly.

It provides reusability of code. We write the function once and use it many times.

It works on the ‘DRY’ principle i.e., “Do not repeat yourself”.

1. Define function - `datatype function_name(parameters){body}`
2. Call function - `function_name(values)`
3. Lambda functions - `x -> x + 1`
4. Pass a function as a variable -

```java
final Consumer<Integer> simpleReference1 = App::someMethod1;  
simpleReference1.accept(1);
```

### Working with Date and Time in Java

Before Java 8 packages:

- `java.util.Date`
- `java.util.Calendar`
- `java.text.SimpleDateFormat`
- `java.util.TimeZone`

Problems:

1. `Date` 缺少小时、分钟、秒；
2. 以零索引命名 (a zero index-based) 的月份比较混乱；
3. 没有考虑时区的问题，而 JDBC 中处理时间有时区的概念

After Java 8:

- **java.time.LocalDate** — This represents only the time according to the ISO calendar.
- **java.time.LocalTime** — This represents only the time in a human-readable manner.
- **java.time.LocalDateTime** — Both the Date and Time without having a time zone will be handled here. This is a combination of _LocalDate_ and _LocalTime._
- **java.time.ZonedDateTime** — _LocalDateTime_ combines with the time zone provided using _ZoneId_ class.
- **java.time.OffsetTime** — Handles time with a corresponding time zone offset from Greenwich/UTC, without a time zone ID.
- **java.time.OffsetDateTime** — Handles a date and time with a corresponding time zone offset from Greenwich/UTC, without a time zone ID.
- **java.time.Clock** — Provides access to the current instant, date, and time in any given time zone.
- **java.time.Instant** — represents the start of a nanosecond on the timeline and useful for generating a timestamp to represent machine time
- **java.time.Duration** — Difference between two instants and measured in seconds or nanoseconds and does not use date-based constructs such as years, months, and days, though the class provides methods that convert to days, hours, and minutes.
- **java.time.Period** — To define the difference between dates in date-based values (years, months, days).
- **java.time.ZoneId** — specifies a time zone identifier and provides rules for converting between an _Instant_ and a _LocalDateTime_.
- **java.time.ZoneOffset** — Specifies a time zone offset from Greenwich/UTC.

```java
import java.time.*;

public class DateTimeExample {
    public static void main(String[] args){
        LocalDate today = LocalDate.now(); // 2021-05-04
        LocalTime thisTime = LocalTime.now(); // 14:52:23.764490100
        LocalDateTime currentDateTime = LocalDateTime.now(); // 2021-05-04T14:52:23.764490100
        LocalDate someDay = LocalDate.of(2020, Month.JUNE, 12); // 2020-06-12
        LocalTime someTime = LocalTime.of(23, 53); // 23:53
        LocalDateTime otherDateTime = LocalDateTime.of(2021, Month.MARCH, 4, 10,51,44); // 2021-03-04T10:51:44
    }
}
```

Via:

1. [ ] https://chamalwr.medium.com/datetime-api-in-java-2aef5df1c39b #doing
2. https://www.baeldung.com/java-8-date-time-intro

### Data structures

https://www.youtube.com/watch?v=9rhT3P1MDHk&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY

### Files and APIs

- `FileWriter` - this class is useful to create a file by writing characters into it
- `FileReader` - this class is useful to read data in form of characters from file
- `Files.lines(Paths.get("file.txt")))` - processing the files as a stream. Since Java 8
- `Files.readString / Files.writeString` - reads the whole file and puts it into a string - since Java 11

## [[object-oriented-programming|OOP]] (Object-Oriented Programming)

Contain data in the form of fields (attributes) and code in the form of procedures (methods). OOP focuses on creating reusable code by grouping related data and behavior into objects, allowing for modularity(模块化), abstraction(抽象), inheritance(继承), and polymorphism(多态性).

These concepts help in organizing and structuring code in a way that mirrors real-world entities and their interactions.

https://jenkov.com/tutorials/java/classes.html

- Fields  字段
- Constructors  构造函数
- Methods  方法
- Nested Classes  嵌套类

### Packages

Namespace that mainly contains classes and interfaces.

### Classes and Objects

Classes are blueprints(蓝图) for creating objects, which are instances(实现) of those classes.

### Attributes and Methods

Attributes are variables that hold data about an object, defining its state or characteristics. Methods are functions that define the behavior of an object, allowing it to perform actions or operations. Together, attributes and methods encapsulate the data and behavior of an object within a class.

### Access Specifiers/Modifiers 访问说明符

- `private`
- `default` (no keyword)
- `protected`
- `public`

### Static Keyword 静态关键字

The `static` keyword in Java is used to create members (variables and methods) that belong to the class itself, rather than to any specific instance of the class. This means there’s only one copy of a static variable shared by all objects of that class, and you can access static members directly using the class name without needing to create an object. Static methods can only access static variables and call other static methods.

### Final Keyword Final 关键字

The `final` keyword in Java is a non-access modifier used to apply restrictions on a variable, method, or class. When applied to a variable, it makes the variable’s value constant after initialization. When applied to a method, it prevents the method from being overridden in a subclass. When applied to a class, it prevents the class from being subclassed (inherited).

### Nested Classes 嵌套类

Nested classes are classes defined inside another class. The class that contains the inner class is known as the outer class. Nested classes can access members of the outer class, even if they are declared private. They are a way to logically group classes that are only used in one place, increasing encapsulation and maintainability.

## More about OOP

### Object Lifecycle 对象生命周期

Refers to the series of stages an object goes through from its creation (allocation of memory) to its destruction (reclaiming of memory). These stages typically include object creation, initialization, usage, and eventual garbage collection when the object is no longer needed. Understanding this lifecycle is crucial for efficient memory management and preventing resource leaks.

The whole object life cycle that includes instantiation, initialization, usage, reference(引用), dereference(取消引用), and trash collection controls how objects behave in Java programmes.

https://www.tpointtech.com/object-life-cycle-in-java

### Method Chaining 方法链

Method chaining is a programming technique where multiple method calls are made sequentially on the same object, one after another, in a single statement. Each method in the chain returns an object, allowing the next method to be called on that returned object. This approach enhances code readability and conciseness by reducing the need for temporary variables and intermediate steps.

### Enums 枚举

Enums, short for enumerations, are a special data type in Java that represent a group of named constants. They allow you to define a type that can only take on a specific set of predefined values. This makes your code more readable and less prone to errors by restricting the possible values a variable can hold.

### Record 记录

A record is a special type of class in Java that is designed to hold immutable data. It automatically generates methods like `equals()`, `hashCode()`, and `toString()` based on the components declared in its header, reducing boilerplate code. Records are useful for creating data transfer objects (DTOs) or simple data aggregates where the primary purpose is to store and access data.

```java
public record Vehicle(String brand, String licensePlate) {}
```

两点需要注意：

1. 它的关键字没有 class
2. 它没有定义属性和方法，但上面签名足以生命一个对象；

#### Using a Java Record 使用 Java 记录

```java
public class RecordsExample {
  public static void main(String[] args) {
    Vehicle vehicle = new Vehicle("Mercedes", "UX 1238 A95");

    System.out.println( vehicle.brand() );
    System.out.println( vehicle.licensePlate() );

    System.out.println( vehicle.toString() );
  }
}
```

#### A Record is Final 记录已终结

https://jenkov.com/tutorials/java/record.html

### Initializer Block 初始化块

An initializer block in Java is a block of code, enclosed in curly braces {} , that is executed when an instance of a class is created. It’s used to initialize instance variables or perform setup tasks before the constructor is called.

#### Instance initializer blocks

run every time a new object is created

```java
public class InstanceBlockExample {

    {
        System.out.println("Instance initializer block 1");
    }
    
    static {
        System.out.println("Static initializer block 1");
    }
    
    public InstanceBlockExample() {
        System.out.println("Class constructor");
    }

    public static void main(String[] args) {
        InstanceBlockExample iib = new InstanceBlockExample();
        System.out.println("Main Method");
    }
}
```

#### Static initializer blocks

run only once when the class is first loaded.

### ​Inheritance 继承
- 继承 Composition, inheritance, and delegation (委托???)
    - 继承基类, 做出扩展; 子类 (完全) 兼容基类
    - 继承 (泛化)
      - 实现继承
        - 无需额外编码的能力
      - 可视继承
        - 子窗体（类）使用基窗体（类）的外观和实现代码的能力
    - 组合 (聚合)
      - 接口继承
        - 子类必须提供实现的能力
      - 纯虚类

### Abstraction 抽象

### Encapsulation 封装

  - 封装 Encapsulation
    - 明确接口

### Polymorphism 多态

基于对象所属类的不同, 外部对同一个方法的调用, 实际执行的逻辑不同; 多态依赖继承

### Interfaces 接口
#### 接口 vs 抽象类
1. 接口的方法默认是 public，所有方法在接口中不能有实现，抽象类可以有非抽象的方法
2. 接口中的实例变量默认是 final 类型的，而抽象类中则不一定
3. 非抽象类类可以实现多个接口，但最多只能实现一个抽象类
4. 一个类实现接口的话要实现接口的所有方法，而抽象类不一定
5. 接口不能用 new 实例化，但可以声明，但是必须引用一个实现该接口的对象
    1. java 8 在接口中用 default 修饰的方法可以有函数体

[接口和抽象类的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21077&query=&asc=true&order=&page=9)

#### 纯虚类 vs 接口
##### 同
- 都是抽象类，都不能实例化
- 接口实现类 & 抽象子类必须要实现已经声明的抽象方法

##### 异
- 纯虚类
- 接口

### Method Overloading and Overriding 方法重载和覆盖
#### 重写**范围**

- **只有实例方法可以被重写**，重写后的方法必须仍为实例方法
- **成员变量和静态方法 (static) 都不能被重写，只能被隐藏**
    - ??? 重写方法可以改变其它的方法修饰符，如 `final` , `synchronized` , `native` 。不管被重写方法中有无 final 修饰的参数，重写方法都可以增加、保留、去掉这个参数的 final 修饰符 (**参数修饰符不属于方法签名**)。
    - ??? 形式上可以写，但本质上不是重写，属于下面要讲的隐藏

#### **两同两小一大**原则

- 方法名相同，参数类型相同
- **返回类型** 子类 <= 父类方法
- **抛出异常** 子类 <= 父类方法
- **访问权限** 子类 >= 父类方法

### Static vs Dynamic Binding 静态与动态绑定

Static binding, also known as early binding, happens at compile time. The compiler knows exactly which method will be called based on the type of the variable. Dynamic binding, or late binding, occurs at runtime. The specific method to be called is determined based on the actual object type, not the variable type, allowing for more flexibility and polymorphism.

```java
public class Animal {

    static Logger logger = LoggerFactory.getLogger(Animal.class);

    public void makeNoise() {
        logger.info("generic animal noise");
    }

    public void makeNoise(Integer repetitions) {
        while(repetitions != 0) {
            logger.info("generic animal noise countdown " + repetitions);
            repetitions -= 1;
        }
    }
}

public class Dog extends Animal {

    static Logger logger = LoggerFactory.getLogger(Dog.class);
    
    @Override
    public void makeNoise() {
        logger.info("woof woof!");
    }

}


Animal animal = new Animal();

// calling methods of animal object
animal.makeNoise();
animal.makeNoise(3);

// assigning a dog object to reference of type Animal
Animal dogAnimal = new Dog();

dogAnimal.makeNoise();

The output of the above code will be:
```

https://www.baeldung.com/java-static-dynamic-binding

## Pass by Value / Pass by Reference

Pass by value and pass by reference are two different ways of passing arguments to a function or method. In pass by value, a copy of the variable’s value is passed to the function, so any changes made to the parameter inside the function do not affect the original variable. In pass by reference, a direct reference to the variable is passed, meaning that changes made to the parameter inside the function will directly affect the original variable.

1. For Primitive types, parameters are pass-by-value
    对于原始类型，参数是按值传递的
2. For Object types, the object reference is pass-by-reference
    对于对象类型，对象引用是按引用传递的

https://www.baeldung.com/java-pass-by-value-or-pass-by-reference

## Exception Handling

Java Exception Handling is a mechanism to handle runtime errors such as `ClassNotFoundException`, `IOException`, `SQLException`, `RemoteException`, etc.

There are three types of exceptions:

1. Checked Exception - exceptions checked at compile time.
   **Example** - IOException
2. Unchecked Exception - exceptions checked at run time.
   **Example** - NullPointerException
3. Error - It is irrecoverable.
   **Example** - OutOfMemoryError

## Lambda Expressions Lambda 表达式
