---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFlatAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFlatAdd.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFlatAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming addition of serialized quartic coefficients

There are four calls to the actual modular-word machine. Width is supplied as
stack data. No instruction table is generated from a coefficient or its width.


### `addOne`

 One word from each flattened coefficient, followed by a real scalar add. 

### `marshalBits_eq_encode_constant`

 The physical scalar marshaler produces the exact flat constant code,
including when the scalar input is not a canonical residue. 

### `program_primitive`

 Primitive-machine refinement of addition of two flat four-word coefficients.
The finite program and its compilation overhead do not depend on p or mu. 
