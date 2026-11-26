---
{
  "module": "OAI/Computability/VPVNP/RAMTapeStacks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStacks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStacks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Elementary bit-stack instructions

A stack step changes at most one bit. All unbounded data belong to the stacks.
The named control can inspect a popped bit, including the empty-stack case.
Binary choices preserve their two branch slots.


### `StackOp`

 One finite-control instruction acting on a named stack bank. 

### `StackCode`

 Instruction table for the bit-stack machine. 

### `Stacks`

 A bit list for each named stack, with its top at the head. 

### `StackStep`

 A single deterministic, continuing instruction. The stored pop
continuation branches on its actual symbol. 

### `StackRuns`

 A deterministic sequence of exactly the given number of stack instructions. 

### `stackPaths`

 Accepting leaf multiplicity up to a stack instruction bound. 

### `StopsWithin`

 Every branch halts within the stated number of elementary instructions. 
