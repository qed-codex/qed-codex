---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDenseProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDenseProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDenseProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite control for dense coefficient projection

The controller below is an actual finite instruction table. Its local callback
contract is deliberately an actual `StructuredCalls.Eval` of a fixed program:
it must be discharged by the concrete lookup and record-emission programs.
It is not an assumption that an abstract ring operation takes one machine step.
The concrete callback integration and product-pair builder are separate stages.


### `projectionController`

 The program is independent of the number of retained slots. Its callback
is a fixed finite subprogram, not a run-time supplied operation oracle. 

### `projectionController_run`

 This theorem contributes the entire measured outer slot loop, including
frame parsing, list markers, guards, and termination. The only local premise
is the actual trace of the fixed lookup/emission callback on one slot. 

### `projectionController_cost`

 A fixed per-slot lookup bound is charged once per actual parsed slot. 

### `bitProject_records`

 Exact relation between the per-slot emitted record and the already
verified bit-key projection algorithm, in the same slot order. 

### `unpack`

 Unpack the reversed payload supplied by the outer record iterator.
Both output fields are forward bit lists. Port 5 is arbitrary preserved data. 

### `program`

 Count the actual key bits into a unary width, retaining the original key.
The table is fixed; no numeric width is compiled into its instructions. 
