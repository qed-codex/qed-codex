---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitAction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing one label at one radix position

The cell control reads its binary counter from the packed table. At the
most-significant-first position `j` of exponent `eᵢ`, it executes the
label callback precisely `⌊eᵢ / Q^(Z-1-j)⌋ mod Q` times on every successful
path. The returned scheduler bank is ready for the next label.


### `cellRoutine`

 Both the lookup control and the decrement loop are fixed across all
rows, columns, field cardinalities, and input widths. 

### `cellBudget`

 A per-label clock independent of the two cursor positions. 

### `fetch_cell_runs`

 At any legal pair of cursor positions the deterministic lookup
prepares the exact radix digit for the countdown. 

### `cellRoutine_realizes`

 A callback preserves the scheduler registers on every normal return. Its
integer count can include any finite number of distinct outcomes, including
outcomes that share a successor state. 
