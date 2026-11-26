---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native initialization of cursor incidence records

A call visits one actual outgoing port in site-major order. The two address blocks
are numbered by the ordinary binary values of the corresponding bits of the physical
address. The call advances the cursor and translates the appropriate block on port one.
It writes the inverse incidence at the computed destination. Parallel copies retain
their own slot numbers. Lanes over a common base arc repeat the same three base writes.


### `visit`

 Public words are the degree, cursor count, two binary radices, real arc width,
and the six column starts. The persistent word is the site-major outgoing port. 

### `Row`

 Values appearing in the six writes. 

### `Row.sourceBase`

 Outgoing port index at the source base vertex, before the residual lane is included. 

### `Row.targetBase`

 Incoming port index at the destination base vertex, used for the inverse base-incidence
  write. 

### `Row.displacement`

 The mask XORed into the residual lane when lifting this base arc to its actual
  destination. 

### `Row.targetActual`

 Destination port index after the cursor advance and lane translation, including the
  actual site's residual lane. 

### `Row.width`

 Number of payload bits carried by the outgoing port, with zero width for padding. 

### `wordRow`

 Decode one site-major outgoing port using word arithmetic and compute its base endpoints,
lane translation, actual destination and payload width. 

### `writes`

 Directly addressed outgoing and incoming columns, followed by the payload column
at each of the two granularities. 

### `events`

 The native trace for one outgoing port, with the arithmetic ticks and six writes populating
the base and actual incidence columns. 

### `visit_native`

 The same instruction table runs at every input length and visits every slot. 
