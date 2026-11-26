---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionOuter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionOuter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionOuter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The outer triangular loop of the fixed convolution controller. Each row
copies the preserved right-hand array, consumes one left coefficient, and
executes only the still-relevant output positions. 

### `outerStep_run`

 One actual row of the convolution, including preparation and cleanup. 

### `outerLoop_run`

 Actual execution of all remaining triangular rows. The proof invariant
tracks the remaining value computation and the physical unary counters. 
