---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotScheduledRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotScheduledRuns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotScheduledRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Source runs of the shrinking slot program

The slot builder's reports follow the same sequence of workers as the
descriptor planner. The first sixteen phases prepare and fill the physical
directory. The last six copy it into the next level's canonical arrays.
Each worker starts at zero in the actual memory left by the preceding phase.


### `Plan`

 The operands compiled into this occurrence of the slot plan. 

### `Plan.template`

 Fixed slot geometry and role subdivision counts for this scheduled shrinking step. 

### `Plan.input`

 Expressions locating the dynamic dimensions and working tables of the slot builder. 

### `Plan.layout`

 Expression reading the layout side selected by the shrink score. 

### `Plan.split`

 Expression locating the surviving-width table used to fill the output slot widths. 

### `Plan.space`

 Descriptor shape used to locate the next level's canonical incidence pointers. 

### `Plan.step`

 Substep number used to locate the level receiving the six completed columns. 

### `Stage`

 A scheduled slot-builder stage for publishing subdivision data, preparing lookups, building
the directory or copying one incidence column. 

### `Stage.visit`

 Compile a slot-builder stage into the corresponding planned worker visit and operands. 

### `preparationOrder`

 Publish four subdivision counts, prepare the role and cyclic-site lookups, then clear the
append counters. 

### `directoryOrder`

 The five sorted-slot core phases followed by base inverse, actual outgoing, actual incoming
and width publication. 

### `constructionOrder`

 The preparation and directory phases in the order that builds all six output columns. 

### `order`

 The complete shrinking slot schedule, ending with the six copies into the next level's
canonical arrays. 

### `order_visits`

 The stage enumeration uses exactly the same chronological visits as the
native block planner, including its six per-column destinations. 

### `Stage.limit`

 Exclusive worker cursor for each stage, using its actual site, owner, field or
incidence-column count. 

### `Stage.arity`

 Number of public operand words expected by the worker for this scheduled stage. 

### `Stage.bank`

 Instantiate the stage's physical operands from the slot shape and table heads, chosen
layout, split widths and destination directory. 

### `Stage.words`

 Expression evaluation at the planner cursor supplies the exact bank and
exclusive stop used by the physical worker. 

### `Source`

 The visit's straight-line program has one unreachable reject instruction.
All preceding instructions, including the return, form its checked fuel bound. 

### `construction_sources`

 Extraction of the original reports of all sixteen construction phases,
with the physical banks and fresh cursors of their compiled workers. 

### `copy_sources`

 Copy the completed columns using their actual base or lane-slot row count. 

### `sources`

 The twenty-two-stage source walk retains every report in construction
and copying. The destination represents the selected next state at the end. 
