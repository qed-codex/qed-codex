---
{
  "module": "OAI/Computability/VPVNP/LiveProgramSkeletonRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramSkeletonRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramSkeletonRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The linked runtime-skeleton sweep

The native table writes one nonblank tape symbol for every bit of the
zero-exponent runtime input. Its reports preserve both the linker tag and
the four runtime operands. The final linked call writes the scatter tag.


### `skeletonReports_outside`

 Every returned native report writes only inside the allocated runtime
interval. This also applies when replaying that report on another memory. 

### `skeletonBase`

 Base word address of the runtime skeleton's four operands, thirteen words past the advice
frame base. 

### `skeletonRun`

 On the actual linked skeleton row, the canonical runtime word is written
to the supplied tape base. At handoff the scatter tag is the only change
beyond these writes, including on the reference memory for untouched cells. 
