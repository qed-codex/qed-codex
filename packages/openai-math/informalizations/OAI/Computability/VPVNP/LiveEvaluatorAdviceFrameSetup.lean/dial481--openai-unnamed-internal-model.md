---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the middle-group operand frames

The length word at frame offset 22 specifies how many bits of the reserved
prefix belong to the evaluator. Its value is checked against the capacity.
The computed destination for runtime fields follows the actual prefix on
the tape, while the order table begins beyond the reserved prefix in the
distributed advice. Quotient and remainder round the number of packed
words up without adding the full word width to the prefix length.


### `FrameCode`

 A native advice-frame initializer flow with 32 registers and eleven public operands. 

### `FramePub`

 The eleven public words supplied to the midpoint advice-frame initializer. 

### `lengthAddress`

 The address at frame offset 22 that stores the actual evaluator prefix length. 

### `actualLength`

 Read the evaluator prefix's actual bit length from its reserved frame cell. 

### `prefixRows`

 Number of packed prefix words, computed from the checked exact length. 

### `runtimeBase`

 The first runtime field address on the tape after the input data and actual evaluator
prefix. 

### `skeletonSize`

 The total word count of the runtime skeleton computed from the two public dimensions. 

### `scatterBase`

 The first exponent-scatter destination after the leading runtime fields. 

### `loadOps`

 Public operands are advice base, prefix capacity, width, frame base,
packed prefix base, radius, old-state base, exponent width, exponent bank
length, incoming exponent base and permutation map base. 

### `setup`

 Read and validate the actual prefix length and field width, then compute destinations and
the rounded-up prefix row count. 

### `ready`

 The bank of computed operands before publication. 

### `setupEvents`

 The initializer's load events followed by the local ticks used to compute the four frames'
operands. 

### `actualLength_at`

 The validated length is read at the ordinary reserved address. 

### `prefixRows_val`

 Exact natural word count in the prefix packer's fifth operand. 

### `ready_congr_length`

 The initializer's register calculations depend on the read length alone. 
