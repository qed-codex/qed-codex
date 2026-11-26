---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramAssignmentSemanticsCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramAssignmentSemanticsCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramAssignmentSemanticsCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Typed selected-ID semantics of the actual factor fold. Neutral IDs are
skipped, including in the output list; no redundant multiplication is added. 

### `selectedRun_denote`

 Indexed semantics allow distinct IDs to emit identical raw dictionaries.
No injectivity or artificial choice of a meaning for a raw dictionary is used. 
