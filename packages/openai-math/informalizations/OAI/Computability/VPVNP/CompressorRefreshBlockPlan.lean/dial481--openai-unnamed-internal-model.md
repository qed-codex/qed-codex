---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshBlockPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshBlockPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshBlockPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The degree-refresh phase list of a fixed compressor block

All phases share the same runtime input and allocation formulas. The
finite graph fixes each ROM pair and each local expander slot in the
program text. Six final scans copy the verified output columns to the
published incidence heads for the next level.


### `shape`

 Computes the refresh dimensions from the block schedule and template, including the tie
count, term-record stride and selector width. 

### `order`

 Numbers the ties between refresh ports in the order used by the block's motif worker. 

### `input`

 Reads the arena start, vertex and residual-lane counts, and old incidence heads from the
specified descriptor level. 

### `term`

 The motif worker pass for this template, using the block's tie ordering and one payload
entry per directed expander incidence. 

### `stage`

 Compiles a refresh stage to its worker visit with the corresponding cursor interval and
operand expressions. 

### `columnCount`

 Computes the copy length for a refreshed incidence column, counting base slots for columns
zero through two and actual slots for columns three through five. 

### `copyColumn`

 Copies one incidence column from the refresh allocation to its assigned column at the next
descriptor level. 

### `visits`

 The native refresh worker visits in execution order followed by the six incidence-column
copies. 

### `stage_params`

 The native worker bank is exactly the bank for which the refresh recipe
proves pointwise agreement with the semantic stage's operands. 
