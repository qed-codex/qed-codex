---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/QuerySum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/QuerySum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/QuerySum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A query, once the digits of its output string are known

Proof of Theorem 30, "Query"; these are steps (2) and (3) of the query in Section 4.3. The routine
adds up the sum of Lemma 28: for each leaf of order below t contributing to the output string the
product of its two numbers in the encodings of the tile (queryLowRound), and for each box of the
output string its value (queryBoxRound): "we look up its value in the trie of the tile". The root of
this trie is an argument of the routine.

Leaves and boxes are enumerated through the strings of m digits with a bounded number of nines. For
the boxes the proof of Theorem 30 says "for every V ⊆ Q with |V| = m - t and every box of 𝓑_V". The
routine has one loop (queryBoxes), over the strings with exactly m - t nines: such a string gives V
(the places of its nines) and the box of 𝓑_V (its other digits) at once. This is the other way in
which Section 4.2 describes the boxes of w, "in terms of the leaves of order exactly t contributing
to w. For such a leaf, consider the lowest level of Q at which it chooses a term other than P₀, and
replace its P₀ by a star at every lower level of Q (or at every level of Q, if t = 0). The result is
a box of w, and each box of w arises exactly once in this way" (for cubes:
`existsUnique_starBelow_eq`). The members of the list of the routine are exactly the strings of the
cubes so obtained (`mem_boxesOf_iff`), and a sum over the list is the sum over the sets 𝓑_V
(`sum_boxesOf`). The sets V come interleaved, in the lexicographic order of the strings.

Both loops have one invariant, Query.Inv: the sum of the first terms stands in a local, and the
current string of the enumeration in the scratch area ss. Query.low_term and Query.box_term say
which term a round adds; Query.lowRound and Query.boxRound are the two rounds, Query.loop is either
loop, and queryCore_spec puts the two loops together.


 ## The program 

### `EncA`

 The local variables of queryCore: the arguments aA, aB, tr, root, wd, ss, box, L, m, t; the sum
so far, whether there is a further string, the code of the leaf (the result of scatter, which is not
used, goes there too), the value of the box, and m - t. 

### `queryLowRound`

 One round of the first loop: a leaf of order below t. 

### `queryBoxRound`

 One round of the second loop: a box, looked up in the trie of the tile. 

### `queryLow`

 The leaves of order below t: the strings with more than m - t nines. 

### `queryBoxes`

 The boxes: the strings with exactly m - t nines. 

### `queryCoreBody`

 queryCore(aA, aB, tr, root, wd, ss, box, L, m, t) returns the sum of Lemma 28. The sum starts
at 0, as all locals that are not arguments; the result of a procedure is its local 0, so the last
statement puts the sum there. 

 ## The pure side: the terms of the sum 

### `lowCount`

 The number of leaves of order below t. 

### `boxCount`

 The number of boxes. 

### `length_digits`

 The output string has one digit for each level. 

### `count_digits`

 The digit 9, which stands at the levels of the subset, occurs m times. 

### `leafAt`

 The string that round i of the first loop writes at box: a leaf of order below t. 

### `boxAt`

 The string that round i of the second loop writes at box: a box of the output string. 

### `low_term`

 Round i of the first loop treats a leaf τ and adds the product of its two numbers. 

### `box_term`

 Round i of the second loop treats a box and adds its value, looked up in the trie of the
tile. 

 ## The memory and the invariant 

### `same_of_ss`

 A write to the string at ss stays within the two scratch strings. 

### `same_of_box`

 A write to the string at box stays within the two scratch strings. 

### `seg_of_same`

 A segment that meets neither scratch string is kept. 

### `Callees`

 The specifications of the routines that queryCore calls. 

### `Inv`

 The state before round i of the loop over the strings with lo to hi nines, when base terms have
been added before the loop: the sum of the first base + i terms stands in the local Sum, the local
More says whether there is a string number i, and this string stands at ss. 

### `segDigits`

 The digits of the output string are kept. 

 ## The two calls that both rounds make 

### `scatter_meets`

 scatter(wd, ss, box, L, star) writes the leaf or the box of string number i at box; the string
at ss is kept. 

### `next_meets`

 nineNext(ss, m, lo, hi) goes on to string number i + 1 and says whether there is one. 

 ## The two rounds 

### `lowRound`

 One round of the first loop adds the term of the leaf number i. 

### `boxRound`

 One round of the second loop adds the value of the box number i. 

 ## The two loops 

### `loop`

 Either loop: as long as there is a further string, one round. 

### `Mid`

 The state between the loops: the sum of the first n terms stands in the local Sum. 

### `Inv.mid`

 After a loop, only the sum and the memory matter. 

### `low_spec`

 The leaves of order below t. 

### `boxes_spec`

 The boxes. 

### `tail_spec`

 The boxes, and the result. 

### `queryCore_spec`

 **queryCore** meets its specification. 
