---
aliases: js, javascript
created: 2024-07-17T00:00:00
description: a high-level, often just-in-time compiled language that conforms to the ECMAScript standard
tags: web
type: lang/programming
wikipedia: https://en.wikipedia.org/wiki/JavaScript
modified: 2025-03-22T16:40:30
---

## Why
## How

### Date Handler

#### [Calculate the date yesterday in JavaScript - Stack Overflow](https://stackoverflow.com/questions/5511323/calculate-the-date-yesterday-in-javascript)

```js
var date = new Date();
date ; //# => Fri Apr 01 2011 11:14:50 GMT+0200 (CEST)
date.setDate(date.getDate() - 1);
date ; //# => Thu Mar 31 2011 11:14:50 GMT+0200 (CEST)
```

#### [Get Yesterday Date in JavaScript | HereWeCode](https://herewecode.io/blog/get-yesterday-date-javascript/#:~:text=The%20best%20way%20to%20get,setDate%20to%20update%20the%20date.)

```js
// Create a date
const todayDate = new Date()
// Before subtracting 1 day
console.log(todayDate.toString())
// Output: "Tue Nov 15 2022 13:37:12 GMT+0100 (Central European Standard Time)"
// Subtract one day to the current date
todayDate.setDate(todayDate.getDate() - 1)
// After removing 1 day
console.log(todayDate.toString())
// Output: "Mon Nov 14 2022 13:37:12 GMT+0100 (Central European Standard Time)"
```

- [ ] [html - How to mark: width of :before pseudo element relative to containing element - Stack Overflow](https://stackoverflow.com/questions/39995303/how-to-mark: -width-of-before-pseudo-element-relative-to-containing-element)
- `relative`?
- [ ] [HTML Entities (w3schools.com)](https://www.w3schools.com/html/html_entities.asp)
- [ ] [css - width and height doesn't seem to work on :before pseudo-element - Stack Overflow](https://stackoverflow.com/questions/20858587/width-and-height-doesnt-seem-to-work-on-before-pseudo-element)

#### [Compare two dates with JavaScript - Stack Overflow](https://stackoverflow.com/questions/492994/compare-two-dates-with-javascript)

```js
var d1 = new Date();
var d2 = new Date(d1);
console.log(d1 == d2);   // prints false (wrong!)
console.log(d1 === d2);  // prints false (wrong!)
console.log(d1 != d2);   // prints true  (wrong!)
console.log(d1 !== d2);  // prints true  (wrong!)
console.log(d1.getTime() === d2.getTime()); // prints true (correct)
```

#### [Checking if two Dates have the same date info - Stack Overflow](https://stackoverflow.com/questions/4428327/checking-if-two-dates-have-the-same-date-info)

```js
Date.prototype.isSameDateAs = function(pDate) {
return (
this.getFullYear() === pDate.getFullYear() &&
this.getMonth() === pDate.getMonth() &&
this.getDate() === pDate.getDate()
);
}
```

#### [check if two dates are the same day in JavaScript (flaviocopes.com)](https://flaviocopes.com/how-to-check-dates-same-day-javascript/)

```js
const datesAreOnSameDay = (first, second) =>
  first.getFullYear() === second.getFullYear() &&
  first.getMonth() === second.getMonth() &&
  first.getDate() === second.getDate();
```

#### [Format a JavaScript Date to YYYY MM DD - Mastering JS](https://masteringjs.io/tutorials/fundamentals/date-tostring-format-yyyy-mm-dd)

```js
const date = new Date();
date.toLocaleDateString('en-GB').split('/').reverse().join(''); // '20211124'
```

#### [Date.prototype.toLocaleDateString() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)

```
const date = new Date();
console.log(date);
```

#### [How to Get the Current Date in JavaScript - Scaler Topics](https://www.scaler.com/topics/get-current-date-in-javascript/)

```
let yourDate = new Date()
yourDate.toISOString().split('T')[0]
```

— [Format JavaScript date as yyyy-mm-dd - Stack Overflow](https://stackoverflow.com/questions/23593052/format-javascript-date-as-yyyy-mm-dd)

## What

## References

- [Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API)
- [JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
- [2020年度 JS13K Games 竞赛](https://github.blog/2020-10-11-top-ten-games-from-the-js13k-2020-competition/)
- [Asynchronous JavaScript (2020 version) - YouTube](https://www.youtube.com/playlist?list=PL4cUxeGkcC9jx2TTZk3IGWKSbtugYdrlu)
- Send HTTP
    - [HTTP GET request in JavaScript? - Stack Overflow](https://stackoverflow.com/questions/247483/http-get-request-in-javascript)
    - [XMLHttpRequest - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
    - API endpoint
