---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Shaving/Network.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Shaving/Network.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Shaving/Network.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantitative reduction of trivalent compression to stages and lookup

`R j d s u` describes the intermediate realization after `j` stages,
with `d` copies, size `s` counting stations and ports, and arity at most
`u`. It can track the admissible table dictionary at each stage.
`T d m` describes a trivalent realization over the original field.


### `Stage`

 One arity reduction with an integer size budget. 

### `Finish`

 Batch lookup followed by descent from a degree `O(log h)` extension. 

### `budget`

 In the large-cost case the descending size envelope leaves enough
room for every exterior bit, even after rounding down. 

### `shave`

 All parameters except the power bound are fixed before the replication
slack `κ` is specified. The cutoff for `n` is uniform in the input tensor. 


# From wide networks to compression

Packing, substitution and field descent preserve the exterior labels.
The same field is used throughout each sequence of arity reductions.


### `Compresses.lists`

 Compression of arbitrary tensors specializes to the independent lists. 

### `compresses_of_stages`

 Theorem 2.1 from ordinary-width sorting and the one-stage arity
reduction. Batch lookup, descent and iteration are all proved here. 
