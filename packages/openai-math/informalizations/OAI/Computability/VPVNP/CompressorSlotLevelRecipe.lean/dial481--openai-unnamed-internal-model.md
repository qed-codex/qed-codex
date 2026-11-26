---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotLevelRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevelRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevelRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native row planners for the five shrinking slot passes

The template fixes the degree, consumed colors, tag count and subdivisions
for this substep. The planner reads the current base and residual lane counts,
the heads of the selected input tables, and the start of scratch space. It
computes each pass's exclusive stop and every address in its public bank.


### `Template`

 Constants in a shrinking substep's fixed finite instruction template. 

### `Template.tags`

 Fixed number of tags per base vertex used by this shrinking substep's planner. 

### `Template.oldDegree`

 Input slot degree compiled into the planner's old arc counts. 

### `Template.colors`

 Fixed number of old color-mask bits used to size the genuine candidate range. 

### `Template.subdivisions`

 Fixed subdivision count for each role edge type, used to size the candidate range and
  determine padding. 

### `Template.newDegree`

 Padded output degree compiled into the slot rows and base-matching phase. 

### `Template.shape`

 Combine the template constants with the current base and lane counts to obtain the slot
level shape. 

### `Inputs`

 Current level counts and physical heads. The role table contains the
eight entries materialized for the chosen layout. 

### `Inputs.bases`

 Planner expression yielding the current number of base vertices. 

### `Inputs.lanes`

 Planner expression yielding the number of residual lanes per packed base. 

### `Inputs.oldArc`

 Planner expression locating the selected old arc records with their role sites and CD
  flags. 

### `Inputs.role`

 Planner expression locating the chosen layout's eight endpoint role selectors. 

### `Inputs.subdivisions`

 Planner expression locating the published subdivision counts for the four edge types. 

### `Inputs.nextSite`

 Planner expression locating the cyclic site successor table used by dummy slots. 

### `Inputs.scratch`

 Planner expression yielding the first fresh address for the slot directory. 

### `Reads`

 The current expressions read the two shape scalars and the five array heads. 

### `Counts`

 Derived counts and array addresses used by the native passes. 

### `Counts.sites`

 Total number of packed sites including all residual lanes. 

### `Counts.pad`

 Number of dummy outgoing slots needed at each packed site to reach the target degree. 

### `Counts.oldBaseArcs`

 Number of old arc identifiers before adding the residual lane digit. 

### `Counts.genuineArcs`

 Size of the genuine candidate arc range across edge types, subdivisions, and residual
  lanes, including holes. 

### `Counts.genuine`

 Number of source and target fields in the genuine candidate range. 

### `Counts.dummy`

 Number of source and target fields in the dummy arc range. 

### `Counts.fields`

 Total number of field addresses covered by the owner and append scans. 

### `Counts.owners`

 Count of real site-and-side owners before allocating private rows for holes. 

### `Counts.baseArcs`

 Number of packed base ports for which the matching scan computes a target and
  displacement. 

### `Counts.rows`

 Starting address of the rectangular field rows following the append counters. 

### `Counts.inverse`

 Starting address of the inverse table that maps each real endpoint field to its
  rectangular slot. 

### `Counts.targets`

 Starting address of the matching target column indexed by packed base port. 

### `Counts.shifts`

 Starting address of the lane displacement column indexed by packed base port. 

### `Counts.stopAddress`

 First address after the slot directory's base displacement column. 

### `counts`

 Compile only the level-dependent arithmetic. Subtraction, division and
exponentiation inside template constants take place when building the fixed program. 

### `Counts.map`

 Apply the same conversion to every derived count and address, as when evaluating planner
expressions or encoding natural values as words. 

### `countValues`

 Calculate the natural-number slot counts and physical table addresses from the level shape
and input heads. 

### `stop`

 Planner expression for the selected slot worker's exclusive cursor bound. 

### `params`

 Public parameter expressions for the selected worker, in the order of its native parameter
bank. 

### `phase`

 Form the selected worker's descriptor recipe from its tag, zero starting cursor, stop
expression, and public parameters. 

### `recipe_words`

 Exact words of the compiled planner at the worker's own arity. 

### `stop_val`

 The cursor stop also equals the natural count when that count fits in one word. 

### `padded`

 Extend a slot phase recipe to the scheduler's common arity by appending zero parameter
words. 

### `pad_phase_words`

 Padding a native phase only appends zero words to its parameter row. 

### `padded_words`

 The enclosing catalog can use any larger row width. Extra words after the
worker's public bank are zero and have no effect on its operands. 

### `execute_padded`

 Launch the finite planner and install the computed row in the live
directory. Its reads, writes and private execution use the native compiler. 
