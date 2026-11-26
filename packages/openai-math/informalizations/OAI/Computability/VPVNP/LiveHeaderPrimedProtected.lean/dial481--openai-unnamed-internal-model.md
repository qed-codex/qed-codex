---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrimedProtected.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrimedProtected.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrimedProtected.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Protected memory in the primed header stages

The digit guard bounds both shifted output addresses, even for an arbitrary
persistent state. The digit and borrow values read from memory can be arbitrary
words since they only determine the data stored at those addresses.


### `init_protected`

 Every successful initialization call preserves all words below the stage tag. 

### `digits_protected`

 Every successful guarded digit call preserves the protected memory below the stage tag. 
