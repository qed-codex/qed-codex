---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Accepting paths of a complete live evaluator group

The first call selects and publishes the action. The remaining calls each
check one cell and preserve that memory. Acceptance of the actual native
segment therefore fixes both the length of its branch stream and every entry
after the first. The memory on which the cell tests run is the memory obtained
by replaying the complete native report.


### `Finishes`

 The concrete interpreter halts on these branch lists and leaves the
specified external memory. 

### `scan_finishes`

 Starting in the cell scan, the only possible accepting stream consists
of one empty entry per remaining cell. This includes the empty suffix at halt. 

### `acceptedSegment_iff`

 Exact path and final-memory characterization for the actual group program.
The first choice list survives, including when two slots publish equal records. 

### `actualPathEquiv`

 A group path is determined by the first call's actual branch string.
All successful cell calls consume empty strings. 
