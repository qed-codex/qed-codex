---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterResourcesWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterResourcesWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterResourcesWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private work of the scheduled pair counter

The two input passes use the live address width, and the parser's word guesses use
fourth powers of that width. For a fixed address multiplier their dispatched costs
both fit the auxiliary machine's per-call private-work budget at large lengths.


### `eventually_privateWork`

 The `n^10` private-work bound includes six elementary operations per instruction
and the fixed dispatch overhead of the full coefficient counter. 
