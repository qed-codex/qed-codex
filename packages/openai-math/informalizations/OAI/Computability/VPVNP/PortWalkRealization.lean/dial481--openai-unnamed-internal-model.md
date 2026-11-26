---
{
  "module": "OAI/Computability/VPVNP/PortWalkRealization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortWalkRealization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PortWalkRealization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Realizing a lazy Cesàro walk by a matching

Section 5.3 of *VP and VNP differ over every field* takes one matching step
at a uniform port to implement the averaged old walk exactly. Combining
integer walk counts with port reversal gives the transition matrix itself.


### `exists_cesaroPortMatching`

 One involution implements the mixture of the first `t` positive powers
of the lazy walk of a symmetric regular graph. Self-transitions use fixed ports. 
