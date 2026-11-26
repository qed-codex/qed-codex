---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Contracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Contracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Contracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM after Chan and He, as a program.  Specifications

Theorem 21(a), after [CH20, Theorem 5.1].  This file contains no program
and no proof.  It states the specifications of the routines of the reduction: the general library,
the routines below the recursion tree, the tree, and the routines that prepare the splittings.  The
proof of a routine uses only the specifications of the routines that it calls.

* The pure models are the definitions of the reduction themselves (`ChanHe.coll`, `heavy`,
  `modulus`, `Node.oneArray`, `nodes`, …), applied to finite sets.  A set lies in the memory as a
  list without repetitions, in any order, with its length passed beside its address (`SetAt`).
* The specification of a routine is a proposition `XSpec lim P p …`: "procedure number `p` of the
  program `P`, run on these arguments in a memory that satisfies this, ends within `tX` steps with
  this result in a memory that satisfies that" (`Meets`).  It is proved for every program that holds
  the body of X at the number `p` and meets the specifications of the routines that X calls.
* The last argument of most routines is the free pointer `fr`; such a routine writes only its output
  segments, the count table (which it leaves as it found it), and cells from `fr` on.
* The count table: `cap` cells from `cnt`, below every free pointer, all zeros between calls
  (`ZeroAt`).  A routine that uses it clears what it wrote.
* Time functions are definitions.  The time function of a caller is written in terms of those of its
  callees.
* Limits: one hypothesis `(xNeed …).Ok lim fr d`, or a field of the structure that collects the
  hypotheses of the routine.


 ## Vocabulary 

### `SetAt`

 The `len` cells from `a` hold the elements of the set `S`, each once, in some order. 

### `ZeroAt`

 The `cap` cells from `cnt` hold zeros. 

 ## Time functions and needs 

### `tEmod`

 The time of a remainder of a number of absolute value at most `V`. 

### `emodNeed`

 What a remainder needs: words for doubled multiples of the modulus, and a cell for each of
them. 

### `tResid`

 The remainders of `len` numbers. 

### `tTally`

 One pass over `len` remainders that changes their counts. 

### `tColl`

 The colliding pairs of a set of `len` numbers: remainders, counting, a pass that adds up, and
removing the counts. 

### `tHeavy`

 The heavy elements of a set of `len` numbers: remainders, counting, a pass that copies, and
removing the counts. 

### `tSearch`

 One search: every candidate prime costs three collision counts. 

### `tModulus`

 The modulus of a node: two searches, and the collision counts modulo the first prime. 

### `tNodeArray`

 The array of a node: the padding pattern, and for each of the three sets remainders, counting, a
pass that writes, and removing the counts. 

### `wordNeed`

 The words that the routines below the tree need, for sets of at most `n` numbers of absolute
value at most `V` and moduli up to `M`: products of a collision count and a number of primes,
thresholds of the searches, entries and indices of the arrays. 

### `residNeed`

 The needs.  A caller's need covers its callees': the remainders of a set take `len` cells, a
long division `log₂ (V + 1) + 2`; the depth is the number of levels of calls below the routine. 

### `collNeed`

 The need of coll and of heavy. 

### `modulusNeed`

 The need of modulus; the moduli are at most `m²`. 

### `nodeArrayNeed`

 The need of nodeArray. 

 ## The generic library

The logarithms, the remainder, the sieve and sorting of the general library meet these
specifications (`EmodSpec` is below). 

### `tLog2`

 The time of log2. 

### `Log2Spec`

 log2(x) returns `⌊log₂ x⌋` (0 for `x = 0`); it touches no cell. 

### `Clog2Spec`

 clog2(x) returns `⌈log₂ x⌉` (0 for `x ≤ 1`); it touches no cell. 

### `tPrimes`

 The time of the sieve. 

### `primesNeed`

 The need of the sieve: a table of `m + 1` cells. 

### `PrimesSpec`

 primes(m, out, fr) writes the primes up to `m` in ascending order to `out` (room for `m` cells)
and returns their number. 

### `tSort`

 The time of sorting. 

### `sortNeed`

 The need of sorting: `n` cells, and a level of calls for each halving. 

### `SortSpec`

 sort(n, a, fr) sorts the `n` cells from `a` in place, in ascending order. 

 ## Remainders, counts, collisions, heavy elements 

### `EmodSpec`

 emod(x, M, fr) returns `x % M`, for `M ≥ 1`. 

### `ResidSpec`

 resid(len, s, sg, M, key, fr) writes the remainders of `sg · x` modulo `M`, for the `len`
numbers `x` from `s`, to `key`.  `sg` is 1 or -1. 

### `TallySpec`

 tally(len, key, cnt, δ) adds `δ` to the cell `cnt + k` for each of the `len` numbers `k` from
`key`. 

### `BucketMem`

 A set of `len` numbers of absolute value at most `V` at `s`, and a table of zeros at `cnt` with
a cell for each remainder modulo `M`; both below the free pointer, and apart. 

### `CollSpec`

 coll(len, s, M, cnt, fr) returns the number of colliding ordered pairs of the set at `s` modulo
`M`. 

### `HeavyOut`

 Where the output of heavy stands: below the free pointer, apart from the set and the table. 

### `HeavySpec`

 heavy(len, s, M, out, cnt, fr) writes the heavy elements of the set at `s` modulo `M` to `out`
(room for `len` cells) and returns their number. 

 ## The modulus of a node 

### `PrimesAt`

 The primes up to `m`, in ascending order, lie in the `np` cells from `pr`. 

### `Slot`

 A set in the memory: the address and the length of its list, and the set. 

### `Env`

 What the routines below the recursion tree share: the free pointer `fr`; the bounds `n` on the
sizes of the sets and `V` on their elements; the bound `m` on the primes, their number `np` and the
address `pr` of their list; the address `cnt` of the count table of `m²` cells. 

### `Env.Ok`

 The primes up to `m` and the count table are in the memory, below the free pointer and apart. 

### `Slot.Ok`

 A set of at most `n` numbers of absolute value at most `V` is in the memory, below the free
pointer and apart from the count table. 

### `NodeArgs`

 A node of the recursion tree in the memory: its three sets, and what the routines share. 

### `NodeArgs.sets`

 The addresses and lengths of the three sets, as the routines are given them. 

### `NodeMem`

 The three sets of a node, the primes and the count table are in the memory. 

### `SearchArgs`

 The arguments of search: a node, the factor `mult` of the moduli, and a bound for each set. 

### `SearchArgs.vals`

 The values of the arguments of search. 

### `SearchArgs.Good`

 A candidate `q` is good: each of the three sets has at most `bᵢ / np` colliding pairs modulo
`mult · q`. 

### `searchNeed`

 The need of search. 

### `SearchSpec`

 search(mult, s₁, l₁, s₂, l₂, s₃, l₃, b₁, b₂, b₃, np, pr, cnt, fr) returns the least good prime
up to `m`, and 1 if there is none. 

### `NodeArgs.modulusVals`

 The values of the arguments of modulus. 

### `ModulusSpec`

 modulus(s₁, l₁, s₂, l₂, s₃, l₃, Λ, np, pr, cnt, fr) returns the modulus of the node. 

 ## The array of a node 

### `NodeArrayOut`

 Where the array of a node is written: `8 m²` cells from `y`, below the free pointer and apart
from the three sets and the count table. 

### `NodeArraySpec`

 nodeArray(M, s₁, l₁, s₂, l₂, s₃, l₃, V, m, y, cnt, fr) writes the first `8 m²` cells of the
one-array instance of the node to `y`. 

 ## The recursion tree 

### `treeCalls`

 The number of calls of the recursive procedure: one for the triple, and those of the three
children if the triple is a node. 

### `tNode`

 The cost of one node, when a Convolution-3SUM solver takes `T N B` steps: the modulus, the
array, the call, and the three sets of heavy elements. 

### `tNodes`

 The time of the recursive procedure. 

### `nodesNeed`

 What the recursive procedure needs with `f` levels to go: a set of heavy elements for each
level, one array, and what the solver needs. 

### `CtxAt`

 The block of parameters that the recursive procedure gets by its address `cx`: `V`, `m`, `Λ`,
`np`, `pr`, `cnt`. 

### `NodesPre`

 What the recursive procedure assumes with `f` levels to go: the memory of a node, the block of
parameters at `cx`, below the free pointer and apart from the count table, and the limits. 

### `NodeArgs.calls`

 The number of calls of the procedure for the tree with `f` levels below a node. 

### `TreeYes`

 Some node of the tree of a three-set input gives a yes-instance. 

### `NodeArgs.Yes`

 The one-array instance of some node of the tree with `f` levels below a node in the memory is a
yes-instance. 

### `NodesSpecAt`

 The specification of nodes for trees with `f` levels: see `NodesSpec`. 

### `NodesSpec`

 nodes(f, s₁, l₁, s₂, l₂, s₃, l₃, cx, fr) returns 1 if the one-array instance of some node of the
tree with `f` levels is a yes-instance at length `8 m²`, and 0 if not.  `T` and `r` are the time and
the need of the Convolution-3SUM solver that it calls. 

 ## The front: distinct values, multiplicities, binary digits, the splittings 

### `tDistinct`

 The time of distinct. 

### `tTwice`

 The time of twice. 

### `tZeroThree`

 The time of zeroThree. 

### `tBits`

 The time of bits. 

### `tPick`

 The time of pick. 

### `Distinct.Ctx`

 What distinct assumes: the sorted list stands at `a`; the three regions lie in the memory and do
not meet; addresses and counts fit in a word. 

### `DistinctSpec`

 distinct(n, a, val, mul): the `n` cells from `a` hold a sorted list.  Writes its distinct values
to `val` and how often each occurs to `mul` (room for `n` cells each), and returns the number of
distinct values. 

### `twiceList`

 The doubles of the values that are not 0 and occur at least twice. 

### `Twice.Ctx`

 What twice assumes: the values, of absolute value at most `V`, stand at `val` and as many
multiplicities at `mul`; the three regions lie in the memory, and the output meets neither of the
others; addresses and doubled values fit in a word. 

### `TwiceSpec`

 twice(nd, val, mul, out) writes the doubles of the values that are not 0 and occur at least
twice to `out` (room for `nd` cells), and returns their number. 

### `ZeroThreeSpec`

 zeroThree(nd, val, mul) returns 1 if the value 0 occurs at least three times, and 0 if not; it
writes no cell. 

### `bitTable`

 The table of the binary digits of the labels: digit `β` of the label of the `i`-th element in
cell `i Λ + β`. 

### `Bits.Ctx`

 What bits assumes: the list of numbers of absolute value at most `V` stands at `s`; the labels
have `Λ` binary digits, and `2^Λ` is not much larger than they are; the list and the table lie in
the memory and do not meet; addresses and doubled labels fit in a word. 

### `BitsSpec`

 bits(len, s, V, Λ, bt, fr) writes the table of the binary digits of the labels `x + V` of the
`len` numbers from `s` to `bt` (`len Λ` cells).  It does not use the free pointer. 

### `pickList`

 The elements whose digit `β` is `x` and, unless `two = 0`, whose digit `β'` is `x'`. 

### `Pick.Ctx`

 What pick assumes: the list stands at `s` and the table of its digits at `bt`, `Λ` cells for
each element; the two positions are below `Λ`; the three regions lie in the memory, and the output
meets neither of the others; addresses fit in a word. 

### `PickSpec`

 pick(len, s, bt, Λ, β, x, β', x', two, out) writes the elements selected by one binary digit
(`two = 0`) or by two to `out` (room for `len` cells) and returns their number. 
