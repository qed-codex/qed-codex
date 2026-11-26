---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Producing the cursor initializer's parameter frame

The virtual-parameter program leaves the site exponent, bucket capacity and
live address width in registers. A fixed suffix splits the exponent, computes
the RAM arc width, and writes the eight words consumed by the scheduler-row
initializer. It uses the integer identity
`width = D * w * (8 + 10 * (D + 1) * H)` for the two mask systems.


### `finish`

 Slots are the input length, live address bits, degree exponent, lane
bits, scheduler row address, worker tag, array start and destination frame. 

### `program`

 Run the virtual-parameter calculation, then split the site exponent and write the cursor
scheduler's eight parameter words. 

### `events`

 The local calculation ticks followed by the eight parameter-frame writes at the supplied
base address. 

### `arc_width`

 The triangular layer count cancels the factor two in each pair of sort blocks. 

### `native`

 At normal call entry the virtual program and the parameter suffix compute
the eight scheduler inputs using one deterministic burst. 

### `frame_ready`

 Readback through the real frame loader. Every address outside these eight
cells retains its original word. 

### `initialize_from_frame`

 The next burst loads the generated frame, runs the existing row initializer
and returns the incremented state. Its memory has the exact loop bound and
all eleven cursor-worker parameters, and the framed call costs 22 probes. 

### `PrefixCorrect`

 Two successive native bursts, with their actual external memory transfer
and the fields of the installed cursor scheduler row. 

### `scheduler_prefix`

 The parameter prefix starts from the live length and address-width words.
Its two bursts make thirty external probes and use logarithmically many steps. 
