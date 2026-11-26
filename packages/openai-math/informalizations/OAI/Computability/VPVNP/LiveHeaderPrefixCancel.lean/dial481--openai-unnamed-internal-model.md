---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrefixCancel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefixCancel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefixCancel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic prefixes of accepting RAM paths

An empty-choice prefix ending at a persistent state fixes its reports and
memory effects in any accepting execution from the same initial state.
The remaining branch inputs execute from the resulting physical memory.


### `no_accept_after_empty_prefix`

 A rejected call immediately after such a prefix excludes every
accepting branch path, even if that path uses different choice lists. 
