---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed stack programs for the quartic coefficient arithmetic

Persistent word registers are separate from the destructive scalar workspace.
Each instruction copies its two operands into that workspace, executes a scalar
program, and moves the answer back. One additional stack suffices for the copies.


### `store`

 The bank, eight scalar stacks, and a single copying stack. 

### `addCode`

 Four scalar additions, retaining both input quartics. 

### `mulCode`

 The literal 49-operation Horner circuit from `SubexpQuarticRing.mulRun`.
Slots 0--3 hold the reduction coefficients, 4--7 the left operand, and
8--11 the right operand. Every scalar result has its own persistent slot. 

### `addConstant`

 Fixed absolute constants: neither the program nor its primitive simulation
overhead depends on the prime, exponent, or input words. 
