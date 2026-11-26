---
{
  "module": "OAI/Computability/VPVNP/CircuitComposition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitComposition.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitComposition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Composition of exact arithmetic circuits

Concatenating two topologically ordered programs preserves their internal wires. A final
binary gate then computes the chosen operation on the two designated outputs.


### `Ref.reindex`

 Renumber the gate references while preserving scalar and variable inputs. 

### `Program.append`

 Append the gates of the second program after those of the first program. 

### `Circuit.combine`

 Combine the outputs of two circuits using one additional binary gate. 
