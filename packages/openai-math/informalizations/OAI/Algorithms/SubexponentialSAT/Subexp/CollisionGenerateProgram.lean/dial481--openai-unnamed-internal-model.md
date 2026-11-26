---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionGenerateProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Generating and evaluating collision tuples with fixed control

The alphabet and unary tuple depth are input data. The generator and collision
stream are linked through actual stack ports. The current word table and the
two selected read plans remain runtime inputs and are preserved.


### `generated_schema`

 Every emitted tuple consists of exactly depth original alphabet words,
even when distinct word tuples have identical concatenated payloads. 

### `program_run_uniform`

 The generated tuples' schema is proved from the input word widths; no
assumption about a generated callback result is needed. 

### `score_program_run`

 One fixed routine generates every tuple, evaluates its collision, then
returns the exact successful-leaf count as unary data on stack 18. 
