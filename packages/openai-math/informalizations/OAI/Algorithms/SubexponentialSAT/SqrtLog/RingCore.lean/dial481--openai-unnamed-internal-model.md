---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrary-degree ternary unramified counting rings

This semantic model reuses the audited monic-lift construction. The extension
is not restricted to degree four. Its finite coefficient representation and
exact readback are exposed separately from any machine-cost refinement.


### `base`

 The base ring embeds as constant polynomials. 

### `coordinates`

 The exact finite power-basis coordinate representation. 

### `readBase`

 Read the constant coordinate; it is an exact left inverse on the base ring. 
