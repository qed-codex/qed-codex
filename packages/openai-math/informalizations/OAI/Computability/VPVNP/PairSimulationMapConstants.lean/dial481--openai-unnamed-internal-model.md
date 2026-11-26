---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapConstants.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapConstants.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapConstants.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Width-independent public constants of a fixed motif entry

A row compares actual endpoint digits with the natural coordinates of a
fixed basis tuple. The selector codes, ordinal names, base widths and row
coordinates form a finite table independent of the host word width. Casting
this single table gives exactly the public words of the descriptor-to-map
program at every fitting width.


### `selectorOrdinal`

 Selectors are numbered once for the fixed base motif. 

### `selectorWord`

 Encode each fixed selector's ordinal injectively in a machine word when the word space is
large enough for the selector table. 

### `halfDigit`

 Absent endpoints have value zero; the two directions have distinct keys. 

### `rawConstants`

 The physical public constants indexed by code ports, dispatch ordinals,
widths, endpoint comparison fields and the actual global parameter ordinal. 

### `words_eq_cast`

 These are the same words at every width supporting the base fields and
the selector numbering. The choice of ordinals does not depend on width. 

### `rawBank`

 The numerical public bank used when inlining the whole call template.
All enclosing positions outside the map allocation carry zero. 

### `installed_eq_cast`

 At every public port, including unused enclosing ports, the installed
word table is the cast of one natural array. 

### `widthThreshold`

 A fixed bit-width threshold, uniform across all parties and grid
points. It also accommodates the whole selector enumeration. 

### `eventually_width`

 The fixed threshold is eventually met by the live RAM word format. 

### `source`

 The source template of the public-bank lowering, using only natural
constants fixed before the host width and the private descriptor are chosen. 

### `source_run_framed`

 The raw constant bank runs the complete descriptor reader, port-directory
builder, selector decoder, row scan, width checks and histogram updates. 

### `source_run`

 The raw constant bank runs the complete descriptor reader, port-directory
builder, selector decoder, row scan, width checks and histogram updates. 
