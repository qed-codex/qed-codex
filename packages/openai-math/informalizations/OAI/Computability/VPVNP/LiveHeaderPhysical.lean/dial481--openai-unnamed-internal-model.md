---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPhysical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPhysical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPhysical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed cut fields at their physical processor sites

The descriptor arithmetic addresses the same bits as the paper's typed
cut layout. In particular the exponent vector uses label-major order,
with the least significant bit first inside each label word.


### `ZeroSlice`

 The field runner tests exactly these bits for zero. 

### `unit_zero_iff`

 Unit mode accepts exactly the all-zero cut once its mode bit is checked. 

### `pair_padding_zero`

 The physical padding guard on a first-half cut is exactly the zero
padding constraint in the typed path equivalence. 
