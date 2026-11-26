---
{
  "module": "OAI/Computability/VPVNP/CursorStateCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorStateCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorStateCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Expanded RAM path counts in compressor coordinates

In (12.2) the compressor starts with the regular cursor network, represented
as base vertices and lanes. Relabelling its original local choices preserves
each accepting path of each validator, including when later substitutions
give it half-wire arguments that disagree across an original edge.


### `expandedRAMStateCount`

 Equation (12.2) for a finite history on the dyadic-degree compressor
state. The original local choices are the validator's individual private
strings and the empty transit choices, transported through the site, edge
and bit-alphabet bijections. 
