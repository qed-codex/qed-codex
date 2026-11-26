---
{
  "module": "OAI/Computability/VPVNP/CursorBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Size of the routed network before compression

In §§11–12 of *VP and VNP differ over every field*, the virtual group uses the least
power-of-two site count that accommodates the pair parser's budget. One circuit of
cursor positions routes each message, with separate fields for each mask. These exact
choices give the position and maximum-width bounds needed in equation (12.1).


### `addressBits`

 The live processor address length in Section 9.1. 

### `processorCount`

 Live processors indexed by their binary addresses. 

### `virtualBits`

 The least binary virtual address length giving enough bucket slots. 

### `virtualCount_bound`

 Rounding the virtual processor count to a power of two costs at most a factor of two. 

### `addressBits_eq_ceil`

 The rounded binary logarithm and the paper's real-log convention agree at all lengths. 

### `virtualBits_le`

 At most two extra logarithmic terms in the virtual processor address length:
one for the word length `n`, one for its rounded binary logarithm. 

### `addressBits_le_virtualBits`

 At large lengths the virtual group retains at least the live number of address
bits. Thus reserving a fixed number of fresh lane bits per compressor block is possible. 

### `wordBits`

 The virtual word length is inherited from the live RAM. 

### `initialPositions`

 Count the actual processor-cursor positions in the graph of §12. 

### `initialWidth`

 Width of one directed cursor arc, reserving a disjoint payload for each mask system. 

### `initialPositions_bound`

 Pointwise initial-position bound with explicit logarithmic factors. 

### `initialWidth_bound`

 Pointwise initial arc-width bound with explicit logarithmic factors. 

### `initialBounds`

 The two pre-compression estimates of §12 hold simultaneously for fixed `B`. 
