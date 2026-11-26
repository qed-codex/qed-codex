---
{
  "module": "OAI/Computability/VPVNP/ProgramLength.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ProgramLength.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ProgramLength.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Length of a literal coefficient-machine program

There are nine table rows per running state, each with at most two transition
records. A unary target takes at most one bit per state including the halting
states. This gives a quadratic bound for the self-delimiting program prefix.


### `programPrefix_length_le`

 Including its unary length header, a literal table has polynomial size in its state count. 
