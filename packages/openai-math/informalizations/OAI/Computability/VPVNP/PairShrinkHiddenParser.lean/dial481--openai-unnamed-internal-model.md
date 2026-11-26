---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenParser.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenParser.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenParser.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The private hidden rows consumed by the selected shrinking kernel

At each site the hidden rows occur in the order of the native directory.
Their concatenated bit fields are the entire branch string consumed by the
kernel. The subsequent resident matrix checks contribute no choice bits.


### `rows`

 Dense identifiers and little-endian bit fields in the site's scan order. 

### `mem_rows`

 The row for every absorbed edge at this site occurs in the scan. 

### `kernel_encode`

 Exact word-for-word agreement with the kernel of the scheduled pass. 
