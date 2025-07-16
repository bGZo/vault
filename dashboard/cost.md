---
aliases:
  - 开支
  - 续费服务
  - Renew Service
created: 2023-05-29T20:55:33
modified: 2025-07-15T22:27:46
title: 续费服务
---

# 续费服务

```dataview
table sum(rows.cost) as "总成本"
FROM ""
WHERE cost >=0
GROUP BY undefined
```

```dataview
table 
	title as 项目,
	cost as "花费/年/RMB",
	remark as 备注
from ""
where cost >= 0
sort cost desc
```
