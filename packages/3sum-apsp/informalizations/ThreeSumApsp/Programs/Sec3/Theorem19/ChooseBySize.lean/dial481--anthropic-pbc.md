---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem19/ChooseBySize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/ChooseBySize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem19/ChooseBySize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Two algorithms for Exact Triangle and a threshold on the number of vertices

For every threshold n₀ there is a constant C₀ such that, if Exact Triangle is solved in time T₁ and
in time T₂, then it is solved in time T₁ + C₀ for n < n₀ and T₂ + C₀ for n ≥ n₀.  This is
`Closure.ChooseBySize`, with "Exact Triangle is solved in time T" read as `SolvedIn etTask T`
(`closure_chooseBySize`).  It is used in the proof of Theorem 19, where the bounds hold
for large n only.

Two solvers are put into one program, the second behind the first (`solves_behind`), and one more
procedure looks at the number of vertices and calls the first solver below a fixed threshold n₀ and
the second one from the threshold on (`bySize_spec`).  The need stays polynomial
(`polyNeed_bySize`).


### `bySizeBody`

 choose(n, U, ab, bc, ac, fr): calls procedure p₁ if n < n₀, and procedure p₂ if not, on the same
arguments: the number n of vertices in a part, the bound U on the weights, the addresses ab, bc, ac
of the three matrices of weights, and the free pointer fr. 

### `bySizeTime`

 The number of steps of choose. 

### `bySizeNeed`

 What choose needs: a word for the threshold, one more level of calls, and what the two solvers
need. 

### `solves_behind`

 A solver stays a solver, with its number shifted, when its program is placed behind another
program. 

### `bySize_spec`

 **choose** solves Exact Triangle. 

### `polyNeed_bySize`

 The need of choose is polynomially bounded if the needs of the two solvers are. 

### `closure_chooseBySize`

 **Two algorithms, chosen by the size of the instance.** 
