---
{
  "module": "OAI/Computability/VPVNP/CompressorTermWorkerRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native execution of a complete term-descriptor visit

The strided worker uses one fixed pass table for all motif ordinals.
Its only nondeterministic instructions read the selected outer vector.


### `motifPass`

 The same finite instruction table handles every row at every machine width. 

### `motifData`

 Assemble the address operands and grid, repetition, and payload constants for the selected
motif template. 

### `budget`

 Instruction allowance for one fused term call at the given word width and maximum demand
width. 

### `budget_linear`

 For a fixed motif, the instruction cap grows linearly with machine word width. 

### `strided_addresses`

 Row arithmetic in a strided scan agrees with the natural addresses reduced to words. 

### `native`

 Every admitted tape returns the successor ordinal and the complete term
record. Conversely, at every sufficient cap, successful native calls consume
exactly the canonical outer-choice tapes. 
