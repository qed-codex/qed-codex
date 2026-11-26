---
{
  "module": "OAI/Computability/VPVNP/ShrinkMonomialWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkMonomialWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkMonomialWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Monomial witnesses of the shrinking kernels

For fixed old half-wires and new half-wires, a vertex first chooses each
absorbed word owned by it. It then performs the syntactic entry check of
every six-party map resident at that vertex. The successful choices retain
their parameter multiplicities in any coefficient ring.


### `partyProductWitness`

 At one packed site only the resident motif-party occurrences contribute
choices or labels to the product. 

### `partyProductWitness_totalExponent`

 The degree of one successful product is the sum of the individual
degrees at its resident map occurrences. 

### `shrinkLayoutEntryWitness`

 Product of the individual map witnesses in one concrete shrinking
layout. All row and column arguments come from the site's own old fields,
absorbed words and outgoing-network half-wires. 

### `shrinkKernelWitness`

 Witness for the actual kernel selected in (7.2). The outer witness
selects the absorbed words, and the inner witnesses count one parameter
per accepted copy of each resident matrix. 

### `shrinkKernelWitness_totalExponent`

 In a successful shrinking-kernel witness the degree is exactly the
total number of base repetitions read by its resident map occurrences.
The choice of absorbed words does not itself contribute a parameter. 

### `shrinkKernelWitness_degree_le`

 The complete kernel degree at a site obeys a linear envelope in the
largest incoming width, uniformly over selected layouts and witnesses. 
