---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEntryZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the processor's global credit word

The parser leaves a width-sized stack of zero bits. Copying this stack to the
empty global credit register prepares the word consumed by the credit routine.


### `zeroGlobal`

 Copy the public width-sized zero template into the native global-credit register. 
