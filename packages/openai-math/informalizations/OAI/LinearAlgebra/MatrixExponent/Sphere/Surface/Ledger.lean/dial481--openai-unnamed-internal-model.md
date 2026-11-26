---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Ledger.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Ledger.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Ledger.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Energy accounting during motion

Work in integral units. Mobile energy includes one reserve per mover.
At terminal fusion the increase in collector energy may be as large
as `1+2g` times the departing budget. Weight mobile energy by that
factor throughout. The local balance includes incident seam energy,
whereas the global balance does not.


### `Budget`

 Telescoping bounds between two states, independent of the number
of intermediate fusions, crossings or expirations. 

### `collect`

 Covers terminal fusion, continued fusion (`μ = 0`) and expiration. 

### `cross`

 A crossing transfers `γ` units between cells and spends at least
`μ` units of seam energy. Only the receiving cell needs the debit. 

### `limits`

 Current energy and crossing counts at any point of the procedure. 

 # Interpolating a cell in the common moving parameter 

### `token`

 Any argument not at a stationary position uses the moving parameter. 

### `reconstruct_cells`

 The interpolation weights are independent of station tables, external
assignments, and the states being summed on all incident seams. 

 # Changing the station order, including in a Laurent coefficient 

 # Merging two insertion tables at a collision 

### `Cell.merge`

 Evaluation at a collision is a finite sum of cells, with unchanged
ordinary parameters and no change to any seam. 


# The ordinary wire left by crossing a seam

Group the lowering operator by output energy. Each term replaces the
shared seam and creates an ordinary wire indexed by a private basis
state. The latter is summed inside the contraction.


### `crossings`

 Only collisions with a nonnegative seam level contribute. 

### `hop_basis`

 Crossing on basis states after resolving the lowered mover energy. 

 # Lifting a seam crossing from modes to insertion tables 

### `residue`

 The newly created ordinary wire carries a basis state of the
mover's private leg. 

### `transfer`

 Preserve the mover's ordinary wires and add the new private wire.
Project the transformed state to its selected energy. 

### `Passage`

 Local data for a Laurent coefficient crossing a specified seam. 

### `weights`

 The coefficients use only the local energies and positions. 
