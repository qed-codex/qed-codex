---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleSuffix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleSuffix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleSuffix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choice suffixes of shrinking visits

A successful visit consumes two adjacent fields: the independent arguments
of the placed children, followed by the owned absorbed words. Its deterministic
map scan decides acceptance on the resulting scratch and consumes no suffix.


### `visitReader_suffix_iff`

 Exact acceptance, factoring out the deterministic setup stages. The old
and hidden results determine the actual starting scratch for the map checks. 
