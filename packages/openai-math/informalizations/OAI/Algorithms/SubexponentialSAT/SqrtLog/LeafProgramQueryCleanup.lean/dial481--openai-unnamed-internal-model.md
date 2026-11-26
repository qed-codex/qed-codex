---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryCleanup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryCleanup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramQueryCleanup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid reclamation after one marked or accepted query. The port list is part
of the fixed program syntax. Only the collector, immutable formula/row inputs,
and the outer caller's high ports survive. 

### `cleanupPorts`

 The fixed lower-workspace cleanup table, kept opaque so elaboration does
not reduce its 768 candidates while checking unrelated resource proofs. 
