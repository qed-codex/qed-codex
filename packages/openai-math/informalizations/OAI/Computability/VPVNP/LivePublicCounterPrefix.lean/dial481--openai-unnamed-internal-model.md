---
{
  "module": "OAI/Computability/VPVNP/LivePublicCounterPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicCounterPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicCounterPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading the two auxiliary operands read from the processor's own prefix

The live program has no copy of its own text in its instruction table. Its
fixed expression vector computes the length-only operands and leaves zeros
in the two prefix slots. It copies the prefix length and packed prefix from
the parsed input into those two slots.


### `shape`

 The finite expression vector whose instruction table is independent of the actual prefix. 
