---
{
  "module": "OAI/Computability/VPVNP/RAMVirtualParametersCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualParametersCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualParametersCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the virtual site count on the private word RAM

The public words give the input length and live address width. Two ceiling
logarithms suffice to compute the least virtual site count and its bucket
size in Section 11. All iterations and arithmetic fit in a live word.


### `program`

 Fixed finite instruction text, with the length and address-width public slots supplied by the caller. 

### `ticks`

 Number of executed instructions, including the final test of each loop. 

### `Result`

 Integer parameters in the final register file, including both powers of two. 

### `programRun`

 Executing the fixed word program computes the prescribed virtual parameters
for each length at least two and each live address multiplier at least one. 

### `programExecute`

 A linked occurrence transfers control to its continuation with the computed
registers, the same branch bits, and the private and external memories it received. 
