---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashScopeProgramFromTuple.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashScopeProgramFromTuple.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashScopeProgramFromTuple.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Direct original-source-to-scope composition. The finite program first reads
raw tuple references and looks up original clauses, then extracts their scope.
No table of precomputed scopes is supplied to this machine. 

### `state_runsIn`

 The output is produced from raw references and the unexpanded original
clause bytes, including every zero-coefficient and repeated reference. 
