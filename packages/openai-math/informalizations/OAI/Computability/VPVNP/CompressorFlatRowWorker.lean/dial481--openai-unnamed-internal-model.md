---
{
  "module": "OAI/Computability/VPVNP/CompressorFlatRowWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFlatRowWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed whole-level worker for repeated local descriptor calls

The original worker runs with the computed public operands and local cursor.
A successful return advances the global row cursor, while choice streams,
external effects and rejection agree with the original body.


### `PCs`

 Number of program counters for the prologue, original body, and final return instruction. 

### `bodyPC`

 Relocate an original body program counter past the operand-loading prologue. 

### `prePC`

 Map a prologue counter into the flattened program, transferring to the original entry when
the prologue finishes. 

### `compile`

 The whole-level template. The operand array is indexed by (local public
parameter or local cursor, base/stride/bias). 

### `result`

 Preserve the body's events and rejection, and replace a successful return by the next
global row cursor. 

### `execute_flat`

 A successful local call contributes exactly its original events after the
operand prologue. Rejection and its accepted branch stream are preserved. 
