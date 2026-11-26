---
{
  "module": "OAI/Computability/VPVNP/LabelEvaluatorIndexedPins.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorIndexedPins.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorIndexedPins.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The indexed equations of the label evaluator's actual slice

An enumeration of the original equations is followed by one slot per
coordinate. The slot contains the advised coordinate equation when its mask
bit is set, and the zero polynomial otherwise.


### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 Finite enumeration of the ground field used to index possible values of pinned coordinates. 

### `Model.pinCut`

 The zero or affine pin in one coordinate slot. 

### `Model.indexedEquations`

 Numeric row order of the exact polynomial system presented by the advice. 

### `Model.queryData`

 Macaulay queries use the original integer coefficient reader and the
advised pins in the same order as `indexedEquations`. 
