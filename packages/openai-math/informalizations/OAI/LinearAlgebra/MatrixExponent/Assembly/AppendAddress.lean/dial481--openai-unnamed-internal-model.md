---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/AppendAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/AppendAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/AppendAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # An exact binary reduction with one additional carry bit per level 

### `cheap_total`

 The cost grows linearly with the number of entries for fixed input width. 


# Electing a common choice from local scores

Rows have short scores even when the number of rows is large.
Accumulate each column along a carry tree before comparing the totals.
Sort with a deterministic tie break by candidate number.


### `election`

 The polynomial in the host address length is incurred just once per
candidate. Per host and candidate the cost only depends on the score width. 


# Applying a common weighted table at each occurrence

Carry the graph once per host. A product of the local weights both
rejects invalid choices and withdraws any prescribed scalar factors.



# Computing a layout from the selected profile tags

Each row presents an activity bit and a short selector. Inactive rows
contribute zero. The comparison is global, but the cost per row depends
only on the size of the profile dictionary.


### `pick_eq_side`

 Any order and padding of the selected profiles give the same decision. 


# Computing the global layout from short local records

At each host, pair the mask with one selector per row. Inactive
positions can contain arbitrary data and are normalized to zero.


 # Selecting one marked stub at each block 

 # Concatenating the high and low parts of a row address 

### `append_pin`

 Each bit of the concatenation is a fixed bit of one input address. 


# Simultaneous expansion of host neighborhoods

For one fixed walk use one batched indirect read per step. Add the
costs before estimating the degree, so the exponent of the overhead
is independent of the walk length.



# Neighborhood expansion without replicating long names at each block



# Short adjacency masks

Each entry compares a neighbor of a listed host against a second
listed host. Batched reads pay for the long addresses only while
preparing the masks.



# Weighted updates on two nested neighborhoods

Use one lookup table shared at every occurrence. Expanded views
are temporary; only the output records and original host graph
are carried across the stage boundary.

