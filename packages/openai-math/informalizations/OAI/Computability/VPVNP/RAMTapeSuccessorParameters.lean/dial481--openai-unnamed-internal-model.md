---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Building the global cost cap on the processor's stack tape

The input parser retains the unary site logarithm `d`, bucket capacity `H`
and word width `w`. Compute `e = ⌈log₂ H⌉` on a copy of the tally, then set
bit `d+e` in a zero word. For `H = 2^e` this produces exactly the w-bit
global cost cap `SH`, and retains all the tallies needed by the site.


### `Port`

 Unary dimensions, intermediate tally and scratch stacks, and the binary cap register used
to construct the global cost cap. 

### `bank`

 Store the site logarithm, bucket capacity, word width, bucket logarithm, and working count
in unary alongside the supplied cap bits. 

### `prepare`

 One fixed table, including both the logarithm and power-bit scans. 

### `capWord`

 The global cap word with value two to the sum of the site and bucket logarithms, when its
set bit fits the width. 

### `steps`

 Number of steps to construct the cap word from the site logarithm, power-of-two bucket
capacity, and word width. 

### `prepare_onPorts_runs`

 Install the parameter adapter in a caller's bank. Only the two output
registers are changed, and the work and temporary stacks return empty. 

### `steps_le`

 Linear in the unary inputs and the word length. 
