---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseFilterReverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseFilterReverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseFilterReverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Shared actual record reversal for the clause-filter storage layout. 

### `reverse_eval`

 Reverse whole records from stack 14 onto the encoded accumulator in
stack 13. All thirteen work stacks and payload stack 15 finish empty. 
