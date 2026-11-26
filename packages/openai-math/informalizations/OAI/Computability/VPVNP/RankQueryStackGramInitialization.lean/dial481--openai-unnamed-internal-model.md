---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackGramInitialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramInitialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramInitialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Input bank and bounds for the physical weighted Gram interpreter 

### `initial`

 Put the two matrix dimensions, the field arithmetic advice, and the
underlying entry reader's initial work bank on their literal ports. 

### `ready_length`

 Size of every auxiliary stack at an instruction boundary, independent of
the time spent by the matrix entry reader. 
