---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Runs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Match/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Matching by source and occurrence rank 

### `sorted`

 Only contiguity of the relevant runs matters, not the order of the runs. 

### `item_span`

 A fixed window suffices to check all occurrences of the thin item. 

 # Counting eligible rows by source 

### `eligible_count`

 Within each source the eligible thin rows are in bijection with
the ranks attained by both thin and thick rows. 

 # A local array encoding the outgoing units of a single source tag 

### `Represents`

 Tags need only distinguish items and destinations within the colony.
Other source tags may use the same array. 

 # Whole-item matching by an ordered list of friends 

### `earlier`

 Within each thin source run, the eligible positions form a prefix,
and their friends occur in order in the thick source run. 

 # Transferring the array matching bound to one source colony 


# Occurrence ranks by stable sorting and pointer doubling

In sorted order, each position points to its predecessor with the same
key, or to itself at a boundary. After doubling `h` times all pointers
give the start of their run.


### `order`

 Stably sort all keys. 
