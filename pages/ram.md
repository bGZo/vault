---
draft: true
aliases:
  - 内部存储器
  - 内存
  - 随机存取储存器
  - 随机访问存储器
  - RAM
  - random access memory
created: 2025-03-15T09:36:24
modified: 2025-08-30T16:39:16
title: RAM
wikipedia: https://en.wikipedia.org/wiki/Random-access_memory
---
# RAM

The two main types of volatile(易失性) random-access semiconductor memory

- static random-access memory (**SRAM**)
	- Synchronous dynamic random-access memory (**SDRAM**) later debuted with the Samsung KM48SL2000 chip in 1992. [^SDRAM]
- dynamic random-access memory (**DRAM**).
	- The first commercial DDR SDRAM (**double data rate SDRAM**) memory chip was Samsung's 64 Mbit DDR SDRAM chip, released in June 1998.[^DDR]

> [!note]
      > Non-volatile memories used for ROM

## Reference

> 运行内存与运存为错误用辞，仅在特指手机内存的非专业交流中流行
> — [随机存取存储器 - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/%E9%9A%8F%E6%9C%BA%E5%AD%98%E5%8F%96%E5%AD%98%E5%82%A8%E5%99%A8#cite_note-1)

- 时钟频率单位：(MT/s) mega transfers per second

[^SDRAM]: 自動與中央處理單元 (CPU) 的時序進行同步。記憶體控制器就跟時鐘一樣，會知道要求的資料何時就緒的確切週期，因此表示 CPU 不必等候記憶體存取。SDRAM 每個時脈週期僅可讀取/寫入一次。via: [RAM 世代：DDR2、DDR3、DDR4 與 DDR5 之間的比較 | Crucial TW](https://www.crucial.tw/articles/about-memory/difference-among-ddr2-ddr3-ddr4-and-ddr5-memory)
[^DDR]: DDR 記憶體在時脈信號的強拍與弱拍（因此每個週期兩次）皆會向處理器傳輸資料。使用這兩拍傳輸資料即可讓 DDR 記憶體遠快於 SDR 記憶體（僅使用時脈訊號的一緣傳輸資料）。DDR 從記憶體陣列將二位元資料傳輸到內部輸入/輸出緩衝區的程序稱為 ==2 位元 (进制)== 預先截取。DDR 傳輸速率通常介於 266MT/s 和 400MT/s 之間。請注意，雙倍資料速率不同於雙通道記憶體。
