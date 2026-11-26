---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkCurrentBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkCurrentBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkCurrentBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The common physical prefix at a shrinking boundary

All terms have identical header reports, so the current packed graph
starts one deterministic prefix before any term is read. The branch at
its endpoint accepts precisely the typed shrinking terms and runs the
selected score and geometry construction for each one.


### `origin`

 The shrinking pass occurrence at the given substep and input state. 

### `defaultTerm`

 The default selected term of this shrinking occurrence, used to describe the header shared
by every choice. 

### `beforeLevel`

 The selected level with the default term and an empty choice stream, used for the common
header before branching. 

### `selectorWord`

 The shrinking template's selector-bit count encoded at the host word width. 

### `Boundary`

 Data at the common selection boundary and the true execution on
every continuation. The level indices are relative to the given layout. 

### `Boundary.pre`

 The common shrinking prefix run from the post-header memory through the input and demand
  preparation before term selection. 

### `Common`

 The physical branch boundary for this packed shrinking level, specialized to the block's
scalar bounds, headers, scratch base and entry memory. 
