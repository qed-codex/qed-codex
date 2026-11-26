---
{
  "module": "OAI/Computability/VPVNP/PolynomialBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PolynomialBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PolynomialBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Closure properties of nonuniform polynomial bounds

The index of a p-projection may revisit small lengths infinitely often. A global
bound by a power of `n + 1` handles those lengths when composing two indices.


### `of_eventually_le`

 An eventual upper estimate by a polynomially bounded function suffices. 

### `exists_global_bound`

 Absorb the finite initial segment of a bounded function into its leading constant. 

### `comp`

 Composition preserves polynomial bounds even for nonmonotone index functions. 
