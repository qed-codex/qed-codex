---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory reads of the fixed AB launch recipes

The row-indexed workers derive their public words from four level scalars,
the first scratch-table head and the AB-bank head. Each prologue parameter
is an affine base, a stride, or the zero bias.


### `Supported`

 Evaluating the AB recipe's row count, four input column heads, two strides and bank origin
reads only the allowed memory region. 

### `ab_supported`

 Exact block operands need four scalar and two table-pointer reads. 
