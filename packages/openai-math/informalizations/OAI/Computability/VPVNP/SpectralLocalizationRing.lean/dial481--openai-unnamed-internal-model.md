---
{
  "module": "OAI/Computability/VPVNP/SpectralLocalizationRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Additive group completion for the spectral localization

We pass from a commutative semiring to a ring by forming formal differences.
Multiplication extends by additivity in each variable, even when addition in
the original semiring is noncancellative.


### `G`

 The additive Grothendieck group of a semiring, equipped below with the induced ring structure. 

### `toG`

 The canonical semiring homomorphism to the ring of differences. 

### `toG_eq_iff`

 Two generators agree exactly when adding a common semiring element makes them equal. 

### `exists_sub`

 Every element of the completion is a difference of two generators. 
