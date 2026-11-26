---
{
  "module": "OAI/Computability/VPVNP/RankCoordinatePlannedReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePlannedReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePlannedReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The native Cramer entries at the common reader-plan budgets

A single advised width accommodates both orientations of the rectangular
matrix, the two monomial decoders and the target shift. The polynomial
space and logarithmic time estimates for the planned minor apply to each
operation and both runtime basis ordinals.


### `local instance : DecidableEq (PrefixPort K)`

 Compare prefix-rank scan ports when mounting the planned minor readers. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decide equality of workspace ports for the planned greedy row and column selections. 

### `local instance : DecidableEq (Select.Side K)`

 Compare addresses within one pivot-selection bank using the prefix-word register layout. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Host K J)`

 Compare addresses of the two pivot banks and the scalar-reader portion of a planned minor. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Work K J)`

 Decide equality of the planned selected-minor workspace ports through the submatrix
reader's representation. 

### `native_reads_of_plan`

 Passing `canonicalFits` for the reader plan supplies every shape, width
and target bound. The two matrices use the common planned minor budget. 

### `planned_ready_bounds`

 Both auxiliary states at instruction boundaries share the planned
height bound, including the three live target arguments. 
