---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramController.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramController.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingProgramController.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed dynamic assignment controller, specialized to the new exact
weighted scores. The producer contract is explicit and must be discharged by
an actual score-stream program; it is not a unit-cost score operation. 

### `ScoreProducer`

 The only remaining producer obligation is execution of a fixed command
which writes actual framed unary scores and restores the controller frame. 

### `controller_runsIn`

 All candidate and coordinate loops are existing fixed bit-machine loops.
Their cost is included. This theorem remains conditional on the concrete
producer's execution theorem, which is displayed in its type. 
