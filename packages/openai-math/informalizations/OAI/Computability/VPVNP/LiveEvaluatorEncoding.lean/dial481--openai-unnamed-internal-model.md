---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite configurations on a live evaluator cut

The two-way tapes in `UniversalMachine.Config` use head-relative coordinates.
The field for each tape on a cut records its cells at offsets `-M,…,M`, with
the head at position `M`. Cells outside the field are blank. A running state
carries both fields. Acceptance and rejection each have a single representation,
independent of the tape contents at the halt.


### `TapeWindow`

 A finite field of cells, with its head at index `M`. 

### `TapeWindow.cells`

 The symbols at offsets from minus the radius through plus the radius, with the head in
  the central cell. 

### `TapeFits`

 Every cell outside the indicated head-relative interval is blank. 

### `TapeWindow.ofTape`

 Read a head-relative window of the specified radius from a two-way tape. 

### `TapeWindow.toTape`

 Extend the array on both sides by blanks. Each half tape begins
at the cell nearest the head. 

### `TapeWindow.read`

 The window indexed by the signed displacement from its head. 

### `tape_ext`

 Extensionality in signed head-relative coordinates. 

### `ConfigWindow`

 The bounded data of one running evaluator. 

### `ConfigWindow.state`

 The finite control state stored alongside the two tape windows. 

### `ConfigWindow.firstTape`

 The first tape's symbols in the finite window around its head. 

### `ConfigWindow.secondTape`

 The second tape's symbols in the finite window around its head. 

### `ConfigWindow.toConfig`

 Recover a machine configuration by extending both stored windows with blank symbols outside
their bounds. 

### `ConfigWindow.ofConfig`

 Record the control state and the two radius-bounded tape windows of a machine
configuration. 

### `ConfigFits`

 Both tapes of the configuration are blank outside the specified radius of their heads. 

### `Code`

 A live cut has a unique code for either kind of halt. 

### `Code.toState`

 Interpret a finite cut code as an evaluator state, preserving its halt status or
reconstructing its running configuration. 

### `StateFits`

 Canonical bounded states use the two halting constructors exclusively
and retain the complete finite-support tapes in every running state. 

### `Code.ofState`

 Encode a fitting evaluator state on a cut, using canonical halt codes and bounded windows
for a running state. 

### `codeEquiv`

 Forgetting the serialization data identifies precisely the canonical
bounded states, including early halts and a zero-radius window. 

### `fieldWords`

 One state word and two consecutive fixed-width tape fields. 

### `stateField`

 The control-state field at word zero of the serialized configuration. 

### `firstField`

 The serialized word position of a first-tape cell, immediately following the control state. 

### `secondField`

 The serialized word position of a second-tape cell, following the control state and all
first-tape cells. 

### `Code.stateWord`

 The control field is the machine's own state number. 

### `Code.firstCell`

 Read a first-tape symbol from a cut code, using blank for either canonical halt. 

### `Code.secondCell`

 Read a second-tape symbol from a cut code, using blank for either canonical halt. 

### `words`

 Store the state, then the first tape and the second tape in increasing
cell order. The halt codes zero every tape field. 

### `format`

 The checked binary decoder requires canonical symbols and zeroes at every
unused position. There are exactly `fieldWords M * w` bits on the field. 

### `stateBitsEquiv`

 Bounded evaluator configurations, including the two canonical halts,
are in bijection with all valid bit strings of the allocated width. 
