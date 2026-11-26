---
{
  "module": "OAI/Computability/VPVNP/RAMLoggedCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLoggedCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLoggedCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Single-pass metered private call execution

The instruction interpreter uses the write log for private memory, reads a
private cell and its work count in the same scan, and threads the report and
operation count through the same call recursion.


### `Instr.actualLogWork`

 Charge the actual lookup in a log implementation, stopping at the first
matching write. Only a store extends the log. 

### `Instr.meteredAction`

 The private load uses the value and cost of the same linear scan. 

### `CallFrame`

 The frame gives the charged result of a stopping instruction or the one
continuation invocation and the event to prepend on return. 

### `CallFrame.ofAction`

 Resolve one instruction action using the remaining probe allowance and choice stream.
Produce either a stopping result or an event with its residual call state. 

### `CallFrame.result`

 Evaluate a call frame, prepending its event to the recursive run when the frame continues. 

### `LocalCharge`

 The interpreter controls reserve eight word operations per dispatch,
five stores per occupied probe, and four operations per guess bit. 

### `EventCharge`

 Interpreter work charged to one continuing event, with eight operations for dispatch, five
per probe and four per requested guess bit. 

### `Machine.meteredLoggedCall`

 Run a bounded private call using its write log and return both the local execution and its
work, charging each actual log scan in that execution. 
