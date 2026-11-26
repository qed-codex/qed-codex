---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQuerySetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete preparation and fresh high-counter initialization for the fixed
marked and accepted queries. The witness below is produced by the actual
programs; no implementation or evaluator is supplied as a hypothesis. 

### `PreparedRun`

 A factual output bundle for the fixed preparation and seed instructions.
All semantic objects and resource assertions refer to these same evaluations. 

### `PreparedRun.eval`

 The measured prefix of the actual fixed successful branch. 

### `local_space`

 Preparation is polynomial work, so its local step bound controls only
visible growth; untouched caller words contribute a separate maximum. 

### `prepare_seed`

 The actual prepared run is constructed from the concrete frontend output
and its serialized scalar bounds. Arbitrary suspended caller words affect
only the separate frame bound, never the preparation or seed time. 

### `marked`

 Marked setup starts with the actual staged record, executes reference
staging exactly once, constructs the real ring, and initializes the current
high mask. Scalar bounds are on canonical physical frontend lengths. 

### `accepted`

 The accepted query executes actual false-flag staging and the same
concrete preparation on history-only sources, retaining the full ambient n. 

### `PreparedRun.guard_loop`

 The actual guard is tested at the frontend output before preparation.
An actual high-loop continuation therefore installs into the original fixed
syntax, paying the conditional microstep once. 
