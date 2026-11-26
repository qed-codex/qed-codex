---
{
  "module": "proof/rates/CountedToPadded/Compare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Compare.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Compare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The word of a value against a padding string

A fragment sees the tree of a value and not its type. `vSplit` takes a tree apart (empty, a bit, or
a pair); its fragment, with the head statement `bitHead`, is the one piece of code for the Turing
machine that this file adds. `visit` works on a list of trees still to be visited and a count: it
takes the first tree off the list, adds the number of symbols that are its own (2 for the empty tree
and for a pair, 1 for
a bit) to the count, and puts the two parts of a pair back on the list. Every round visits one node,
and a word has at least as many symbols as its tree has nodes. So after as many rounds as the
padding string has units either the list is empty, and the count is the length of the word, or the
word is longer than the padding
string. 

### `encV`

 The coding of a tree is the tree itself. 

 ### Taking a tree apart 

### `vSplit`

 Takes a tree apart: empty, a bit, or the two parts of a pair. 

### `bitHead`

 Look at the symbol on top of the main stack: an opening bracket gives the label false, anything
else the label true. At the start of the word of a tree the symbol is an opening bracket or a bit,
so there the label true means a bit. The stack is left as it was. 

### `bitHead_bit`

 On a bit the head statement gives the label true and leaves the stacks as they were. 

### `bitHead_L`

 On an opening bracket the head statement gives the label false and leaves the stacks as they
were. 

### `length_code_tag`

 A tag in front adds three symbols to the word. 

### `vSplit_poly`

 Taking a tree apart is polynomial-time: look at the first symbol, for a bracket at the second,
and put the one or two tags in front. 

### `vSplit'`

 The same in the form that the tactic `fun_prop` uses; in this file only. 

 ### One round 

### `visit`

 Visit the first tree of the list. 

### `visit_poly`

 One round is polynomial-time. 

### `total`

 The symbols of the trees still to be visited. 

### `nodes`

 The number of nodes of a tree. 

### `work`

 The nodes still to be visited. 

### `nodes_pos`

 A tree has at least one node. 

### `nodes_le`

 A tree has at most as many nodes as its word has symbols. 

### `visit_total`

 A round keeps the sum of the count and the symbols still to be visited. 

### `visit_work`

 A round on a list that is not empty visits exactly one node. 

### `fold_total`

 So do any number of rounds keep that sum. 

### `fold_done`

 After at least as many rounds as there are nodes the list is empty. 

 ### The comparison 

### `cmp`

 As many rounds as the padding string has units; then: is the list empty, and the count within
the padding string? 

### `cmp_eq`

 The comparison decides whether the word is at most as long as the padding string. 

### `sum_len_le`

 The word of the list of trees has at most three times their symbols, and two more. 

### `cmp_poly`

 The comparison is polynomial-time: the states of the fold are at most three times as long as the
input, and six more. 

### `wordCompared`

 Whether the word of a value has at most as many symbols as a padding string has units is decided
in polynomial time, for every type and every coding. 
