---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterVirtualFuel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterVirtualFuel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterVirtualFuel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The auxiliary verifier's private clock as a width-only operand

At the paper's word widths the parser clock dominates the assembler's
address-scan clock. The exact clock used by the native coefficient counter
can therefore be computed inside a virtual leaf from its word width alone.


### `virtualFuel`

 Public operand computing the auxiliary coefficient verifier's instruction allowance as
twelve times the virtual word width plus 110. 
