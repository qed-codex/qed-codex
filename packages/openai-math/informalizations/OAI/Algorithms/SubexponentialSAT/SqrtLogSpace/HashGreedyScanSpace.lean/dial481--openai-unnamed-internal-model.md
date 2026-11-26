---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyScanSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyScanSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyScanSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Uniform storage for the actual streamed candidate scan. The attempt
premises describe executions and prefixes of the fixed preparation/query/padding
command; the complete query implementation must instantiate them. No bound in
this module uses the number of candidates as a space bound. 

### `body_space`

 Only the local native comparison time is used to bound comparison
workspace. The potentially expensive attempt has its independent prefix bound. 

### `visits_space`

 Every callback and increment of the real scan shares this bound, including
the last overflowing increment. The cardinality of the scan is absent. 

### `scan_halt_space`

 The complete scan, its initialization and final halt have the same storage
cap. Determinism transfers the proof to any execution of this fixed command. 

### `stage_space_of_halt_space`

 The scan bound can be used directly as a stage inside the actual round. 

### `round_halt_space`

 The actual complete round uses the same fixed polynomial storage cap:
one seed attempt, native install, the uniform scan, native append, and the
charged guard reset. The entry cap includes all previously retained history. 

### `rounds_halt_space`

 All outer rounds retain only the attained history and a shrinking unary
counter. The history byte allowance is explicit and polynomial in the original
round count and row width; exponentially many losing rows are never retained. 
