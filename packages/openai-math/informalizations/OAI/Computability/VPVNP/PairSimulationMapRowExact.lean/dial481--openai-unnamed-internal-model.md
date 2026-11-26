---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapRowExact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowExact.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowExact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One decoded copy of a grouped motif in private RAM

The selected grid point, selector and party fix all widths, compared fields,
and row names. The variable input consists of the resident wire bits, their
base addresses and the running offsets. The program reads the fields, selects
the corresponding fixed parameter, and advances both demand and supply offsets.


### `endpoint`

 Source and target are separate positions even for loops. Absent positions
have an empty resident bit slice. 

### `group`

 The two ends of each group share its running offset. 

### `slices`

 A copy's complete endpoint slices, including demand padding and payload clipping. 

### `row`

 The tuple of base demand digits and base payload digits from this copy. 

### `digit_eq_key`

 The digits actually read by the native field scan give exactly the public-table key. 

### `offsetReg`

 A single cursor register per demand or supply group. 

### `groups`

 Advance groups in a fixed order, including groups with no endpoint at the party. 

### `nameFlow`

 Concrete table text chosen before the number of repetitions or the wire inputs. 

### `advanceFlow`

 Advance every demand and supply group's shared endpoint offset by the selected row's public
width. 

### `Sites`

 A fixed dispatch for the selected grid, selector and party. All links are between
individual instruction rows. The enclosing evaluator supplies its normal and bad exits. 

### `Sites.fields`

 Locations of the setup and padded-reader instructions used to assemble this row's
  endpoint digits. 

### `Sites.lookupPC`

 Program-counter placement for the flow that looks up a parameter name from the assembled
  endpoint digits. 

### `Sites.advancePC`

 Program-counter placement for the flow that advances the demand and supply offsets after
  lookup. 

### `Linked`

 The machine links the field reads, parameter lookup, and offset updates in order, directing
success to the supplied continuation and failure to the bad exit. 

### `cap`

 Worst-case cost of the path for this base copy. 

### `exists_uniform_cap`

 One bound serves all branches of the fixed block before choosing any inputs,
word width, repetitions, grid point, selector or party. 

### `exactSteps`

 The exact count uses the physical public bank and this copy's decoded row.
The field scan and the cursor advances take fixed time. The label lookup stops
as soon as its first matching row is found. 

### `native_exact`

 Reading one decoded copy computes its prescribed parameter ordinal and advances
the natural offsets of every group. The only private operations are deterministic ticks. 
