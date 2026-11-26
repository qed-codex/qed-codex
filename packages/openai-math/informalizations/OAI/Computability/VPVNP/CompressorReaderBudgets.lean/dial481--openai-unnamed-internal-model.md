---
{
  "module": "OAI/Computability/VPVNP/CompressorReaderBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorReaderBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorReaderBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Uniform raw matrix-reader budgets for the actual compressor equations

The widths and the two bounds are fixed for the input length and circuit-size
exponent. They cover the prime and affine slice selected from any circuit at
that length, all integer equation queries, and the operation-dependent target
row. The word width can be increased for the outer rank computation.


### `compressorReaderPlan`

 Reader plan sized for the compressor's equations, joint labels, degree bound, and advised
prime header. 

### `readerDegreeBudget`

 Upper bound on the extension degree needed by the compressor reader at the given
characteristic and input length. 

### `readerLimbBudget`

 Arithmetic limb-width budget derived from the compressor's prime-header width. 

### `compressorRawReaderBudgets`

 The bank, peak space and binary clock exponent supplied to the actual
Macaulay reader are polynomially bounded before selecting the circuit. 
