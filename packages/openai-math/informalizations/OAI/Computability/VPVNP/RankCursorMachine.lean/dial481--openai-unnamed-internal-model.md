---
{
  "module": "OAI/Computability/VPVNP/RankCursorMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executing the outer rank scan

Each request returns one scalar Schur coefficient, the zero test selects
the cursor update, and the updated registers give the next request or the
rank. Only the current field element and binary degree pair survive a step.


### `rankMachine`

 The control, including its loop, is independent of every size parameter. 

### `RootRead`

 The root-query contract uses the actual binary indices, field scalar
encoding and live auxiliary matrix bank. 

### `rankMachine_runs`

 The physical run returns the rank in cursor register one. The input field
is the irreducible polynomial-basis extension in which the matrix was encoded. 
