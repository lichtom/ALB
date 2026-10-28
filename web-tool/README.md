# ALB.js — 纯 JavaScript ALB 解释器

在浏览器或 Node.js 中运行 ALB 代码，无需编译，零依赖。语义与 C++ 参考实现保持一致。

## 安装

**浏览器 (ES Module):**
```html
<script type="module">
import ALB from './alb.js';
ALB.run('(print "Hello ALB!")');
</script>
```

**Node.js (CommonJS):**
```js
const ALB = require('./alb.js');
ALB.run('(print "Hello ALB!")');
```

**浏览器全局:**
```html
<script src="alb.js"></script>
<script>
  ALB.run('(print "Hello ALB!")');
</script>
```

## API

### 执行代码

```js
ALB.eval('(+ 1 2 3)')          // → 6
ALB.run('(print "hi") (+ 1 2)') // → { result: 3, output: ["hi"] }
```

### 注入数据与函数

```js
ALB.setVar('name', 'Tom')       // 变量（ALB 可修改）
ALB.setConst('PI', 3.14)        // 常量（ALB 不可修改）
ALB.setFunc('shout', s => s.toUpperCase() + '!')  // 注册 JS 函数
```

### 构造 ALB 数据结构

```js
ALB.list(1, 2, 3)               // ALB list
ALB.map({ a: 1, b: 2 })        // ALB map
ALB.vector(10, 20, 30)          // ALB vector
ALB.nil()                       // ALB nil
```

### 读取与检查

```js
ALB.getVar('x')                 // 读取变量（返回 JS 值）
ALB.has('x')                    // 变量是否存在
ALB.deleteVar('x')              // 删除变量
```

### 模块系统

```js
ALB.registerModule('math', '(let double (func (list n) (* n 2)))')
ALB.loadModule('math')
ALB.eval('(double 21)')         // → 42
```

## 支持的 ALB 特性

| 类别 | 特性 |
|------|------|
| **特殊形式** | `let` `define` `def` `let*` `letrec` `if` `when` `cond` `while` `for-i` `do` `func` `match` `try` `quote` `defmacro` `struct` `export` |
| **算术** | `+` `-` `*` `/` `%` `^` `abs` `floor` `ceil` `round` `sqrt` `min` `max` `clamp` |
| **三角** | `sin` `cos` `tan` `asin` `acos` `atan` `atan2` |
| **比较/逻辑** | `==` `!=` `<` `>` `<=` `>=` `and` `or` `not` |
| **位运算** | `bit-and` `bit-or` `bit-xor` `bit-not` `bit-lshift` `bit-rshift` |
| **字符串** | `str` `len` `substr` `str-split` `str-join` `str-lower` `str-upper` `str-trim` `str-find` `str-replace` `str-starts?` `str-ends?` `str-reverse` `str-repeat` |
| **列表高阶** | `map` `filter` `fold` `sort` `flatten` `reverse` `take` `drop` `zip` `unzip` `uniq` `each` `for` `apply` `partial` `compose` `pipe` |
| **列表基础** | `car` `cdr` `cons` `nth` `push` `range` |
| **Map** | `dict` `map-get` `map-set` `map-del` `map-has?` `map-keys` `map-values` `map-merge` |
| **Vector** | `vector` `vector-ref` `vector-push!` `vector-pop!` `vector-set!` `vector-size` `vector->list` `list->vector` |
| **Struct** | `struct` + 自动构造函数、谓词、字段访问器 |
| **正则** | `re-test?` `re-find` `re-match` `re-replace` `re-split` |
| **其他** | `type` `print` `prints` `json-parse` `json-serialize` `time-now` `time-now-ms` `assert` `throw` `break` `random` `random-int` |
| **模式匹配** | 数字 / 字符串 / 列表（`$` rest）/ 结构体 / `_` 通配 |
| **宏** | `defmacro` + `` ` `` quasiquote + `,` unquote + `,@` splicing |
| **字符串插值** | `` `Hello ${name}` `` |
| **TCO** | 尾递归优化（自递归 + if 分支递归） |

## 多实例

```js
const { createALB } = await import('./alb.js');
const sandbox = createALB();
sandbox.setVar('x', 100);
sandbox.eval('x');  // → 100
```

## License

MIT
