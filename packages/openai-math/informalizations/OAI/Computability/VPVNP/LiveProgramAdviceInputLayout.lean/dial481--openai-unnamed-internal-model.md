---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdviceInputLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceInputLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceInputLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The live program's midpoint tape layout

The old state bank contains a head-relative two-tape window. The raw prefix
starts at its central cell, followed immediately by the evaluator runtime
fields. All scatter sources lie in the earlier header workspace, and the
permutation lookup table lies beyond both configuration banks.


### `copyBank`

 The four fixed prefix-copy operands, in order the tape radius, old state base, packed
prefix base and word width. 

### `stateBank`

 Evaluated control-state operands that target the old evaluator configuration bank. 

### `initialLengthMemory`

 Memory after the length packer has stored the active raw prefix's length. 

### `skeletonBank`

 The four runtime-skeleton operands evaluated using the stored prefix length, including the
suffix start and size. 

### `scatterBank`

 The five operands of the exponent scatter, with its tape destination determined from the
stored prefix length. 

### `InputRegions`

 Address order and exact words supplied to the subsequent three stages. 

### `inputLayout`

 All capacities and nonaliasing conditions for prefix copy, skeleton and
scatter on the three published operand banks. 

### `beforeFrame_preserved`

 In particular the four stages do not touch the old configuration or the
header's incoming exponent bank between the reserved tag and frame base. 

### `suffixFrameData`

 Every physical operand loader in the final three middle stages reads the
four- or five-word bank computed from the validated raw length. 

### `preparedInput`

 Starting in the tagged prepared memory, the prefix copier reads exactly
the evaluator prefix, the scatter sees the incoming exponent and order words,
and every cell of the previously initialized control bank is preserved. 
