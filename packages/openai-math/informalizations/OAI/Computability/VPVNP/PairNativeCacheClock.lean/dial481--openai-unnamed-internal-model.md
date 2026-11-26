---
{
  "module": "OAI/Computability/VPVNP/PairNativeCacheClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clock for the native operand-cache initialization

The arithmetic prelude and all 38 store/increment pairs together use at most
one input length in native ticks at every sufficiently large length. The
threshold is uniform in the live bucket size.

