---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdvicePrepared.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePrepared.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePrepared.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the evaluator's advice banks in physical memory

First the native packer reads the raw length. The next call validates it and
publishes four operand frames. The prefix packer takes its operands from the
first published frame, and the ordinal packer fills the lookup table. The
four stages run successively on the memory produced by their predecessors.


### `PreparedLayout`

 The public operands and their allocated address intervals. The cursor
bounds cover the reset column as well as every data column. 

### `lengthMemory`

 Memory after the initial length pack, whose only output is the length
at frame offset 22. 

### `rawOperands`

 Five dynamically published operands of the prefix stage. 

### `rawMemory`

 Memory after frame publication and prefix packing. 

### `preparedAdviceMemory`

 Final memory of the four native stages. 

### `prepared_length`

 The frame program reads the newly packed length at its designated address. 

### `PreparedImage`

 Final readback of the four operand frames and the three packed banks.
Outside the frame interval, packed prefix and ordinal table, memory agrees
pointwise with its value before the length stage. 

### `PackHistory`

 Exact deterministic call sequence, costs and post-memory of one native
packing bank. 

### `preparedSources`

 Source readback in the successive input memories of the three native
packing stages, using only the copied header bits. 

### `prepareAdvice`

 Source images, native reports and final data for the consecutive length,
frame, prefix and ordinal stages. The prefix machine sees its public words
through the just-published operand loader. 

### `PreparedImage.frameData`

 All four dynamic operand loaders still read their complete frames after
both data banks have been packed. 
