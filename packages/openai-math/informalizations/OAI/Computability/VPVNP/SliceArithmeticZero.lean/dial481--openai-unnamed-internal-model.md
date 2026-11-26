---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Testing a packed field element for zero

A two-state bit scan records whether every bit is zero. It saves the input in
reverse order on a scratch stack, then restores it before returning the single
output bit. The running time depends only on the length of the packed input.


### `Port`

 Input, decision flag, and scratch ports of the packed scalar zero test. 

### `State`

 Finite control that tracks whether all bits seen so far are zero while reading, saving, and
marking the result. 

### `machine`

 After the scan, move the input back from scratch in its original order. 

### `frame`

 The packed input, flag suffix, and saved bits at a stage of the zero-test scan. 

### `machine_runs`

 One output bit, with the input restored and scratch empty. 

### `vector_runs`

 On a canonical scalar the flag is true precisely when its coefficient
vector is zero. An arbitrary existing flag suffix is retained. 
