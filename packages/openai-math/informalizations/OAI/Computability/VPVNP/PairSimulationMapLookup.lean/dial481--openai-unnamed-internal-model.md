---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapLookup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapLookup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapLookup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native fixed-table lookups for motif maps

The code compares the supplied fields with fixed public words. On the first
matching row it loads the corresponding selector or label ordinal. Reaching
the end of the table transfers control to the rejecting instruction.


### `Tree`

 A finite decision tree with public constants at the comparison nodes. 

### `eval`

 One native dispatch loads an output or goes to the bad exit. Each
comparison takes one public-word load and one conditional jump. 

### `flow`

 Lower the decision tree to the same structured finite table compiler
used by the coefficient machine. 

### `native`

 Success leaves the ordinal in the output register at the normal exit.
A miss reaches the rejecting exit. Each path consumes exactly its computed
number of ticks, without a probe or binary choice. 

### `row`

 Comparing a row stops at the first differing field. 

### `table`

 Compile a finite table in its given order, permitting partial tables. 

### `table_eval`

 The path returns the first matching row and performs at most two tests
per row field plus the final dispatch. 

### `publicData`

 Public ports can be allocated from the fixed rows and fields alone. 

### `Runs`

 A pathwise step cap, actual normal or bad exit, and the complete
private-memory frame available at that exit. 

### `reject_after_ticks`

 A deterministic tick prefix ending in the rejecting instruction rejects
with every fuel budget, including one that expires inside the prefix. 

### `Runs.rejects`

 A missing key rejects on every continuation budget and branch tape. 

### `native_table`

 The actual instructions read the given public key words. In particular
a short path on an early match satisfies the same cap as the longest path. 

### `tableFlow`

 Allocate the public ports once and compile an ordinary finite program.
Its opcode table and register numbering are independent of the word width. 

### `compiled_table`

 The compiler provides a concrete instruction table with all constants
installed. A caller can enter with arbitrary private memory and input
registers. The common exit returns the ordinal and the bad exit rejects. 

### `widen`

 Widen a fixed base-motif field to one machine register without truncation. 

### `native_selector`

 Compare the anchor word against the fixed selector codes. The first
matching selector returns its recorded ordinal. An unused code reaches
the rejecting exit in at most twice the table length plus one tick. 

### `halfKey`

 Absent endpoints contribute zero to the fixed tuple of compared words.
The two ends of a loop have distinct positions. 

### `LabelRow`

 Exactly the two input tuples in the fixed label lookup of the motif evaluator. 

### `labelRows`

 The fixed matrix has one row for each pair of local coordinates. 

### `LabelField`

 An endpoint field used in matrix-row lookup. The sum distinguishes demand from supply
edges, and the Boolean selects the source or target endpoint. 

### `labelFields`

 All endpoints can be numbered once for a fixed base motif. 

### `label_step_cap`

 The same bound holds at all grid points, selectors and parties of the
fixed motif, before choosing the widths or the number of outer copies. 

### `labelKey`

 Every demand and supply coordinate is represented by its widened natural digit. 

### `native_label_exact`

 Scan the complete fixed local matrix. The query registers hold the
decoded fields of one copy, in their own endpoint positions. A successful
scan emits precisely the ordinal of the parameter in equation (6.2). 

### `native_label`

 The complete local matrix lookup also satisfies its uniform table cap. 
