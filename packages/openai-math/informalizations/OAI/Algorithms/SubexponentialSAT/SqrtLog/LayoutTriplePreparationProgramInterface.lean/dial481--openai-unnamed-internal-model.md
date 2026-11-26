---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgramInterface.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgramInterface.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutTriplePreparationProgramInterface.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The factored triple stream uses the positive H cache directly. The outer
parity and both powers in a scalar summand are combined before serialization. 

### `factored_scalarProgram_runsIn`

 The unmodified scalar machine now returns the numerator itself. 

 The actual generated stream has the exact coefficient sum and nonnegative
mass required by the scalar machine, despite the factored cache representation. 

 One consumer-facing contract for native triple preparation. 

### `prepareProgram_factored_runsIn`

 The produced stream is already in the scalar machine's exact triple order.
Its signed sum is the numerator and its total is the no-cancellation budget. 

### `unsignedCache`

 Cache representation supplied by the native unsigned cache builders. 

### `unsignedCache_contract`

 All representation hypotheses needed by the native preparation theorem
follow from the native H/Pascal builders' unsigned rows and the power word. 
