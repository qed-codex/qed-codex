---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Reciprocal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Reciprocal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Reciprocal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Sorting the two sides of a matching by source, then item or bin 

 # Circuits computing one rank per row with no factor for alphabet size 

 # First, last and other occurrences of a key 

 # Treating a tuple of fixed-width fields as one comparison key 

### `same_group`

 Comparing the counts in two fibers tests whether all rows in the
first fiber agree on their additional field. 


# Matching rows at equal rank

The first key distinguishes the two colors. The second key erases the
color and adds its within-color rank. Every active fiber of that key
contains at most one row of each color. Comparing two group counts
then tests that a thin item lies entirely in one thick bin.



# Bounded-fan-in costs for ordered matching

Use two rank comparisons per row. The costs depend polynomially on
the address and label widths and linearly on the padded array length.
They do not depend on the number of distinct keys or the item size.


 # Returning the matching mask and mate addresses in the original order 


# The matching decoded from the row circuit

The selected mask is constant on each thin item. On this mask the friend
pointer gives a distinct thick mate, with common destination for the item.


### `SortedControls`

 Both the mask and the mate address are specified, for every unit. 

### `Controls`

 The controls in original row order determine the entire matching. 

### `controlled_subround`

 Different colonies may share an array, with one source tag per colony.
Array positions and tags may depend on the affine coloring. 


# Reading a matching in either direction

The friend address is an involution even for an unused row. Looking
up the mask at that address therefore identifies all used thick units.

