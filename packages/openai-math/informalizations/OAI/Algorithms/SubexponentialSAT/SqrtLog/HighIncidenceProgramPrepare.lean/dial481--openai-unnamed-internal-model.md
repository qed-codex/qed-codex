---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Complete physical preparation from explicit scopes and binary n,t.
The input contains neither scope counts, mass, cutoff, nor unary loop fuel.
All are computed by fixed finite programs. The output mask retains all n
original coordinates and is in descending original-coordinate order. 

### `command_eval`

 Full prefix trace. Persistent input words and source scopes are retained;
output14 is the mask, output2 is unary n, and output13 is unary(cut+1).
Computed E1, unary S18, binary S19 and cutoff20 remain in their work ports.
Arithmetic work24--31 may contain leftovers and is outside the scan frame. 
