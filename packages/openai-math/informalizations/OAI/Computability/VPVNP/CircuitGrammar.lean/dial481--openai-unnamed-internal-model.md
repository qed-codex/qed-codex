---
{
  "module": "OAI/Computability/VPVNP/CircuitGrammar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitGrammar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitGrammar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Graded parse labels for exact circuits

An exact circuit determines one assignment of the labels of the grammar of Section 8.1
of *VP and VNP differ over every field*. This assignment works simultaneously for all
homogeneous pieces up to the prescribed cutoff and for all gate, variable and output
states. It allows arbitrary field constants and does not require homogeneous intermediate
gate computations.


### `Circuit.exists_parseGrammar_on`

 A single assignment of the scalar labels represents the given circuit at every
state and every degree up to `D`. The state list can contain extra copies of any slot. 

### `Circuit.exists_parseGrammar`

 The start state computes the requested piece of the exact output polynomial. 

### `Circuit.card_grammarSlots`

 The state count is one plus the number of variables and binary gates. 

### `Circuit.exists_parseGrammar_fin`

 The prescribed rectangular table can be padded to any sufficiently large width.
The start slot is number zero (number one in the paper). 
