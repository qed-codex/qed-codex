---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sequencing input measurement, public parameters and field parsing

The raw input starts on one stack and all remaining stacks start empty. The
fixed length pass restores the input, the parameter pass computes the two
field widths, and the fixed parsing pass extracts the four data stacks.


### `withScratch`

 The input registers together with the parameter routine's scratch bank. 

### `measured`

 The complete physical tape has been measured and restored. 

### `startup`

 Measure and restore the raw input, prepare its field widths with the supplied routine, and
parse the site fields. 

### `startup_runs`

 The raw site tape is the only populated stack at entry. Once the public
parameter pass has run on its measured size, parsing incurs at most another
`5n+17` stack instructions. 
