---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Stack-only contracts for the concrete copies, fixed-width reads, and unary
counter updates in the convolution controller. Register values are genuine
outputs of the executed commands, but are unrestricted between these blocks. 

### `Buffers`

 Runtime buffers, in order: left, right, accumulator, output index, row
index, row fuel, right suffix, cell fuel, current coefficient, left operand,
right operand. All other stacks form the scalar-service/caller frame. 

### `buffers`

 Proof-level state embedding; the executable code uses fixed numeric ports. 
