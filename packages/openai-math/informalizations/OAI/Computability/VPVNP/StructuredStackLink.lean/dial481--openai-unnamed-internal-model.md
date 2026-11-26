---
{
  "module": "OAI/Computability/VPVNP/StructuredStackLink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackLink.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackLink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executing a structured routine inside its caller

Installed instructions keep the same stack labels. The last ordinary
instruction returns directly to the caller's continuation.


### `Runs.link`

 A deterministic run transfers to its caller without changing its cost. 
