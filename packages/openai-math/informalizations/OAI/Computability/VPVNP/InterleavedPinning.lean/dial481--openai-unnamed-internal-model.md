---
{
  "module": "OAI/Computability/VPVNP/InterleavedPinning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/InterleavedPinning.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/InterleavedPinning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projections with interleaved fixed and free input bits

A deterministic input format may place prescribed bits among the bits that
carry weights. Fixing the prescribed coordinates retains exactly the paired
monomials indexed by fillings of the free coordinates.


### `fill`

 Fill the free positions of an input, preserving its prescribed bits. 

### `weighted_projection`

 The source index is fixed in advance. Only accepting counts on the specified
fillings enter the weighted predicate. 

### `recordLayout`

 A column record has a marker, one free bit, and its list of prescribed flags.
The machine scans these records from the right end of the physical input. 

### `recordLayout_fill`

 The physical input obtained by filling all column records. 

### `recordLayout_unique`

 Each free variable occurs exactly once even after reversal and padding. 
