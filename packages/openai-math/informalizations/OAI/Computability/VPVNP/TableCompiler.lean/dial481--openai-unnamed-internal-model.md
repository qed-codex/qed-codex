---
{
  "module": "OAI/Computability/VPVNP/TableCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TableCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TableCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic finite controls as literal transition tables

A control reads the head of the first tape and either halts or moves that head.
The compiled two-tape table preserves both tapes' symbols and the second head's
position. The ordering of the running states puts the given start state first.


### `Step`

 A deterministic read-only control action that halts with an acceptance bit or enters
another state with a specified motion of the first tape head. 

### `compile`

 The nine rows per running state, in the order used by the literal machine. 

### `running`

 Running configuration corresponding to a finite control state. 

### `moveTape`

 Motion of the read-only head, with the literal codes stay, left, right. 
