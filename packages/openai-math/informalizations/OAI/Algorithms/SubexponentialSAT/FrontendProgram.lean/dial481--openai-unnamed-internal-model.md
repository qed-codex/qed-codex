---
{
  "module": "OAI/Algorithms/SubexponentialSAT/FrontendProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FrontendProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FrontendProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual initialization of the canonical SAT input

The nineteen-label program splits the variable-count header and counts its
unary marks into a binary stack word. The untouched encoded CNF body remains
on stack 0. All growing values live on Boolean stacks, not in finite control.


### `storage`

 Body, unary work, binary variable count, and counter scratch. 

### `initializeProgram`

 The port maps are fixed once. Counter input/output/scratch are stacks 1/2/3. 

### `initializeBound`

 The direct sum of the two checked instruction bounds. 

### `initialize_raw`

 Actual raw-input initialization. The formula body is preserved on stack 0,
the binary count is on stack 2, and both work stacks are empty. 

### `initialize_sigma`

 The same fixed program applies uniformly across the dependent input type. 

### `initialize_formula_primitive`

 The checked compiler gives a primitive-tape execution from the actual raw input. 
