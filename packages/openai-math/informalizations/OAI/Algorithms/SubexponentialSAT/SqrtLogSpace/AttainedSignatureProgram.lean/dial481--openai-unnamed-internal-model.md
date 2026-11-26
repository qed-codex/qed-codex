---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native full-key computation for the resumable attained-signature scan

One invocation preserves the assignment and all raw integer constraint rows.
Its local polynomial-time bound controls every scratch stack at every source
prefix. The generator retains candidate and predecessor cursors separately.


### `key_eq_iff`

 Every physical bit in the complete key is retained; equality is precisely
full integer-signature equality, including every original raw row. 

### `prefix_stack_bound`

 A complete per-key execution has polynomial local time. This estimate is
applied to that invocation only, never to the exponential outer traversal. 

### `command`

 The two compared words and the surrounding frame survive comparison. 

### `prefix_stack_bound`

 Every prefix includes both preserved key words, the comparison copies,
all cleanup scratch and the persistent caller frame. 

### `updateFresh`

 Reject only a duplicate full key; keep scanning to charge and complete all
predecessor work independently of success. 

### `body`

 One predecessor is processed by actual full-signature and byte-equality
programs; the assignment counter is incremented only after all scratch is free. 
