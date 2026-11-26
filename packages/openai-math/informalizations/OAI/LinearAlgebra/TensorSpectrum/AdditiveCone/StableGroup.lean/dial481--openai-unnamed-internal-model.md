---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/StableGroup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/StableGroup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/StableGroup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stable additive group of a commutative semiring

Pairs represent formal differences. Two pairs agree if their cross sums become
equal after adding one common catalyst. This relation works without cancellation
in the original semiring.


### `StableGroup`

 The additive group obtained by identifying formal differences whose cross
sums agree after adjoining one common catalyst. 

### `mk`

 The formal difference represented by `(a, b)`. 

### `exists_mk`

 Every stable group element is represented by one pair. 

### `embed`

 The canonical additive map into the stable group. 

### `embed_eq_embed_iff`

 Equality of embedded semiring elements is exactly stable equality. 

### `mk_eq_zero_iff`

 A pair is zero exactly when its two entries are stably equal. 

### `mk_eq_sub_embed`

 Formal pairs are differences of canonical embedded elements. 
