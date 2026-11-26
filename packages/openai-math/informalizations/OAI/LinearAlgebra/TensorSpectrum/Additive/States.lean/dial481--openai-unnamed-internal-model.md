---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Additive/States.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/States.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Additive/States.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The compact additive-state space in Appendix A.1

This file proves the topological reduction to a finite inconsistent system. It
does not assert that this system has a solution: ruling out a finite obstruction
also requires the integer cone certificate and the tensor rank-growth argument.


### `stateSet`

 Normalized additive monotone states with the additional detection inequality.
Multiplicativity is deliberately not included. 

### `StateConstraint`

 Individual conditions, each of which uses only finitely many coordinates. 

### `coordinateBox`

 The coordinate box uses ordinary rank only as a finite upper bound. 

### `finite_inconsistent_subsystem`

 Compactness gives an actual finite subsystem when no state exists. 
