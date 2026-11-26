---
{
  "module": "OAI/Computability/VPVNP/AdviceCountAdapter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCountAdapter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCountAdapter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Using the circuit-advice interpreter as a counting verifier

Each invocation copies the persistent advice, query, and current witness into
the interpreter's work stacks. After evaluation it transfers just the designated
output to the enumeration flag and empties the valuation stack. This restores
the state required for the next witness without copying the count itself.


### `AuxPort`

 Ports for the persistent query and advice, the circuit interpreter’s work stacks, and the
scratch stack used to copy its inputs. 

### `Port`

 The witness counter’s ports extended by the query, advice, and working stacks for the
Boolean circuit verifier. 

### `inputs`

 Persistent strings with every private work stack empty. 

### `verify`

 The verifier called by `UniversalCountStack.enumerate`. 

### `verify_runs`

 A successful advice program returns its first valuation bit to the flag,
restoring the complete persistent input and both counter registers. 
