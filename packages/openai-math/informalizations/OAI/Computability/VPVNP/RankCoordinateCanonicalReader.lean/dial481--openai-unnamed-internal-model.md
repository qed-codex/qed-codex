---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateCanonicalReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCanonicalReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCanonicalReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A fixed coordinate callback for both operations of the evaluator

Starting from the raw indexed relation-entry reader, the installed program
performs pivot selection, computes the live target row, executes the two
determinants, divides their outputs and reclaims its workspace. Both operation
tables use the same advice and the same uniform clock and storage bound.


### `local instance : DecidableEq (PrefixPort K)`

 Decide equality of prefix-scan ports using the Gram engine's scan-port representation. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decide equality of auxiliary ports used while computing the rank of a prefix. 

### `local instance : DecidableEq (SelectedAdvice.Side K)`

 Compare addresses on one side of the selected-minor advice using their prefix-register
representation. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Host K J)`

 Compare selected-minor ports by distinguishing the row bank, column bank, and scalar
reader. 

### `local instance {J : Type} [DecidableEq J] : DecidableEq (SelectedMinor.Work K J)`

 Compare working ports of the selected-minor reader using the underlying submatrix
workspace. 

### `local instance : DecidableEq (SelectedAdvice.Parts K)`

 Decide equality across the disjoint banks used to prepare a selected Cramer query. 

### `program`

 Install the coordinate callback that prepares the two selected minors and divides their top
Schur coefficients. The common determinant sign cancels, yielding the matrix entry with the
next basis index as row and the current one as column. 
