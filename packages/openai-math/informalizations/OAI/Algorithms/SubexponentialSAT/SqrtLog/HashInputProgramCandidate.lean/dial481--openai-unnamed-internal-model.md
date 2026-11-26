---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCandidate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCandidate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramCandidate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The assembler receives exactly the selector's raw candidate bytes. Its
source is a serialized original formula, and its result is a produced inline
row, with every raw tuple occurrence retained. 

### `assemble_serialized_candidate_runs`

 This theorem starts from the selector's raw byte payload and the actual
source serialization. No inline weighted clauses are supplied as input. 

### `assemble_generated_candidate_runs`

 Every actual generated selector payload, not merely an extensionally equal
row, is accepted by the same fixed native assembler. 
