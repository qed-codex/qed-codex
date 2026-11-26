---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BinaryArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinaryArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinaryArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic on explicit little-endian bit lists

Natural numbers occur in the specification and in theorems about trace lengths.
The data routines inspect Boolean values and list constructors only.


### `mul`

 Shift-and-add multiplication; no natural-number arithmetic is executed
by this data routine. Leading zero bits are allowed in its output. 

### `length_mul`

 A deliberately loose output-width bound that needs no normalization. 

### `AddCfg`

 Three bit stacks and a three-valued finite control register. 

### `addStep`

 One fixed-size block consumes at most one bit from each input and pushes
one result bit. No length, toNat, or natural arithmetic is evaluated here. 

### `add_trace`

 Exact number of executed stack blocks, not a cost annotation on toNat. 

 A fixed finite TM2 program implementing exactly those adder blocks. 

### `addMachine_correct`

 The finite stack machine executes a linear number of its fixed blocks. 

### `addMachine_micro_correct`

 Expanding the fixed blocks gives a measured trace of actual one-constructor
stack operations. A stack-to-primitive-tape compiler is still separate. 

 Source-level bit-event traces for the recursive multiplication routine.
The lists below record inspections, Boolean gates, and constructed list cells.
They are not asserted to be PrimitiveMachine execution traces. 

### `carryAddRun`

 Executable writer-style interpretation: result bits and primitive source
events are produced together, without using natural-number arithmetic. 
