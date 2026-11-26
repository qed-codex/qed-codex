---
{
  "module": "OAI/Computability/VPVNP/SpectralInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adjoining finitely many interpolated parties to a spectral point

A finite interpolation tree describes a point in every CAT(0) realization
of a configuration. Each internal node can be adjoined by the fractional
extension of Theorem 2.4(1). Subsequent extensions preserve all old tensor
values and hence the already realized wire distances. This places the
centroids used for the balanced cuts in Section 4.3 simultaneously.


### `ExtendedSpectrum`

 An enlarged finite spectral configuration with its old parties marked.
All placed old tensors keep their values. 

### `ExtendedSpectrum.Parties`

 Finite party set of the enlarged spectral configuration. 

### `ExtendedSpectrum.point`

 Spectral point on the enlarged party set whose values extend those of the original point. 

### `ExtendedSpectrum.old`

 Embedding that marks the original parties inside the enlarged configuration. 

### `refl`

 Regard a spectral point as an extension of itself using the identity embedding on parties. 

### `trans`

 Compose two successive extensions of a spectral point by composing the embeddings of their
marked parties. 

### `RealizesTree`

 The marked party realizes the prescribed tree in every CAT(0) metric
embedding of this finite configuration. 

### `RealizesTree.trans`

 Once a tree is realized, it remains realized in each further extension. 

### `exists_tree_extension`

 A single finite interpolation prescription can be realized while preserving
every old tensor value. 

### `exists_treeFamily_extension`

 Realize all trees in a finite indexed family in one enlarged spectrum. 

### `exists_cubeCentroid_extension`

 The centroids of all subsets of the marked basis corners are parties of
a single extension. Every isometric CAT(0) embedding locates those parties
at the prescribed points of the filled cube. 
