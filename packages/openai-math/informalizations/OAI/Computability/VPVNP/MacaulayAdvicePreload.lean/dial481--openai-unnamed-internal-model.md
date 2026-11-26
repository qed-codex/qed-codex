---
{
  "module": "OAI/Computability/VPVNP/MacaulayAdvicePreload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayAdvicePreload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayAdvicePreload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Capacity of the actual coefficient-reader advice banks

The checker serialization and the selected mask and extension-field values
are present in full. Both banks use finite port types. Each immutable stack
fits the common live-space budget used by the row phases.


### `pin_preload_length`

 Immutable pin mask, scalar table, width markers and arithmetic advice. 

### `CoefficientPort`

 Disjoint ports for the signed equation-coefficient reader and the affine pin mask and value
reader. 

### `coefficientAdvice`

 The checker words and affine advice occupy disjoint physical banks. 

### `coefficientAdvice_preload`

 The same prime-independent bound covers all immutable coefficient slots
and the constant zero and one field encodings. 
