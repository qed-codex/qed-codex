---
{
  "module": "OAI/Computability/VPVNP/CompressorHeaderOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorHeaderOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorHeaderOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Planner reads for the initial and substep header visits

The first-header formula reads the row count. Level offsets read the pitch.
Only the cursor planner loads additional words, namely its six scalar inputs
in the permanent first-level frame. These facts apply to each reference
memory at which the corresponding visit is prepared.


### `Supported`

 The start, stop, and parameter expressions of a visit read only addresses allowed by the
specified region. 

### `initial`

 Covers the concrete four visits in their true order, including the
level-zero role word at offset 27. 

### `substep`

 At any substep the two scalar publishers need only the runtime pitch.
The pointer publisher also reads the row count to locate the first level. 
