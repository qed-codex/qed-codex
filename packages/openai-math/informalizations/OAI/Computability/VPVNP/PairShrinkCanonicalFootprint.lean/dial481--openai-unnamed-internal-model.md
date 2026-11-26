---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCanonicalFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of the shrinking vertex interpreter

For each parent assignment, the canonical parser reads the physical resident
matrix rows in their stored order. Decoding the parent preserves the same
worker read domain and external memory for every successful visit.


### `canonicalFamily_support`

 Read and write footprints of a returned raw visit with its parent fixed. 

### `canonicalParent_worker`

 Every successful shrinking visit reads only the worker's cells and returns the
same external memory, before examining any future choice bits. 
