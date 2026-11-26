---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinate-major representation of a complete local basis table

The encoded search enumerates one square table and a split position.  Rows
are ambient coordinates and columns are basis vectors.  This module proves
that this representation covers every successful kernel/complement pair.
No transpose or basis search is performed by these definitions.


### `unflattenTable`

 View a flat coordinate-major vector as a square table. 

### `flattenTable`

 Read the entries of a square table in coordinate-major order. 

### `flatTableEquiv`

 An executable bijection; it uses quotient/remainder indexing only. 

### `tableRows`

 Coordinate-major rows, directly consumable by a matrix/vector scan. 

### `tableEntries`

 Coordinate-major flat entries. 

### `tableEntries_eq_flatten_rows`

 The flat index order is exactly the matrix scan's row concatenation. 

### `splitPair`

 Split a square coordinate-major table into its first `d` columns and
its remaining columns. 

### `tableOfPair`

 Read a successful pair as one coordinate-major square table. The
dimension equality is used only to certify the second column index. 

### `tableOfPair_splitPair`

 Joining a split table returns exactly its original entries. 

### `splitPair_tableOfPair`

 Splitting the table of a pair with the full ambient dimension returns
the exact pair, including its dependent dimension indices. 

### `headCoefficients`

 Restrict a full coefficient vector to the first group of columns. 

### `tailCoefficients`

 Restrict a full coefficient vector to the remaining columns. 

### `joinCoefficients`

 Join coefficient vectors in the same column order used by `splitPair`. 

### `coefficientEquiv`

 Full coefficients are equivalent to the two restrictions. 

### `matrixMap_eq_combine`

 Multiplication of the coordinate-major table is exactly the sum of the
kernel-tuple and complement-tuple linear combinations. 

### `dimensions_add`

 Correct kernel and complement data necessarily contain exactly `N`
basis vectors in total. 

### `goodPair_is_splitPair`

 The square-table search space covers every valid pair, independently
  of the order used to enumerate tables or split positions. 

### `goodPair_is_flat_splitPair`

 Enumerating flat vectors of length `N²` and split positions covers every
valid pair; no separately prepared matrix representation is assumed. 

### `exists_good_splitPair`

 At least one square table and split passes the actual pair specification. 
