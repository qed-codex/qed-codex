---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Hold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Hold.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Hold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering pointers for packed intervals

Each record gives an inclusive start, exclusive end, and translation
modulo the address space. Empty or reversed intervals are inactive.
After sorting the starts, all queries run a parallel binary search.



# Carrying a public tape across the entire computation

Some protocols transport the physical payload only at termination.
Compose the control kernels first, and add a *single* identity on
the public tape. Its cost is independent of the number of stages.


### `Transforms.stages`

 There is no extra identity charge at each step of the iteration. 

 Parallel binary search on a vector of sorted addresses. 


# Computing the status masks for a frozen core

Read the status of each neighbor once, then duplicate the short
mask at each block. The label serialization only permutes bits.



# Deterministic grouping and coloring

The chosen mixer minimizes the number of splits. The affine coloring
maximizes the number of matched units for this grouping. Unused
host positions have score zero.


 The bucket ordinal is the occurrence rank in the vector of dyadic levels. 

 Near-linear circuit for assigning the ordered slots of a payload bank. 


# Distributing host records to dyadic slots

At each level, sort a one-bit key stably. The hosts of that level
come first, in increasing input order. Replace all inactive rows
by the padding value and retain the physical bucket's prefix.


 Only the address metadata passes through comparison sorting. 

 Each level uses a single controlled exchange of whole records. 

### `realize`

 Total redistribution, including when a bucket has too many entries.
In that case only the entries in its physical seats are retained. 
