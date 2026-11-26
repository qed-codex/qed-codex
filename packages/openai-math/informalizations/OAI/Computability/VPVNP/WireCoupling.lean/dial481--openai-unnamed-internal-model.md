---
{
  "module": "OAI/Computability/VPVNP/WireCoupling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireCoupling.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireCoupling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coupling the endpoint choices of two spectral wire intervals

The recursive split in Appendix A.3 keeps the two marked legs open at every
node. Dividing by the product of the ancestor diagonal-wire values gives a
subadditive binary tree, whose endpoint values obey the shrinking cost tables.


### `wireEndpointTable`

 The four pairwise distances between the endpoint choices. 

### `couplingNode`

 The two-mark tensor at a path in the exterior split tree. Each level is
chosen from the endpoint table *before* the new branch is taken. 

### `ancestry`

 Product of the values of the exterior-level wires along the ancestry. 

### `wireDistance_endpointCoupling_of_product_bound`

 The two-mark independent product inequality implies the bound for every endpoint coupling. 

### `wireDistance_endpointCoupling`

 Equation (A.3). Every coupling of the endpoint choices bounds the
distance between the two fractional points. 

### `diagonalCoupling`

 Pair the first endpoints and the second endpoints with equal interval parameter. 

### `fractionTransport`

 Lemma 2.2. Interpolating at the same fraction on two wire intervals
bounds the distance by the correspondingly weighted endpoint distances. 

### `realizable_fractionTransport`

 The spectral transport inequality passes to every jointly realizable
finite configuration by cancellation of the realization's positive scale. 
