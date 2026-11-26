---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseSelfFilterProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseSelfFilterProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseSelfFilterProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete fixed-master clause filtering

This wrapper performs the actual initial copy, record scan, cleanup, and
record-order restoration. Its input and output are on stack 13; every other
stack is empty at both boundaries.


### `selfFilter_eval`

 A complete finite-program execution; the master copy and all temporary
records have been consumed when the ordered output is returned. 

### `selfFilter_runsIn`

 The concrete in-place filter returns exactly the selected ordered list,
with no hidden callback or external execution premise. 
