---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/ChanHe/FromNumbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/FromNumbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/FromNumbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a), the reduction of Chan and He: from n numbers to one-array Convolution-3SUM

We read the 3SUM of the paper as: three of `n` numbers, at different positions, sum to 0.  Its
Convolution-3SUM has one array (Section 1.2).  The proof of [CH20, Theorem 5.1] is
about three sets and three arrays.  This file passes from the one to the other by elementary
devices, which are not from that proof, and shows that the whole reduction, `instances`, is correct.

* Three distinct values.  The label of a number `x` in `[-U, U]` is `x + U`.  The labels of two
  distinct numbers differ in a binary digit, so splitting the set of values by two binary digits of
  the labels, in all possible ways, separates any three distinct values into three sets
  (`distinct_iff_split`).
* A repeated value.  A solution that repeats a value is `a, a, -2a` or `0, 0, 0`
  (`threeSum_iff_distinct_or_degenerate`), and two further three-set inputs detect these
  (`degenerate_iff`).
* Three arrays in one.  `oneArray` interleaves the three arrays and adds multiples of a large number
  `G`, which cancel only in equations `X i + Y j = Z (i + j)` (`oneArray_correct`).
* The whole reduction.  `IsInput` lists the three-set inputs.  There is a solution iff one of them
  has one (`threeSum_iff_exists_input`), each of them meets the hypotheses of `reduction_correct`
  (`IsInput.admissible`), and the nodes of the reduction are the nodes of their trees
  (`mem_allNodes_iff`).  With `reduction_correct` this gives `instances_correct`.  The number of
  instances, their entries and the count for the searches are bounded in `length_instances_le`,
  `abs_instances_le` and `scanPairs_le`.


 ## One set instead of three: three distinct values 

### `lab_cast`

 On `[-U, U]` the label of `x` is `x + U`. 

### `lab_lt`

 The label of an element of `[-U, U]` has at most `Lam U` binary digits. 

### `exists_testBit_lab_ne`

 The labels of two different elements of `[-U, U]` differ in one of their `Lam U` lowest binary
digits. 

### `exists_split_of_testBit`

 Let `x + y + z = 0` in `S`.  If the label of `x` differs from those of `y` and `z` in digit `β`,
and `y ≠ z`, then one of the three-set inputs obtained by splitting `S` has a solution. 

### `distinct_iff_split`

 A set has three distinct elements with sum 0 iff one of the `2 (Lam U)²` three-set inputs,
obtained by splitting it by two binary digits, has a solution.  This step is not from [CH20]. 

 ## Positions instead of values: solutions that repeat a value 

### `Degenerate`

 There is a solution that repeats a value: `a, a, -2a` with `a ≠ 0`, or `0, 0, 0`, at different
positions. 

### `degenerate_of_eq`

 A solution at three different positions, two of which hold the same value, repeats a value. 

### `threeSum_iff_distinct_or_degenerate`

 Three different positions with sum 0: either the three values are distinct, or the solution
repeats a value. 

### `degenerate_iff`

 There is a solution that repeats a value iff one of two three-set inputs has a solution.  The
first input leaves the search for `-2a` to the reduction.  The second already contains the answer
for `0, 0, 0`; see `zeroSet`. 

 ## Three arrays in one 

### `oneArray_val`

 The definition of `oneArray` with `G` written out. 

### `oneArray_sol`

 A solution `(i, j)` of the three arrays gives the solution `(4i + 1, 4j + 2)` of the one
array. 

### `convSol_of_oneArray`

 A solution of the one array is a solution of the three arrays: the multiples of `G = 3W + 1`
cancel only if the two indices have the remainders 1 and 2 modulo 4. 

### `oneArray_correct`

 **Three arrays to one**, of four times the length.  Here `W` bounds the entries of the three
arrays below `N`.  This step is not from [CH20]. 

### `abs_oneArray_le`

 The entries of the one array have absolute value at most `30W + 10`. 

 ## The one-array instance of a node 

### `Node.abs_arr_le`

 The entries of the three arrays of a node are bounded by the number `2U + 1` with which its
one-array instance is built. 

### `Node.conv_iff_convOne`

 The three-array instance of a node and its one-array instance have the same answer. 

### `Node.abs_oneArray_le`

 The entries of the one-array instance of a node have absolute value at most `60U + 40`. 

### `reduction_correct_oneArray`

 `reduction_correct` with one-array instances, read at length `8 * mPar n U ^ 2`. 

 ## The three-set inputs of the whole reduction 

### `bdd_image`

 The values of `x` are bounded by `2U`. 

### `bdd_twiceSet`

 The elements of `twiceSet x` are bounded by `2U`. 

### `bdd_zero`

 The set `{0}` is bounded by anything. 

### `bdd_zeroSet`

 The set `zeroSet x` is bounded by anything. 

### `card_image_univ_le`

 `n` numbers have at most `n` values. 

### `card_twiceSet_le`

 `twiceSet x` has at most `n` elements. 

### `card_zeroSet_le`

 `zeroSet x` has at most one element. 

### `IsInput`

 The three-set inputs on which the whole reduction runs `reduction n (2 * U)`. 

### `IsInput.split`

 The set of values, split by two binary digits: for the solutions with three distinct
  values. 

### `IsInput.twice`

 For the solutions `a, a, -2a`. 

### `IsInput.zero`

 For the solution `0, 0, 0`. 

### `exists_isInput_iff`

 A property holds for one of the three-set inputs iff it holds for one of the splittings or for
one of the two further inputs. 

### `threeSum_iff_exists_input`

 Three entries of `x` at different positions sum to 0 iff one of the three-set inputs has a
solution. 

### `mem_allNodes_iff`

 The nodes of the whole reduction are the nodes of the trees of the three-set inputs. 

### `IsInput.admissible`

 Each three-set input has at most `n` elements in each set, of absolute value at most `2U`. 

### `admissible_of_mem_allNodes`

 Each node of the whole reduction has at most `n` elements in each set, of absolute value at
most `2U`. 

 ## The whole reduction 

### `instances_correct`

 **Correctness of the whole reduction.**  Let `x` consist of `n ≥ 1` integers of absolute value
at most `U`.  Then three entries of `x` at different positions sum to 0 iff one of the instances,
read at length `8 * mPar n (2 * U) ^ 2`, has a solution. 

### `length_instances_le`

 **Number of instances**: at most `(2 (Lam (2U))² + 2) (2⌊log₂ n⌋ + 2)⁵`. 

### `abs_instances_le`

 **Entries of the instances**: they have absolute value at most `120U + 40`. 

### `scanPairs_le`

 **The searches look at no more than (number of nodes) · 2m · 3n pairs.**  This bounds the count
`scanPairs`, which we define; it is not a running time. 
