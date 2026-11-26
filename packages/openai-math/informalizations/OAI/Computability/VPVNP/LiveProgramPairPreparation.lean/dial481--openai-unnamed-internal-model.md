---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The concrete native preparation of every first-half pair

Starting with the recovered live header, the nominated production words
stay in the live counter array. The initializer builds the descriptors and
the copy stage prepares every auxiliary header address in the shadow.
Unused shadow words have zero default. Header words below the descriptor
table and counters below the shadow are preserved.


### `histogram`

 The packed histogram installed at the auxiliary machine's header addresses. 

### `PreparedBranch`

 Certificate of auxiliary initialization and copying after a particular nomination,
including exact shadow contents, preserved header and counters, and bounds on native
reports and probes. 

### `PreparedBranch.init`

 Unit-indexed initializer starting from the memory reached by the chosen nomination. 

### `PreparedBranch.copy`

 Unit-indexed sparse copy starting from the initializer’s final memory. 

### `prepare`

 All required stage classifications before the compressed pair, with the
correct memories and linked report costs. 
