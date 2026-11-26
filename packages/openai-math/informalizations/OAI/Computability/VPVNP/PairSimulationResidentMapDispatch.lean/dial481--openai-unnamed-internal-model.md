---
{
  "module": "OAI/Computability/VPVNP/PairSimulationResidentMapDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatching a resident map by its demand grid and party

Each fixed grid row and party has a distinct matrix image. The selected term
stores the demand ordinal, and the resident directory supplies the party. Two
finite comparison chains decrement these ordinals until they reach their own
images. No public constants beyond the zero and one registers are needed.


### `Cases`

 A separate test and subtraction instruction for each fixed alternative. 

### `Cases.items`

 Cases in ordinal order, starting at zero. 

### `Cases.test`

 Address of each case's test for a zero index. 

### `Cases.subtract`

 Address of the decrement that skips each unmatched case. 

### `Cases.target`

 Destination when the corresponding case matches. 

### `Cases.bad`

 Destination when the case list is exhausted. 

### `Cases.index`

 Register holding the remaining ordinal. 

### `Cases.zero`

 Register used as zero by the comparison instruction. 

### `Cases.one`

 Register used as one by the decrement instruction. 

### `start`

 Enter the first case test, or the rejecting continuation if the list is empty. 

### `Linked`

 The machine tests the current index and decrements it before testing the next case. 

### `ticks`

 Dispatch takes two ticks per skipped case and one for a matching case. 

### `run`

 A valid ordinal reaches precisely its own table image. Any unused ordinal
exhausts the chain and enters the rejecting continuation. 

### `Program`

 The first fixed table transfers to the selected grid's party table. 

### `Program.grids`

 First-stage table indexed by the demand-grid ordinal. 

### `Program.parties`

 Second-stage party table for each grid. 

### `hit`

 The two-stage native dispatch uses the stored grid and party ordinals.
All registers outside those two operand words survive both comparison chains. 
