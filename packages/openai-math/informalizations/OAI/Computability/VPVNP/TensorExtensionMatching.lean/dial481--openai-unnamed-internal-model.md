---
{
  "module": "OAI/Computability/VPVNP/TensorExtensionMatching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorExtensionMatching.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorExtensionMatching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prescribing added tensor values while extending the entire old spectrum

For the two cases of Theorem 2.4, the finite set of required generators
consists of the added star or the two added wires. The generator family
also contains every nonzero old restriction class. Multiplication folds
the old factors into one class before the contraction estimates are used.


### `exists_extension_matching_of_rank`

 The contraction estimates for a finite family of added tensors imply
that one spectral point matches their prescribed values and extends the
original point on all old tensors. 
