---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterDispatchSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatch within a site of the primed pair counter

Dividing the cursor offset by the span of a site gives the row and its local
cursor. The two comparisons then select a mark clear, root initialization,
or node visit. This calculation and the preparation of the parser operands
consume only ticks and preserve the two registers used to finish the call.


### `siteBranch`

 Selected parser routine for each position of a site. 

### `siteTicks`

 Five row instructions, one or two comparisons, and any operand preparation. 

### `siteRegs`

 The branch sees the clear index in register 2 or the row offset in register 5. 

### `site_pref`

 The local dispatch preserves and reflects successful traces, with the exact
tick count and the physical row and mark operands of the selected parser. 
