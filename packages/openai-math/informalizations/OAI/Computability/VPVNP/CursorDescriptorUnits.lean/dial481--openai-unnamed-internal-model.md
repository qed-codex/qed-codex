---
{
  "module": "OAI/Computability/VPVNP/CursorDescriptorUnits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorDescriptorUnits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorDescriptorUnits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Number of descriptor visits on the selected cursor branch

The units of the descriptor scans count the old sites, old slots and encoded
outer-term bits along the actual compressor execution. The number of blocks
and the binary length of every intermediate field are logarithmic in the
input length. Both logarithms enter the visit bound in Appendix E.


### `descriptorUnits`

 The actual number of old site visits, old slot visits, and selector bits
on a branch of the chosen iterated compressor. 

### `descriptorUnitConstant`

 Uniform constant multiplying the quadratic logarithmic visit bound. 

### `eventually_descriptorUnits`

 The threshold precedes all lane labelings, scalar specializations, and
outer term choices. Both site and slot scans count the old level's order. 
