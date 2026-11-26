---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native first-half stage completions at a common group clock

The dispatcher has a different length at each tag. Subtracting that length
from one group clock gives the source clock of the selected stage. The
continuation receives the actual transferred memory and the accumulated
report cap, including the dispatch and transfer probes.


### `Group`

 A live group with its fixed components, physical geometry and literal prefix, common call
clock, and bounds ensuring that stage tags and dispatch fit. 

### `Group.constants`

 Fixed parameters for the grammar, motif labels, header capacities, and evaluator windows. 

### `Group.evaluator`

 The universal evaluator program used in the group’s component table and stage
  transitions. 

### `Group.pair`

 The pair instruction table mounted at the group’s pair stage. 

### `Group.g`

 Physical input length, address width, bucket capacity, and RAM word width for the group. 

### `Group.lit`

 Literal prefix whose packed value and length can supply public operands. 

### `Group.clock`

 Common fuel allowance for a linked group call, including outer dispatch. 

### `w`

 RAM word width of this group’s physical geometry. 

### `components`

 Component rows assembled from the fixed constants, evaluator program, and pair table. 

### `T`

 Linked private instruction template containing all of the group’s component rows. 

### `pub`

 Public operand words of the linked table, obtained from the geometry and actual literal
prefix. 

### `addr`

 The group’s dispatch-tag address encoded as a RAM word. 

### `nextStage`

 Successor-stage function for the group’s evaluator program. 

### `P`

 Outer dispatcher program with the linked components, successor stages, public operands, and
actual tag address. 

### `clockAt`

 Fuel left for a source-stage call after charging the dispatch events for its selected tag. 

### `StagePaths`

 Complete ordinary source histories starting in state zero at the supplied memory, with the
selected stage’s residual fuel and linked-report room checks. 

### `tagged`

 The memory at the group’s tag address contains the word encoding the selected stage. 

### `program_eq`

 The program with flattened, stage-relocated operands is the physical group program. 

### `Entry`

 Entry certificate for a tagged stage. Its invariant holds at state zero and supplies the
tag-preservation condition for the stage’s returns. 

### `Entry.inv`

 Invariant on the returned state word and memory used to establish the stage’s tag frame. 

### `Indexed`

 The ordinary stage traces indexed by their mathematical choices. 

### `Indexed.traces`

 Bijection between the chosen indices and complete ordinary source histories of the stage. 

### `logs`

 Map the indexed history’s ordinary reports to their linked reports, including outer
dispatch and stage transfer. 

### `memory`

 Memory after the indexed history’s source events and transfer to its successor stage. 

### `tagged_memory`

 The transferred tag of an ordinary stage is visible on entry to its successor. 

### `continuationEquiv`

 A completed component indexed by its own branch data, followed by an
arbitrary native continuation at the same outer clock. 
