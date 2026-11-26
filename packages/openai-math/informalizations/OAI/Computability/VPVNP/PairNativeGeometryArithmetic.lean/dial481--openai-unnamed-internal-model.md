---
{
  "module": "OAI/Computability/VPVNP/PairNativeGeometryArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometryArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometryArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed powers and literals in the live pair's native registers

Both pieces are finite instruction text. Their lengths depend only on a
fixed integer from the program. They preserve every register except their
destination and produce one tick per instruction.


### `Code`

 Instruction flows for computing the pair geometry in twelve registers with access to the
eleven public words. 

### `Register`

 An index in the twelve-register bank used by the fixed-power and literal-loading routines. 

### `power`

 Raise the source register to a fixed natural power, starting from one. 

### `literal`

 Produce a fixed natural literal using only two-bit literal text. 
