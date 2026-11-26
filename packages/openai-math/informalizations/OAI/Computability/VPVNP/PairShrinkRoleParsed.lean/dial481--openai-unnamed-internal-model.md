---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleParsed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleParsed.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleParsed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Retaining the actual argument of a successful native parse 

### `Parsed`

 A concrete result of the reader on some finite input stream and entry scratch. 

### `Realizes.withParsed`

 In addition to the native postcondition, the continuation can use the fact
that the data came from the very reader it is linked to. 
