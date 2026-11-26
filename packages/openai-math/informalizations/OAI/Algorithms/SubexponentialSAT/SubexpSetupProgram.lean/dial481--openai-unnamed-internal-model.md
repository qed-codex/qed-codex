---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSetupProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A closed program for the growing numerical setup

The clause width, dyadic control parameter, and extra workspace are fixed before
the input. Every phase below is a named finite bit program. Inputs are copied
from persistent storage into a reusable workspace, outputs are copied back,
and the entire local subroutine workspace is physically cleared after return.

The protected threshold extension is disjoint from both ordinary workspace and
the thirty-two persistent scalar slots. Its producer is the fixed-width
threshold-table compiler.


### `Config`

 All fields are fixed before reading the input formula. 

### `guardRegister`

 The decision bit is separated from the arithmetic work registers. 

### `stage`

 A statically allocated real subroutine call, with physical copy and cleanup
instructions. The program argument is instantiated below by named bit tables. 

### `numericSetup`

 Every listed arithmetic operation is a concrete previously defined program. 

### `scalarCommand`

 Small-log inputs exit with a false decision bit before positive-divisor
arithmetic is invoked. The good branch computes all scalar guard operands. 

### `workspacePorts`

 All ordinary workspace is cleared before the next top-level phase. The
protected threshold extension and persistent slots are outside this list. 

### `ScalarValues`

 The numerical data relation that the closed setup will establish. 
