---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Accounting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Accounting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Accounting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A crossing in two adjacent cells 

### `Socket`

 A cell with one designated seam temporarily removed. 

### `crossing`

 Both endpoints keep their original seam order. The signs are
absorbed into the scalar weight of the branch. 

 # Exact local transformations inside a closed sewn surface 

### `replace`

 Change the local contraction while leaving all shared levels fixed. 

### `reconstruct`

 Interpolate a cell simultaneously for all exterior assignments. 

### `rotate`

 Rotate two blocks of stations into position for fusion. 

### `crossed`

 Replace both ends of one seam. Other cells ignore the new private wire. 

### `cross`

 The outside sum indexes orders, levels and regular evaluations. The
residue state is an ordinary wire inside each resulting network. 


# States of the motion procedure

An active station carries its crossing count. A residue, including an
original auxiliary mark, is passive. A collector keeps its name and
position. Ordinary wires created on crossing are numbered in order
of creation and contracted separately from the seam indices.


### `Ready`

 At most one mover is away from its initial cell. 

### `Step`

 Support of one expansion step. Branch weights are separate from
the transition, so the same invariants apply to all linear combinations. 

 # Incidence, stationary positions, and selection of the next mover 

### `Layout`

 A static, loopless seam incidence pattern. 

### `Valid`

 Dynamic invariants of the motion procedure. 


# Energy and progress of the motion procedure

Each active mark keeps one reserve; a stationary residue has no reserve.
All energies use units of `1 / (2P)`. In particular the public seam
energy is multiplied by `P`.


### `tally`

 A local sum over the marks, independent of their order and tables. 

### `potential`

 Each remaining hop pays for the new residue and one step of progress. 

### `merge_bounds`

 At a continued fusion the total mobile energy does not grow.
Only terminal fusion is allowed a positive Laurent order. 
