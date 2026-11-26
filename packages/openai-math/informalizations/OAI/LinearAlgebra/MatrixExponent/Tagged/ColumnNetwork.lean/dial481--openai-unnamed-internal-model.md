---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Tagged/ColumnNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/ColumnNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/ColumnNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lifting short sorts by four parallel passes

In a grid with `c` columns of height `2*r*c`, where `c ≤ r`, four
passes of independent column sorts suffice. Between passes the wiring is
fixed. Grouping the first and last half-columns together in the final
pass avoids sentinels.


### `Grid`

 Column number first, position within the column second. 

### `witnesses`

 A large entry after sorting has a witness to its left before sorting.
Dually, a small entry has a witness to its right. 

### `interlace`

 Sorting two sequences which interlace with displacement `d` preserves
that displacement. At most `d` inputs are unmatched. 

### `deal`

 Deal entries cyclically from each old column into the new ones.
Indices map from the new layout back into the old. 

### `align`

 Read the sorted columns in row-major order into aligned blocks. 

### `crossing`

 Between distinct aligned blocks, an inversion must cross from the
second half of one block to the first half of its immediate successor. 

### `stagger_le`

 Within each staggered block the two layouts give the same order. 

### `stagger`

 Map aligned positions to their slots in the final pass. Block zero
contains the two end halves in their original order. 

### `afterThree`

 All remaining inversions after pass three lie in one staggered block
per inversion. Sorting that block then resolves the inversion. 

### `fourPass`

 Each pass invokes one short sorter per column. 

### `factor`

 A full tuple sort factors through four calls to the parallel short
sorter. The three permutations are fixed before the input is given. 

 # Wiring four layers of parallel short sorting networks 

### `Model`

 Column lifting uses only composition and reordering. The same proof
works for trivalent gates and high-arity sorting gates. 

### `sort_lift_batch`

 Combine groups of `2^v` short sorts, preserving independence between
the `t` resulting long sorts. No factorization of the input network is needed. 

### `sort_lift_iterate`

 Each full lift multiplies the address length minus two by at least 3/2.
The cost of `k` lifts is at most `4^k` times the initial batch size. 
