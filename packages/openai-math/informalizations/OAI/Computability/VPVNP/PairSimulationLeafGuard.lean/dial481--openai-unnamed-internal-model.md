---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafGuard.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafGuard.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafGuard.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Successor fields and the private choice bank of a virtual validator 

### `guardPort`

 Map a successor-check port into the leaf processor's cut-register bank. 

### `guard`

 The successor check with its ports assigned to the leaf's cut-register bank. 

### `stream`

 The choice-generation routine that reads the processor's public budget and fills its
private choice stack. 

### `finished`

 The successor-port stacks after finishing the incident record and computing the guard
verdict for the virtual site. 

### `guarded`

 The leaf's initial stack bank with the results of the successor guard installed on its
assigned ports. 

### `entered`

 The stack bank at interpreter entry, with the generated bits on the choice port and the
spent public budget cleared. 

### `entered_call`

 The interpreter receives every decoded cut, all public words, and the
generated bit string on the same ports used by its actual graph. 
