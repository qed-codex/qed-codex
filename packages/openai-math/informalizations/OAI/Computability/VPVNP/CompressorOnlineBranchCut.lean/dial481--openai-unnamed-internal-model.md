---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineBranchCut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineBranchCut.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineBranchCut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native branch cuts of the fixed online descriptor table

The data bursts of a term row occur between three empty entering control
calls and one empty returning call. Every valid source tape selects a term,
and all terms use the same number of motifs. These facts distinguish the
terms even in the presence of arbitrary later native calls. The ordinary
descriptor rows are executed from the memory produced by each preceding row.


### `ControlBounds`

 All non-data instruction bounds are fixed by the finite program. 

### `oneRow`

 The actual online portion for a single valid source row. 

### `Interval`

 A finite interval of valid native rows, ending at a calendar boundary.
The ending ordinal may still have further phases to execute. 

### `intervalBits`

 Concatenate the choice tapes of the successive rows in an online interval. 

### `intervalLog`

 Replay the interval's row reports in chronological order using the memory produced by each
preceding row. 

### `intervalSegment`

 Physical segment witnessing a valid interval of online rows with its original choice tapes
and report log. 

### `quietInterval`

 The entire native interval, including each row's control calls, uses
empty tapes whenever every scheduled source burst does. 

### `selectorCut`

 Invert a term row, using its actual one-call worker invariant and the
source selector's completeness on valid recovered rows. 
