---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One row of the table interpreter

For each possible row ending at a specified input position, the expression
tests its literal encoding and the preceding position's reachability wire.
The row predicate can restrict the transition record for a particular lookup.


### `rowBits`

 Concatenated unary fields of one machine row, including the branch count. 

### `rowStep`

 Reachability of a row endpoint, using the previous layer's start-position wires. 

### `rowStep_size_le`

 The number of possible rows is quadratic in the number of states. Each literal
test costs at most linearly many gates in the input length. 
