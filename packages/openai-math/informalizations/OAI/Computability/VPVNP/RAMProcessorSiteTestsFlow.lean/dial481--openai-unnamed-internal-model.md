---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteTestsFlow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsFlow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsFlow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed exits of the site checks

The graph consumes the verdict stack before transferring to the selected
caller label. The caller receives all original site data and empty scratch.


### `Tree.fragment`

 Compile the site's decision tree into a graph fragment that consumes its verdict bits and
jumps to the caller's reject, finish or dispatch label. 
