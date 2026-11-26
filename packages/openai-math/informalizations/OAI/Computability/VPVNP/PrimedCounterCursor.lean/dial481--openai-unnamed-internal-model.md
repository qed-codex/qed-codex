---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterCursor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCursor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterCursor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Absolute cursors of the pair counter

The machine makes one call for each cell in each input pass. It then visits
each site in row-major order, clearing its marks, initializing its root and
processing one node per call. The final calls compare all histogram entries.


### `span`

 A site occupies one call per clear, one root call, and one call per node. 

### `compareStart`

 Start of the histogram comparisons. 

### `calls`

 Total number of calls. 

### `LocalItem`

 The three types of call within one site's parse block, indexed by mark position, root
initialization or node number. 

### `Item`

 All calls in the pair schedule, partitioned into input assembly, per-site parser operations
and final label comparisons. 

### `localIndex`

 Number the calls within a site by listing its mark clears first, then its root
initialization and node visits. 

### `index`

 All independent slots of the binary branch tape, in chronological order. 

### `unpack_site`

 Word division and remainder in the site phase recover both the physical
row and its local phase. 

### `calls_pair`

 For the paper's `2R` sites, each has exactly `2n−1` nodes. 
