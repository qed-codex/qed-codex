---
{
  "module": "OAI/Computability/VPVNP/RAMTapePublicExprCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePublicExprCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A fixed finite stack program for every live public operand expression

The syntax fixes the instruction table and the number of temporary registers.
Word width and operand values come from the parsed geometry at execution time.


### `extra`

 Number of extra registers required above the result slot to evaluate an expression
recursively. 

### `nodes`

 Number of syntax-tree nodes, counting geometry parameters and literals as leaves. 

### `compile`

 Compile the expression into a fixed register program that writes at its base and stages a
binary right operand one register higher. 

### `nodeCost`

 Quadratic step allowance for a single compiled expression node at the given word width. 
