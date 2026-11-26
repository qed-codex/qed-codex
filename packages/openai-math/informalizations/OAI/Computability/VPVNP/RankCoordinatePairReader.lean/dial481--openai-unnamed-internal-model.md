---
{
  "module": "OAI/Computability/VPVNP/RankCoordinatePairReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePairReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePairReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Running two ordinary determinant queries inside the evaluator reader 

### `PairedHost`

 Workspace of the two Schur determinant engines and their quotient routine. Each engine has
a Gram-engine auxiliary bank and reads ordinary entries of its own square minor. 

### `pairCore`

 Construct the coordinate callback from the two literal matrix-entry routines and a common
preparation stage. 

### `pairTime`

 Clock allowance for preparation, both determinant queries, field division, result copying,
and workspace reclamation. 

### `pairCore_bounded`

 With the roots staged from advice and the matrix-address parameters
installed, the fixed reader makes the two determinant calls itself. 
