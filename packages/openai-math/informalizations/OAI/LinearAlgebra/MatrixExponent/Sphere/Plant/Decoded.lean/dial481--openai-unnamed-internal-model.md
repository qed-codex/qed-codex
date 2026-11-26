---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Plant/Decoded.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Plant/Decoded.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Plant/Decoded.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Signs in the transposition of a matrix of generator blocks

Reordering blocks uses only their lengths modulo two. The formula
therefore also applies with doubled energies in place of lengths.


### `wick_append`

 If no pair crosses a boundary, the perfect matching sum factors. 

### `interlace`

 Number of transpositions when interleaving two rows of blocks. 

### `shuffle`

 Transpositions in changing from site order to species order. 

 # Signs within and between blocks of species 

### `shuffle_blocks`

 Once the intra-block signs are known, the remaining sign only
uses the total occupancy of each block at each mark. 


# One auxiliary probe per coded mode

The covectors are prescribed only on the mode prefixes used in the
fixed-energy codes. The remaining modes have higher normalized weight.


 # Ordered wedges and their single-species components 

 # Factorization of the sphere form into independent species 

### `wick_species`

 The sign only uses the parities of the individual wedges. 

### `wick_two_groups`

 When the first group has even length in every species, its
shuffle sign and the second group's shuffle sign are independent. 


# Planting one species with linearly many auxiliary marks

Site `i` carries `b i` coded bits, using the first `4 * b i` modes.
After rescaling weights at each site, all tested modes cost at most
eight and every untested mode costs strictly more. Thus interpolation
of just the tested modes suffices under a total weighted budget.


### `decoded`

 Extend a bit table by zero to all unrecognized words. 

 # Occupancy words for the auxiliary marks 

### `response`

 The contribution of one species of the auxiliary state. 


# Planting across independent species

Only the total energy at each original mark is fixed. This fixes the
total weight across species. If one species exceeds its budget, a
second is under budget and its selector vanishes. Thus exact levels
at every mark in every species follow without a separate check on
each seam.


### `auxSign`

 Sign exponent of the auxiliary occupancy table. 

### `joint`

 A joint state on auxiliary sites. Each coefficient factors over
species, apart from the known shuffle sign. 

### `plant_joint`

 Linear-size auxiliary positions and a product state enforce the
prescribed bit table on each species, given only total leg energies.
The same one-species state works for every replication count. 

 # Wiring coordinates on the original marks 

### `markCode`

 Encode one packet for every species at a fixed total energy. 

### `joint_decoded`

 Sum over all coded, independently addressable packets. Any assignment
that disagrees with any original mark contributes zero. 
