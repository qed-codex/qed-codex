---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingIncidenceProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete incidence collision scoring from raw two-word read plans.
The fixed legacy program constructs its selection tables and all four-word
completion tuples at runtime. No precomputed collision table is an input. 

### `ValidRawPair`

 Each incidence reads an original-variable word and a factor word. 

### `inputBound`

 Fixed polynomial in the original input sizes, before preparing any table. 

### `command_eval`

 The raw-plan builder executes its real selection and tuple loops. The
output is a framed unary count for each candidate, in candidate order. 

### `program_runsIn`

 A single finite BitProgram, independent of the incidence instance. 
