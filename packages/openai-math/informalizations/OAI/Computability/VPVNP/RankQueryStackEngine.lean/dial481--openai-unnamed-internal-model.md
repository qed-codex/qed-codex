---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackEngine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Return control for the physical determinant stack

The finite control dispatches a query, scans its summands and returns each
operand to the suspended parent. The result of a terminal descriptor and a
finished sum both enter the same return instruction. An empty direction history
signals that the root coefficient is ready. A nonempty history is restored
before the frame reader consumes the saved fields.


### `Port`

 Live and historical frame registers, the result, one condition bit and the
scratch or persistent ports of the installed scalar and dispatch routines. 

### `Actions`

 Each of the external calls returns normally and supplies its data on the
named ports. Describe emits a true condition for a scalar, scan for a completed
sum. Left and right children are placed in pending registers before the active
frame is pushed. 

### `Actions.describe`

 Inspect the active query and initialize its scan or signal a scalar result. 

### `Actions.scan`

 Advance the sum scan, signaling completion or preparing the next left child. 

### `Actions.activate`

 Move a pending child query into the live frame after saving its parent. 

### `Actions.right`

 Prepare the right child after the left factor's value returns. 

### `Actions.multiplyAdd`

 Add the product of the returned factors to the parent accumulator. 

### `Call`

 Subroutine calls of the stack evaluator, including frame saves and restores. 

### `Actions.callee`

 Select the installed evaluator action or built-in frame routine for a call tag. 

### `Admin`

 Controller states for inspecting subroutine results, restoring the frame direction and
rejecting invalid signals. 

### `State`

 Physical engine state, either a controller state or a program counter inside an identified
subroutine. 

### `invoke`

 Enter the specified subroutine at its initial program counter. 

### `routine`

 Execute the installed evaluator actions and frame routines under the call-and-return
controller. 

### `machine`

 The outer program is finite as soon as its component programs are finite. 

### `return_to_frame`

 Test the direction history without changing the bit at its top. 

### `return_to_caller`

 The empty continuation stack returns the computed root scalar to the caller. 
