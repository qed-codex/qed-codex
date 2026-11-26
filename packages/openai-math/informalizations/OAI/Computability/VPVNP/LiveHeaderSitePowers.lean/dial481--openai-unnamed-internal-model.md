---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderSitePowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSitePowers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSitePowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Powers of two in the live header operand bank

All addresses and scan limits in a header row combine the base address and
the five public lengths by addition and multiplication. Thus each row, its
zero padding, and the appended stage tag preserve the site-power restriction.


### `operands_sitePowers`

 Every operand, including default words of short rows, preserves the
restriction on exponential operands inherited from the public layout. 
