---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the physical reader's field lengths

Copy the unary input length before computing the address width and the live
bucket on separate passes. The incident width calculation reads both results,
after which the bucket tally can be erased. The raw input and the reader's data
fields are carried through every pass.


### `Work`

 Work ports for the saved length, unary bucket, and the separate bucket and incident-width
computations. 

### `Scratch`

 Scratch bank for preparing the physical input fields with the bucket and width subroutines. 

### `routineKeep`

 The only length-dependent data are on stacks. The finite control depends
on the fixed address multiplier and rational exponent. 

### `routine`

 A parser-only run erases the bucket tally after preparing the two lengths. 

### `readerFrame`

 The parameter stage preserves all reader stacks outside its working registers. 

### `bank`

 Parser stacks with their literal input and the unary counters. 

### `prepBudget`

 Sum of instruction bounds for the five passes. 

### `budget`

 Step budget for preparing field widths, including erasure of the unary bucket copy. 

### `runs_keep`

 Keep the bucket tally for subsequent validation after parsing the address and incident fields. 

### `runs`

 On the physical input tape the address and incident counts become available
to the parser and all private scratch stacks finish empty. 

### `clockCoefficient`

 A constant depending only on the address multiplier and fixed exponent. 

### `budget_le`

 A polynomial clock for preparing both input fields, uniform in the tape length. 
