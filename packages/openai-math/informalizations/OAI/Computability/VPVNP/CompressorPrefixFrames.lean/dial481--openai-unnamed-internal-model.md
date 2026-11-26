---
{
  "module": "OAI/Computability/VPVNP/CompressorPrefixFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPrefixFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPrefixFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Low-memory frames for arbitrary finite native prefixes

A partial successful execution may stop inside a pass with no accepting
extension. The frame invariant covers such prefixes directly. Once a
complete choice segment has been consumed, the same test continues in
its actual successor state and memory.


### `PrefixFrame`

 Low-memory stability of each branch and each successful prefix of the branch cut, including
prefixes ending before branch selection completes. 

### `deterministic_prefix`

 An arbitrary finite run either preserves all reserved low cells or
has already consumed the entire forced interval. 

### `Framed`

 The local frame proof required at each actual pass and terminal close. 

### `Framed.stable`

 Every finite successful prefix of the whole native execution preserves
the low bank, including prefixes on branches that cannot reach a leaf. 
