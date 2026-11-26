---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PairPreparationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairPreparationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairPreparationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing all selected pair plans once per assignment step

The fixed program preserves the full seed-index records, original pair
records, seed count, and processed counter. It computes the next cutoff,
builds each pair's actual selection table, and emits selected pair records.
The candidate value is not an input to this preparation phase.


### `selectorStacks`

 Stack 7 holds the cutoff throughout the pair loop and is excluded. 

### `callback`

 Each operation below is a fixed instruction table or a fixed finite
composition. In particular, the selection table is actually generated. 

### `command`

 Inputs: 30 seed-index records, 31 raw pair records, 32 unary seed count,
33 unary processed count. Output: 29 selected pair records in input order.
Every source is copied before it is scanned or changed. 

### `inputState`

 Only the four immutable inputs are populated initially. In particular,
processed bits are arbitrary; their length is the logical processed count. 

### `traceBound`

 This bound sums the costs of the actual called instruction tables and
record scans. It is not an assumed bound on an abstract preparation function. 

### `callback_eval`

 One actual pair-preparation call. Its effect is one framed selected pair
prepended to the existing output list, with the loop and source state framed. 

### `loop_eval`

 The outer scan is the actual framed-record loop. It invokes the proved
pair preparation exactly once per raw pair. 

### `program_runsIn`

 Full halted execution of the concrete once-per-step preparation routine.
No selected-plan table is supplied to the machine as a precomputed input. 
