---
{
  "module": "OAI/Computability/VPVNP/PairSimulationPrivateScratch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateScratch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateScratch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private arrays and pointwise dependence on the incoming memory

Writing a finite word array replaces precisely its addressed cells. Incrementing
a list of histogram labels depends at each address only on that address's original
contents. These operations describe the scratch state of a successful map call.


### `Memory`

 Contents of private scratch memory as a word-valued function of a machine-word address. 

### `write`

 The result of storing all values in a consecutive private array. 

### `outside_of_ne`

 An address distinct from every word in a natural-addressed array is outside
its natural interval. 
