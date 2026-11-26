---
{
  "module": "proof/rates/PaddedDescent/F/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top of the function A: the walk of the sparsification tree, and the correctness of A

`walk : StWalk`: if the pad is long enough, `walkF k` says whether some leaf of the sparsification
tree at width k passes the test.
`treeK`: what is needed to know about the sparsification tree of a formula with clauses of 1 to k
literals.
`walk_sat`: for every width k ≥ 1, every n with sOf n ≥ s0K k and every pad of length at least
2^(8·(n / 2^(sOf n) + 1)), the walk whose test is «`countM k` is positive» says whether a
formula on n variables with clauses of 1 to k literals, at most inLen k n of them, is satisfiable.
`correct : StCountM → StLeaf → StSched → StA → StAW → StCorrect (C0K 3) (s0K 3)`: the function `A`,
given the code of an instance φ of 3-SAT on n variables with
sOf n ≥ s0K 3 and the pad of length 2^(C0K 3·(n / 2^(sOf n) + 1)), returns the bit «φ is
satisfiable». The five hypotheses are the statements
of other files: the count for one sparse formula, the form of a leaf, the schedule, and the two
parts of the arithmetic («the pad is long enough»). 

### `foldl_capped_eq_iterate`

 A fold that applies f and then a cut-off cp in every round equals the iterate of f, if the
cut-off leaves all iterates alone. 

### `walk`

 If the pad has at least 2·(number of leaves) − 1 units and every state of the walk fits under
it, `walkF` says whether some leaf passes the test. 

 ### The length of the word of a state of the walk 

### `len_list_le`

 A bound on the length of the word of a list of at most k members, each with a word of length at
most s. 

### `len_lit_le`

 A bound on the length of the word of a literal with variable below n. 

### `len_fml_le`

 A bound on the length of the word of a formula of at most m clauses of at most k literals with
variables below n. 

 ### The tree of an instance 

### `prog`

 The sparsification lemma of the imported modules `SparsifyWidthK.Step` to
`SparsifyWidthK.ProgMain`, for the program `stepK`. 

### `treeK`

 The sparsification tree of a formula ψ of at most m clauses of 1 to k literals on variables
below n: every node that `leaves` returns at depth bsum τ k · n is a leaf (`stepK` gives `none` on
it); their number; the word of
every state of the walk is short; and if the test is right on every formula of at most (leafC τ k + 2)·n
clauses of 1 to k literals in which every variable occurs at most
leafC τ k + 2 times, then some leaf passes the test iff ψ is satisfiable. 

### `one_le_tauOf`

 The threshold is positive. 

### `length_markPar`

 The four parameters of the evaluations, as numbers. 

### `walk_sat`

 The walk whose test is «the count is positive» decides satisfiability: width k ≥ 1, n variables
with sOf n ≥ s0K k, at most inLen k n clauses of 1 to k literals, and a pad of
length at least 2^(8·(n / 2^(sOf n) + 1)). 

### `inLen_three`

 The bound for the length of a code at width 3. 

### `correct`

 The function `A` is correct on every instance with sOf n ≥ s0K 3, given the pad of length 2^(C0K
3·(n / 2^(sOf n) + 1)). 
