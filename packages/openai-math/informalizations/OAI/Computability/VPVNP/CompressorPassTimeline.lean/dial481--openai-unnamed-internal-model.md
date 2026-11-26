---
{
  "module": "OAI/Computability/VPVNP/CompressorPassTimeline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPassTimeline.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPassTimeline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical pass intervals in the repeated block calendar

Each shrinking substep and degree refresh occupies its own window in the
fixed block script. Their absolute row intervals concatenate from the end
of the initial cursor setup through the exclusive calendar bound.


### `Pass`

 An elementary pass of the repeated block script, either a bounded shrink index or the final
refresh. 

### `Located`

 An occurrence of an elementary pass together with its zero-based block number. 

### `Located.block`

 Number of the block repetition containing this pass occurrence. 

### `Located.pass`

 Shrink or refresh pass executed at this occurrence in the block. 

### `Located.phase`

 Calendar phase label of the located pass, forgetting its block number. 

### `oneBlock`

 Pass occurrences within one specified block, listing all shrink indices before its refresh. 

### `timeline`

 Chronological pass occurrences across all block repetitions in the script. 

### `Located.visits`

 Concrete visits installed by this occurrence of the shrinking or refresh pass. 

### `Located.window`

 Contiguous script window occupied by the located pass's visits within its block. 

### `Located.first`

 Absolute directory ordinal of the first visit, accounting for initialization, preceding
blocks, and the within-block offset. 

### `Located.finish`

 First directory ordinal following the last visit of this pass occurrence. 

### `Located.calendar_row`

 Each row of the interval is the actual indexed visit in the script;
its calendar level is the block at which the occurrence was located. 

### `Consecutive`

 The listed pass windows meet consecutively and span exactly the supplied start and finish
ordinals. 

### `timeline_consecutive`

 The fold of successive half-open pass intervals, with the actual
calendar bound even when the block is never entered. 

### `execute_follows_timeline`

 The state-dependent mathematical execution follows this same list of
located visits on every sequence of terms. 
