---
{
  "module": "OAI/Computability/VPVNP/SpectralSectorSeminorm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorSeminorm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorSeminorm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The pullback seminorm of a spectral sector

In Section 4.1 the speeds of parallel affine segments agree at every
interior base point. The triangle inequality on a small translated triangle
gives subadditivity of the common speed. Reversing and rescaling small
segments gives absolute homogeneity. Moving endpoints towards an interior
point and taking a one-sided limit extends the distance formula to the
entire convex sector, including its boundary.


### `exists_sector_seminorm`

 The pullback distances of an affine geodesic parametrization on a convex
sector with nonempty interior are given by a single seminorm on the plane.
The conclusion includes pairs of boundary points. 
