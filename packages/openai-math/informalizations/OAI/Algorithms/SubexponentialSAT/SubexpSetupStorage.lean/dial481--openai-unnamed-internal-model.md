---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSetupStorage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupStorage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupStorage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical storage operations for the closed parameter setup

All copies, clears, and register resets are fixed instruction sequences or
calls to proved bit programs. Their state transformations below are assertion
notation only. The setup program uses them to isolate dirty arithmetic
subroutines from the persistent parameter words.


### `invoke_eval`

 This rule consumes an actual subroutine trace. It does not postulate a
semantic-function instruction or an unproved runtime. 

### `isolated_eval`

 Copy/clear overhead is derived from actual instructions around an actual
callee trace. No unproved semantic or timing callback is introduced. 
