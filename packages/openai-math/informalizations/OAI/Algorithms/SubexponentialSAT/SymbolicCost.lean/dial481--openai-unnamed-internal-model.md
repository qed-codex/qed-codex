---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SymbolicCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SymbolicCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SymbolicCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit lists for canonical symbolic coefficients

`project` scans a finite term list once for each supplied retained slot. Multiplication
first enumerates all input pairs and then projects. Duplicates are intentionally
allowed before projection. The counters below count scalar/index operations, not
primitive bit-machine steps; the latter need an implementation of the coefficient
ring and exponent vectors.


### `Retained`

 The actual three cutoffs for the manuscript's canonical representative. 

### `slotIndex`

 Convert a mathematically retained monomial to the executable array index. 

### `SlotEnumeration`

 The enumerator is explicit input data. Its generation cost is not asserted
here: each executable operation below works for every complete duplicate-free list. 

### `Dense`

 A dense list contains every supplied slot once, in the supplied order,
including slots whose coefficients are zero. 

### `coeff`

 Sum every occurrence of the requested coefficient by a sequential scan. 

### `project`

 Retain the supplied slots, with all duplicate coefficients collected. 

### `rowMul`

 One explicit row of the pair-product enumeration. 

### `rawMul`

 Enumerate all input pairs; this is an ordinary terminating list recursion. 

### `scanWithCost`

 Instrumented coefficient scan. Each cell charges a list visit, an index
comparison, and a scalar addition (including addition of zero). 

### `appendWithCost`

 Append with one charged list copy per cell of its left input. 

### `rowMulWithCost`

 Each pair charges one exponent addition, one scalar multiplication,
and one list-cell construction. 

### `rawMulWithCost`

 The outer multiplication loop also charges each row visit and the copies
performed by append. The result is the same raw pair enumeration as above. 

### `projectWithCost`

 Projection really performs one complete coefficient scan per output slot.
Two additional events visit the slot and construct its output cell. 

### `denseCost`

 Exact abstract-operation budget for multiplying two dense N-slot lists.
These events are scalar operations, exponent operations, and list visits/copies;
none is being identified with a primitive bit-machine transition. 

### `denseCost_retained_le`

 Conservative polynomial-in-D times M_X^4 bound, derived from the
instrumented list multiplication and the actual retained-slot cardinality. 

### `denseMulWithCost_bound`

 The bound applies to the cost returned by the actual executable operation,
for an arbitrary supplied complete ordering of the retained slots. 

### `denseMul_correct`

 All coefficients of the actual projected multiplication agree with full
polynomial multiplication at retained slots and vanish elsewhere. 

### `denseMul_denote`

 A list implementing the retained slots gives the genuine canonical
representative of the polynomial product. No quotient-ring evaluation is used. 

### `indexData`

 Actual serial data for an exponent index; the final entries are U and Z. 

### `unaryWord`

 Unary delimited encoding is sufficient for exponent indices, since their
values are O(D). Coefficients require a different (binary) encoding. 

### `equalBitsWithCost`

 A concrete bit-by-bit equality scan; the counter records actual inspected
bit pairs plus its terminal inspection. It is not a compiled TM trace. 

### `encodedScan`

 A coefficient scan on stored bit-string keys. Only coefficient addition is
abstract here: index equality is performed by the explicit bit-by-bit routine.
The counter charges bit inspections, scalar additions, and list visits. 
