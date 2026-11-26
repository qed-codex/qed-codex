---
{
  "module": "OAI/Computability/VPVNP/PairNativeCacheProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The private operand-cache program embedded in a final-vertex pair burst

The native arithmetic reads only the eleven public operands and the runtime
cache-base word. The store tail writes each result at its designated offset.
All labels and registers can be relocated in the surrounding vertex table.


### `args`

 Expression for the cache word at index `i`, in the order of the four virtual-machine
parameters followed by the 34 auxiliary public operands. 

### `bankSize`

 Number of native registers allocated to evaluate all 38 expressions and retain their
results for the cache stores. 

### `number`

 Index of a fixed leaf source in the cache vector, given by its offset from the private
cache base. 

### `resultReg`

 Register holding the evaluated word for leaf source `j` when the native arithmetic prelude
finishes. 

### `block`

 Native operand-vector program that derives the pair geometry and evaluates the 38 cache
expressions using bucket parameters `a` and `b`. 

### `relocated`

 Place the cache arithmetic in the caller's register bank through `reg`, keeping its eleven
public operand indices. 

### `template`

 Standalone initializer that runs the pair's 38 operand expressions in their native bank,
stores them at successive private addresses, and accepts. 

### `prelude`

 Arithmetic prepares every store source in its actual native register,
leaving registers outside the chosen embedding available to the caller. 
