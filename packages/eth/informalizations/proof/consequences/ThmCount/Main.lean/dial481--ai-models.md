---
{
  "module": "proof/consequences/ThmCount/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/ThmCount/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem C from Theorem D(b) at k = 3

This is not the route of the proof sketch of Appendix C; see the head of
proof/consequences/ThmCount/Defs.lean.
* `wrapper_counts`: let M have the body of Theorem D(b) with the constant C, let `pre` map the plain
  code of a 3-CNF φ to the code of (3, φ with four forced variables more), and let N wrap M with
  `pre` and `dropFour`, with the number q. Then N computes the number of satisfying assignments of
  every 3-CNF on n variables within q·(⌊2^{C·9·(n+4)·log log(n+4)/√(log(n+4))}⌋ + a·(n+2)^d + 1)^q
  steps, where a·(n+2)^d bounds the length of the plain code.
* `stFromVariablesB`, `stCanBeWrappedAndEveryWrapperCounts`, `stTheorem`: with the comparison of the
  rates `stRates`.
* `stRemarkTime_of`: the time in the closing remark of Appendix C, as a sentence, from Theorem D(b),
  with the second comparison of rates `remark_rate`. 

### `wrapper_counts`

 Every machine N that wraps a machine M with the body of Theorem D(b), with a front end that adds
four forced variables and with `dropFour` as the last step, computes the number of satisfying
assignments of every 3-CNF on n variables within q·(time of M on n + 4 variables + a·(n+2)^d + 1)^q
steps, if a·(n+2)^d bounds the length of the plain code. 

### `time_cast`

 The time of `wrapper_counts` is at most the same expression with 2^{C·expN 3 (n+4)} in the place
of its floor, as a real number. 

### `stFromVariablesB`

 **For every machine M with the body of Theorem D(b)**, every front end that adds four forced
variables and every machine N that wraps M with it and with `dropFour`: N computes the number of
satisfying assignments of every 3-CNF, on n ≥ 2 variables in time 2^{C'·n/(log n)^{1/20}}. This is
the statement `ThmCount.StFromVariablesB`. 

### `stCanBeWrappedAndEveryWrapperCounts`

 Existence and the statement on every wrapper in one: for every machine M with finite alphabets
and the body of Theorem D(b) there are a polynomial-time front end, a machine N with finite
alphabets and q such that N wraps M with it and with `dropFour`; and every such N counts, as in
`stFromVariablesB`. This is the statement `ThmCount.StCanBeWrappedAndEveryWrapperCounts`. 

### `stTheorem`

 Theorem C from Theorem D(b): if one algorithm computes, for all k ≥ 1 and n ≥ 4, the number of
satisfying assignments of a k-CNF on n variables in time 2^{C·k²·n·log log n/√(log n)}, then one
algorithm computes the number of satisfying assignments of a 3-CNF on n ≥ 2 variables in time
2^{O(n/(log n)^{1/20})}. This is the statement `ThmCount.StTheorem`. 

### `stRemarkTime_of`

 The time of the closing remark of Appendix C, as a sentence, from Theorem D(b): one algorithm
computes the number of satisfying assignments of a 3-CNF on n ≥ 4 variables in time 2^{O(n·(log log
n)^{2/3}/(log n)^{1/6})}. The machine is a wrapper as in `stCanBeWrappedAndEveryWrapperCounts`. 
