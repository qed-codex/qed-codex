---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMPrepareImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMPrepareImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMPrepareImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The scheduled preparing call on configuration images

The first call reads the old state and the two head symbols and consults the
fixed evaluator's row. The selected five words must match the proposed state
and are published to disjoint scratch memory. The choice stream distinguishes
the slots even if they specify identical instructions.


### `PrepLayout`

 The allocation supplies enough bits for every program row, both
configurations, and the separate five-word scratch area. 

### `Prepared`

 A native run from cursor zero, indexed by its final memory and consumed bits. 

### `preparedMemory`

 Memory obtained by publishing the selected record of this source. 

### `prepared_iff`

 Execution at cursor zero is equivalent to picking an occupied slot with
a nonrejecting target equal to the proposed state. Both the consumed bits and
the resulting external memory are specified. 

### `preparedMemory_images`

 Publication preserves the two configuration images and installs the five
chosen instruction words at the address subsequently used by the cell scans. 
