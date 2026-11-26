---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingCanonicalSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingCanonicalSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingCanonicalSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical packing specification from the produced assignment

All representation fields are proved from the natural assignment array,
the numeric scope plans, and the physical universal-type enumeration. The
width word is retained literally; only its length matters to the gather
program. No packing result or lookup correctness is an input.


### `input_eq`

 Concrete input data accepted by the existing packing program. 

### `input_eq_of_wordOrder`

 The saved alphabet can be identified using the actual assignment
frontend's word-order theorem. No permutation of the emitted bytes occurs. 

### `specWithWidth`

 Every `Spec` field is discharged from the actual input construction.
In particular the label records are derived, not assumed. 

### `spec`

 Convenience specialization when the width word is canonical unary. 
