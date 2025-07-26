---
aliases:
  - py
  - Python
created: 2024-12-08T21:26:22
modified: 2025-07-25T23:21:25
title: Python
type: lang/programming
---

# Python

## Why

- 语法简单，符合自然语言

## How

### Date

```python
# https://stackoverflow.com/questions/441147/how-to-subtract-a-day-from-a-date
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date

from datetime import datetime

ts = int('1284101485')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case

print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
```

```python
# http://strftime.org
# https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

from datetime import datetime
datetime.today().strftime('%Y-%m-%d')
'2021-01-26'
```

## What

### `tuple(xxx,xxx,xxx)` Vs `list[xxx,xxx,xxx]`

前者无法修改

## References
