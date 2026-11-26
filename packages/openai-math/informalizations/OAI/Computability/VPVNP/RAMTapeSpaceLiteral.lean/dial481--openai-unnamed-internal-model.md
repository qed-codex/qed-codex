---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpaceLiteral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceLiteral.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceLiteral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Head displacement of a literal compiled table on a choice string

A bit selecting an instruction contributes the two moves in that record.
Rejection of an invalid choice and all padding after a halt leave both head
positions fixed. The continuing records form a prefix of a path through the
source control with exactly the displacement of the whole literal run.


### `choiceMotion`

 Read the moves of the instruction actually selected by a witness bit. 

### `choiceDisplacement`

 Sum the moves from the literal rows, evolving the same configuration as
`acceptsChoices` on each bit. 

### `choiceDisplacement_path`

 Every prefix of padded witness bits has the net motion of a prefix of
continuing source commands, even when a later witness bit invalidates it. 
