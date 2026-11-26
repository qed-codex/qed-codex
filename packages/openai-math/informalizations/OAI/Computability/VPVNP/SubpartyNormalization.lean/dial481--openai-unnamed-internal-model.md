---
{
  "module": "OAI/Computability/VPVNP/SubpartyNormalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SubpartyNormalization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SubpartyNormalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Normalizing a spectral point on fewer parties

Lemma 2.3 of *VP and VNP differ over every field* embeds tensors on the used
parties by trivial legs outside them. Raising the old values to the reciprocal
of the embedded diagonal exponent makes their direct sums additive and thus
defines a spectral point on the smaller set.


### `embeddedValue`

 The old value on trivial extensions descends to the restriction classes
on the smaller party set. 

### `subpartyExponent`

 Base-two logarithm of the value of the embedded two-dimensional diagonal. 

### `embeddedValue_natCast`

 The power law for local diagonal tensors on the used parties. 

### `subpartyNormalization`

 The smaller-party spectral point, with the local diagonal normalized to
dimension. Its evaluations include every tensor supported on the used parties. 

### `trivialExtension_wire`

 Keeping an old wire and adding trivial legs agrees with the same wire
between the included endpoints. 

### `wireDistance_le_subpartyExponent`

 Each wire on the used parties is a restriction of their local diagonal. 

### `subpartyNormalization_wireDistance`

 All wire distances are scaled by the same positive reciprocal diagonal
exponent upon passing to the smaller spectrum. 
