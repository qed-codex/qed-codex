---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteProcessorPortsInjective.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteProcessorPortsInjective.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteProcessorPortsInjective.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Recovering call-loop port names from the shared processor bank 

### `origin`

 Partial inverse of the shared aliases. A `none` identifies a guard or public
stack lying outside the call loop's image. 

### `callPorts_injective`

 Every two distinct logical ports of a call occupy different physical stacks. 

### `callPorts_ne_cut_of_origin_none`

 Any public or guard register whose inverse entry is vacant survives an entire call. 
