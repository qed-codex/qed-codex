---
{
  "module": "OAI/Computability/VPVNP/PairRefreshVertexInputWrites.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexInputWrites.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshVertexInputWrites.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External write footprint of the refresh vertex inputs

The level locator and each child header probe external memory. The child scan
stores the guessed half-wire bits in private memory. Its chronological trace,
including each choice, contains no external write.


### `NodeArguments.ChildScan.events_noWrites`

 Every ordered child row only reads the external descriptor and columns.
The bit payloads may be chosen arbitrarily. 

### `RefreshVertexAssembly.inputTrace_noWrites`

 The complete input trace for a typed old half leaves all external words
untouched, independently of the values returned by its probes. 
