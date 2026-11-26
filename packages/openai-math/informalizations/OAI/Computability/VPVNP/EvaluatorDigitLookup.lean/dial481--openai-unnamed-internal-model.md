---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting a digit from a packed bit stack

The offset and width are unary. Two loops move the skipped and selected bits
onto a saved stack. The second loop also copies the selected bits. Reversing
the two temporary stacks restores the input and emits the digit in its
original bit order. The same finite control works for every table size.


### `Port`

 The source table, skip and width counters, and temporary and output stacks for extracting
one digit. 

### `ready`

 Initial lookup bank holding the table, unary offset and width, and incoming output stack,
with both reversal stacks empty. 

### `lookupRoutine`

 Select a bit interval, restore the table, and prepend the selected interval
to the digit stack. Malformed inputs that exhaust the source are rejected. 

### `lookupTicks`

 Instruction count for skipping the offset, extracting width bits, restoring the table and
prepending the digit to the output stack. 

### `lookupRoutine_runs`

 The returned table agrees bit-for-bit with the input. The two counters
and the two temporary stacks are empty after every successful lookup. 

### `lookupRoutine_space`

 A linear peak storage bound for all six stacks at every intermediate point. 
