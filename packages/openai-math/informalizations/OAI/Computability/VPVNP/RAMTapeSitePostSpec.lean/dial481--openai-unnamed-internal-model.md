---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePostSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Correctness of the physical sort and boundary decisions

For the actual shared sorting fields the checked block determines the
terminal predecessor test. On a passing sorting transcript the physical
last-slot test therefore compares exactly the replayed block with the
edge records. A failed comparator contributes zero regardless of that block.

