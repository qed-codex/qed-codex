---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackSignedScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackSignedScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackSignedScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Power-basis representation of a signed coefficient

A matrix coefficient supplied as the difference of two nonnegative counts
reduces to one prime-field limb. Storing that limb followed by zero padding
writes exactly the scalar used by the determinant stack.


### `packed_scale_one`

 The packed constant vector has exactly the bit prefix returned by the
fixed constant emitter. 

### `pack_signed_counts`

 Reducing the two counts modulo the advised prime, subtracting them and
packing the result in the low limb realizes integer casting into the scalar ring. 
