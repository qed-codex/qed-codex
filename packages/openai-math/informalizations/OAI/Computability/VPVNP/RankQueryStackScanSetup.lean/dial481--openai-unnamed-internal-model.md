---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackScanSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackScanSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackScanSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing a child call or a completed Schur sum 

### `borrowPorts`

 Wire the decrement routine to the live remaining-count field, a scratch stack, and the
engine's condition port. 

### `test`

 Decrement the remaining count and signal whether the scan has exhausted its product terms. 

### `finish`

 Return the completed accumulator, clear the live frame fields, and signal completion of the
scan. 

### `descend`

 Compute the left child's words, set the saved direction and select descent. 

### `scan`

 Inspect the remaining count, then stage the next left child or return the completed Schur
sum. 

### `right`

 Prepare the second child of a summand. Its suspended frame receives the
just-returned left operand before the result port is cleared. 

### `succ_runs`

 A positive loop counter prepares the left continuation and the pending child. 

### `right_runs`

 The left value changes ports while its parent's query and count are restored
for the right-child dispatcher. 
