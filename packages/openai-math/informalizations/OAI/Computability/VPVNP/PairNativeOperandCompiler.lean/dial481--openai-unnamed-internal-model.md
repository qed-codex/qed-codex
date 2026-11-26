---
{
  "module": "OAI/Computability/VPVNP/PairNativeOperandCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Compiling public expressions to native instructions within a pair burst 

### `logarithm`

 Evaluate an operand, pass it through the floor or ceiling binary-logarithm routine in fixed
registers 2 and 3, then copy the result back to its temporary slot. 

### `compile`

 Compile a public geometry expression into native instructions writing temporary slot
`base`. A binary operation evaluates its right operand one slot higher to retain the left
value. 

### `cost`

 Recursive tick bound for a compiled public expression. Literal costs grow with the literal
and logarithm costs grow with the machine word width. 
