---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a): from 3SUM to Convolution-3SUM, and on to Exact Triangle

Theorem 21(a) reduces 3SUM to Exact Triangle.  Here it is composed of two
reductions.

* From 3SUM to Convolution-3SUM, cited from [CH20, Theorem 5.1].
  `theorem_21a_threeSum_to_convolution` states it for the explicit function `ChanHe.instances`.  It
  collects the correctness of the reduction (`ChanHe.threeSum_iff_exists_convolution3SUM`), the
  number of instances (`ChanHe.length_instances_pow_le`), the size of their entries
  (`ChanHe.abs_instances_pow_le`), the count for the searches (`ChanHe.scanPairs_pow_le`), and the
  asymptotic form of the three bounds.
* From Convolution-3SUM to Exact Triangle, cited from [VW13, Theorem 4.3]:
  `theorem_21a_convolution_to_exact`.  `theorem_21a_threeSum_to_exact` applies it to each array that
  the first reduction makes.

Nothing is stated here about running times, and the forms `n^{1/2+o(1)}` of Theorem 21(a) are not
derived; see the two docstrings.

Of the facts about `ChanHe.instances`, the programs for the reduction use only the correctness
(`ChanHe.instances_correct`).  Their running time is counted on the programs themselves, with the
bound on the number of nodes of a tree (`ChanHe.length_nodes_le`) and the orders of growth of the
parameters; the count `ChanHe.scanPairs` and the bounds `numBound` and `workBound` serve the
compared statement only.


 ## From 3SUM to Convolution-3SUM 

### `theorem_21a_threeSum_to_convolution`

 The reduction from 3SUM to Convolution-3SUM in the form needed for **Theorem 21(a)**.  The list
of instances may depend on the input, so a statement that such a list exists would be true for
trivial reasons.  The statement is therefore about the explicitly defined function
`ChanHe.instances`, and it is to be read together with the definitions of the namespace `ChanHe`.

What is stated: the input (`n ≥ 2` integers of absolute value at most `n^κ`, for a natural number
`κ`, the ν of Theorem 21, to which a real exponent can be rounded up; 3SUM asks for three numbers at
different positions), the number of instances, `(log n)^{O(1)}` (at most `ChanHe.numBound κ n`),
their length, `Õ(n)` (`ChanHe.lenOf κ n`, the common length), the absolute value of their numbers,
`n^{O(1)}` (at most `120 n^κ + 40`), and the one-array problem.

What is not stated: that the reduction is deterministic and takes `Õ(n^{3/2})` time.  This is about
a machine, and nothing here is about a machine.  In its place stands `ChanHe.scanPairs`, the number
of pairs (candidate prime, element) that the searches for the moduli go through.  It is a count that
we define, not a running time that we derive. It is at most `ChanHe.workBound κ n`, which is
`n^{3/2}` times a polylogarithm.

NOTE.
* `κ` is a natural number.
* Theorem 5.1 of [CH20] is a statement about running times, for 3SUM on three sets and
  Convolution-3SUM on three arrays.  The reduction stated here, with its count of instances, their
  length and the Õ(n^{3/2}), follows the proof of that theorem, and passes to `n` numbers and to one
  array by elementary devices; see `docs/REMARKS.md`, "Section 3: cited results". 

 ## On to Exact Triangle 

### `TriangleTemplate.weightsBoundedBy_instantiate`

 The weights that a template produces are bounded by the filler, if the entries of the input
are. 

### `theorem_21a_threeSum_to_exact`

 The two reductions of **Theorem 21(a)** composed.  For `n ≥ 2` put
`N = ChanHe.lenOf κ n`. There are `t ≤ √N + 1` and at most `2t` templates such that, for every input
`x` of `n` integers of absolute value at most `n^κ`: the list `ChanHe.instances n (n^κ) x` has at
most `ChanHe.numBound κ n` arrays; each template turns each array into an instance of Exact Triangle
on `t` vertices per part, with the filler weight `240 n^κ + 81` and all weights of absolute value at
most that; and three entries of `x` at different positions sum to 0 iff one of these instances has a
zero triangle.

So there are at most `2t · ChanHe.numBound κ n` triangle instances.  As above, `κ` is a natural
number; it is the paper's ν.

What is not stated.  The words "deterministically, in n^{3/2+o(1)} time" are about a machine, and
nothing here is about a machine. The forms `n^{1/2+o(1)}` of Theorem 21(a) for the number of
instances and for `t` are not part of this statement: they follow from the bounds on `numBound` and
`lenOf` in `theorem_21a_threeSum_to_convolution` by the arithmetic of `theorem_21a_compose`, but
this last step is not carried out here.  No lower bound on `t` is stated, so the weights are not
bounded by a power of the number of vertices, which is the form in which Theorem 19 takes them. 
