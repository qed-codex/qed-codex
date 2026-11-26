---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNodeGeneration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeGeneration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeGeneration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One fixed program for generating the nonzero quartic-node word table

The input is the explicit framed scalar alphabet. Eight real instructions
install the constant depth four. The tuple generator builds all four-word
records, and the verified record filter removes exactly the zero record.
No tuple array or node list is supplied as an input to this program.


### `program_runsIn`

 The complete finite program starts with only the supplied scalar alphabet. 

### `primitive_runsIn`

 The primitive compiler preserves the actual generated word table. 
