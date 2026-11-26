---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StackCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


A global finite controller for one-head finite stack programs. A source step
first inspects one finite-alphabet stack top, then changes finite control and
keeps, pops, or pushes that stack. The compiled controller performs only the
primitive bit reads, moves, and writes of StackMachine.controlStep.


### `initialCfg`

 The source input stack uses its given Boolean interface; all other stacks are empty. 

### `compilerOverhead`

 This bound is fixed by the finite stack alphabet codes. 

### `one_step_execution`

 One source stack transition is implemented by actual primitive transitions. 

### `controller_simulation`

 The simulation theorem does not assume a cost annotation for stack operations. 

### `compiledMachine`

 The assembled finite control is a genuine primitive bit machine. 

### `primitive_one_step`

 Reindexing the finite controller changes no primitive transition counts. 

### `compiled_initial`

 Width-one input coding identifies the simulated input with the physical raw input. 

### `output_execution`


An actual source execution on raw input becomes an actual primitive-bit
execution with machine-fixed multiplicative overhead and the same answer.

