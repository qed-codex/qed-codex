---
{
  "module": "OAI/Computability/VPVNP/CompressorCalendarRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCalendarRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCalendarRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the online descriptor calendar's row count

A fixed burst-RAM program raises the input length to the numerator of the
compression rate and repeatedly divides by the radix determined by its
denominator. It writes the resulting affine row count at workspace offset
eight. Only this final instruction accesses external memory.


### `Spec`

 Parameters for the calendar's row count as an initial count plus a fixed number of rows per
complete block. 

### `Spec.p`

 Numerator of the ratio controlling the logarithmic number of complete compressor blocks. 

### `Spec.q`

 Denominator of the block-count ratio, used as the exponent in the repeated division by a
  power of two. 

### `Spec.initialRows`

 Number of directory rows occupied before the first repeated compressor block. 

### `Spec.phaseRows`

 Number of directory rows contributed by one complete compressor block. 

### `rows`

 Total chronological row count for an input length, including startup and all complete
repeated blocks. 

### `ticks`

 Private instructions through address calculation, including all loop tests. 

### `table`

 Registers zero and seven retain one and zero. Register two counts down the
multiplications. Register three holds the power and then the running quotient.
Register four counts divisions and subsequently holds the affine row count. 

### `report`

 The native report that computes the row count and writes it at offset eight of the
workspace. 

### `execute_native`

 For every sufficient instruction cap the native stage accepts on its
unique empty choice stream and writes the encoded row count. 

### `ticks_le`

 Each successful division consumes at least one binary digit. 

### `eventually_fits`

 With the paper's live word width, every integer used in a loop guard
and the full natural row count are representable for all sufficiently large lengths. 
