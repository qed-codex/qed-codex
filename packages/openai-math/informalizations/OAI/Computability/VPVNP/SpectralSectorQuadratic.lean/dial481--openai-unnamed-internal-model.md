---
{
  "module": "OAI/Computability/VPVNP/SpectralSectorQuadratic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorQuadratic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorQuadratic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Euclidean distances of possibly degenerate spectral sectors

Section 4.1 obtains a seminorm on the coordinate plane of a sector. Realizing
the distances on any nonempty open set forces its square to be a positive
semidefinite quadratic form, including when some directions have zero length.


### `exists_normPreserving_map_of_realizable`

 The separation quotient of a finite-dimensional seminormed space inherits an
inner product if its eight-point distances are realizable by spectral wires. 

### `seminorm_sq_smul_sub`

 The squared seminorm of a difference along two fixed directions has a
single mixed coefficient valid for every real parameter, including when one
or both directions lie in the kernel. 

### `sectorSeminorm_quadratic`

 The square of the pullback seminorm on the coordinate plane of a spectral
sector is a quadratic form. The topology in the open-set hypothesis is the
usual topology of the coordinate plane. 
