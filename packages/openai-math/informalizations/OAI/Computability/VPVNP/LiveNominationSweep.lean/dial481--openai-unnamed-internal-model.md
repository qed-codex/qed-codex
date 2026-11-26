---
{
  "module": "OAI/Computability/VPVNP/LiveNominationSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveNominationSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveNominationSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological RAM calls for the nominated histogram

The first-half groups in §14.1 guess one fixed-width word for each production
label. The persistent cursor runs in increasing label order. The calls consume
exactly the row-major binary encoding of the histogram and store its entries
in the contiguous array beginning at the public base address.


### `calls`

 One little-endian binary choice list per production label. 

### `flatten_calls`

 Flattening the interpreter's choices gives the canonical array encoding, a bijection
between histograms and binary tapes of length `T * b`. 

### `stored`

 Contents of the histogram area after the last component call. 

### `stored_at_val`

 Each stored counter has the nominated natural value, without truncation. 

### `stored_outside`

 The sweep touches only the designated array. 

### `sweep_native`

 Run all nominations with reset private registers at each call, preserving the external
memory and advancing the cursor. At `T = 2^w` the final word is zero modulo `2^w`. 

### `SweepPaths`

 Native paths of the nomination phase, with one call per production label. 

### `sweepEquiv`

 Every binary path of the required number of calls is the unique encoding of a histogram. 
