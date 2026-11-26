---
{
  "module": "OAI/Computability/VPVNP/LiveStageSegments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageSegments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageSegments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A complete accepting stage inside the native linker

The segment before the accepting report keeps its stage tag and ordinary
persistent state. The accepting report transfers control, preserving all
source writes except for the linker's update to its own reserved word.


### `PreservesTag`

 Each source report preserves the linker's reserved tag address. 

### `PreservesTagOnReturns`

 At each continuing report, the next dispatch sees the same tag. The
accepting report may write the tag because it immediately halts or transfers. 

### `transferMemory`

 Memory passed across an accepting boundary. 

### `runSegment_accepting`

 Complete native simulation of one accepting component, including every
returned cursor, external word effect and the precise cumulative probe cost. 
