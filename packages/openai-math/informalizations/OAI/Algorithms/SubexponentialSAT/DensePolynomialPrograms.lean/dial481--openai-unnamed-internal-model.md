---
{
  "module": "OAI/Algorithms/SubexponentialSAT/DensePolynomialPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DensePolynomialPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/DensePolynomialPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed streaming program for dense polynomial addition

Quartic coefficients are four consecutive fixed-width base words. The loop
uses the actual modular-word addition program and tests the input stacks.
Its instruction table is independent of the array lengths and the width.


### `addCmd`

 The fixed program calls the same fixed modular-word routine at each step. 

### `wordStep`

 The generic loop premise is discharged by the existing actual scalar trace. 

### `addWordsTotal_values`

 Equal-length word arrays represent coordinatewise modular addition. 

### `wordVectorAdd_eval`

 The same fixed loop is a coordinatewise modular vector-addition machine.
Taking μ=1 specializes it to vectors over the prime field. 

### `preparedPolynomialAdd_primitive`

 Concrete prepared-quartic instantiation, with no callback-refinement premise. 

### `callAt`

 Relocate the fixed addition program into a caller's physical workspace. 

### `callAt_eval`

 The relocated call changes only its two input/output ports. The complete
bit-level addition trace, including its return instruction, is retained. 
