---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One finite-window evaluator transition in a live group

Each output cell reads a single offset from the previous window. Two
additional blank checks, immediately outside the new window, detect any
loss of nonblank tape data. Halts carry the unique canonical state code.
One choice bit selects a table slot, so equal instructions in a branching
row remain distinguishable.


### `updatedCell`

 Symbol at signed displacement `j` after writing at the old head and moving. 

### `boundaryBlank`

 The only two exterior positions which can receive a nonblank cell. 

### `updatedWindow`

 The finite head-relative tape window resulting from the proposed head write and movement. 

### `advanceCode`

 Check a selected instruction. The two boundary reads are necessary only
when its target is running, since the representation discards both tapes on a halt. 

### `row`

 Read the fixed row table at the state and the two current symbols. 

### `nextCode`

 Advance a cut code using one row-selection bit, handling carried halts, missing slots, and
the finite-window transition check. 

### `advanceCode_iff`

 A transition emits precisely the bounded representation of the true
successor. If it clips a tape, no outgoing code passes the transition test. 
