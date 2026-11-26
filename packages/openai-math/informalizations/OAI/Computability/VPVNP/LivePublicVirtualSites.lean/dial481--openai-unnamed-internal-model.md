---
{
  "module": "OAI/Computability/VPVNP/LivePublicVirtualSites.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicVirtualSites.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicVirtualSites.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the virtual site count from the live address width

The least admissible virtual address width is the ceiling logarithm of the
probe budget minus the virtual bucket exponent. Adding the live address
width after taking the logarithm keeps the largest operand of the logarithm
at `n * clog₂ n`.


### `virtualSites`

 A fixed expression for the number of virtual sites in Sections 11 and 14. 

### `virtualSites_fits`

 The input, product, two logarithmic counters and both division operands
fit the same word as the resulting site count. 
