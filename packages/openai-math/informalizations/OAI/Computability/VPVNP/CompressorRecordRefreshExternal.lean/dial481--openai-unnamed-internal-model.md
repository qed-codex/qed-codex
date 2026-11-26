---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshExternal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshExternal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshExternal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External segment arrays on the actual dyadic refresh graph

Starting with the old widths and the translated bundle directory in memory, the native
pass constructs both ends of every external segment. Its row count is the old degree times
the position count. Its offsets agree with the concatenation used by the kernel even when
widths vary arbitrarily between lanes of the same bundle.


### `DyadicArc`

 A numbered external segment of a dyadic refresh, indexed by its base vertex, lane, bundle
port, and segment port. 

### `idWord`

 The numerical source identifier used as the persistent scan cursor. 

### `bundleWord`

 The bundle identifier used in the target, shift and running-total arrays. 

### `Directory`

 Contents required in the old width table and in the two fixed-width columns of the
directory. The initial values at unused addresses are immaterial. 

### `graphInput`

 Decode each numbered row directly to the old width, destination bundle or port shift.
Blank padding past the three table extents is assigned zero. 

### `graphInput_directory`

 The explicitly decoded table gives a valid directory with room for each concatenation. 

### `bundleWord_live`

 Each bundle number names a reachable directory row. Its source segment at port zero
is an actual cursor value in the pass. 

### `prefixTotal_eq`

 A bundle accumulator sums exactly its own previously visited source ports. 

### `prefixTotal_offset`

 The running total at the source segment number equals the exact kernel offset. 

### `directory_legal`

 For the actual graph the translated rows are injective. The only numerical width
requirement is that the full concatenation of each bundle fits in a word. 

### `external_pass`

 The complete native external pass writes the source and destination records of every
actual old arc, at cost nine per segment including call boundaries. 
