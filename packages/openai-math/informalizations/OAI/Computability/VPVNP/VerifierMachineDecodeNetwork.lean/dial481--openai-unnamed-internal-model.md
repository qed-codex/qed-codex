---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean circuit for decoding a literal transition table

The circuit simultaneously tests candidate lengths and state counts. For each output
query it stores a bit at each possible endpoint of the prefix parsed so far. One
layer consumes a complete transition row. Once a candidate has consumed all its
rows, later layers copy its bits. The final disjunction checks the endpoint against
the outer length header.


### `decoder`

 Decode every output bit of the literal table from the same input fragment. 

### `decoder_eval_iff`

 Every accepted bit describes the unique program parsed from the input. 

### `decoder_size_le`

 The number of gates is polynomial even though the table is part of the input. 
