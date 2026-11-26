---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpComputedWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComputedWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComputedWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computed weights for reconstructed r-group inputs

Field addition happens before the arbitrary coordinate lift.  Disjoint
supports prove that a reconstructed input equals the base outside all color
supports and equals base plus the own-color increment on each color support.
These facts discharge the exact monomial split used by the executable kernel.


### `outsideCoordinates`

 Enumerate the complement of the supplied color supports. 

### `reconstruct`

 Reconstruct the full field assignment before applying any coordinate lift. 

### `momentWeight_reconstruct`

 Exact splitting of computed weights, derived from support and field
reconstruction.  The coordinate lift is an arbitrary function. 

### `enumerationFiberEquiv`

 Convert the explicit enumeration's product target to the dependent-fiber
form consumed by the executable kernel correctness theorem. 

### `enumeration_weight_split`

 Exact computed weight factorization for the explicit layout enumeration.
Increment support is discharged from layout membership, not assumed as a
global factorization property. 

### `enumeration_kernel_weight_split`

 This is precisely the `hw` premise of the r-group kernel bridge, with
the weights computed on a base point and one own-color increment. 

### `enumeration_outsideCode_denote`

 The raw outside scalar code discharges the kernel's local `hC` premise. 

### `enumeration_insideCode_denote`

 The raw one-color scalar code discharges the kernel's local `hW` premise. 

### `enumeration_single_color`

 With zero representatives for the other colors, the local group input
is exactly the outer base plus its own increment. 

### `computedBlocks`

 Actual outer/inner block lists with computed scalar weights.  The only
programs supplied externally here are the individual group expressions. 

### `execute_computedBlocks_eq_separatedJet`

 The kernel bridge with all scalar-code denotation, weight splitting,
and finite-list enumeration premises discharged.  Only the supplied group
expression semantics and its independently provable own-coordinate
invariance remain as local program premises. 
