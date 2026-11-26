---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgramPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgramPairs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgramPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual depth-two tuple program builds all raw incidence-pair records.
Its input has one two-address record per incidence, not a quadratic table. 

### `rawPairProgram_runsIn`

 The fixed 83-instruction tuple generator produces the quadratic raw table. 
