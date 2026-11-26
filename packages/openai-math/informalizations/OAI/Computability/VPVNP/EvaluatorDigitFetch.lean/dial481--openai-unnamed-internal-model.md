---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitFetch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitFetch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitFetch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fetching a packed digit during the column and label loops

The scheduler stores both forward indices on tally stacks. Each fetch computes
the bit address, reads the selected cell, and restores the table. Only the
digit stack changes across the whole call.


### `Port`

 The scheduler owns the address counters, packed table, and digit scratch
stacks. The callback's own registers occupy the `work` ports. 

### `bank`

 Between matrix queries all lookup and decrement scratch is empty. 

### `fetch`

 Compute the row-major bit address and read one digit without consuming
the packed table or any of the scheduler's loop indices. 

### `fetchTicks`

 Instruction count for computing a packed digit's bit address and then reading that cell
while restoring the table. 

### `fetchTicks_le_cells`

 A uniform fetch bound works across the full pair of loops. 

### `fetch_space`

 Every intermediate stack of a fetch grows by at most a linear function
of the table dimensions, even with arbitrary callback registers in the bank. 
