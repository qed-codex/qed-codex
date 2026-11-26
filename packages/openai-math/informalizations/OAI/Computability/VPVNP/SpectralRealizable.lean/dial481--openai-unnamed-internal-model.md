---
{
  "module": "OAI/Computability/VPVNP/SpectralRealizable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralRealizable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralRealizable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite configurations of spectral wire distances

A configuration of labelled points is realized up to scale when the distances
between labels are a single positive multiple of their distances in a spectral
wire pseudometric. Several labels may designate the same tensor party.


### `WireRealization`

 The data realizing a matrix of distances by finitely many tensor parties.
The ambient party set has at least two members, as in Section 2. 

### `WireRealization.Parties`

 Finite ambient party set, with at least two members, carrying the wire metric of the
  realization. 

### `WireRealization.spectrum`

 Spectral point that assigns the wire distance between ambient tensor parties. 

### `WireRealization.label`

 Party representing each label of the given configuration. Labels may share a party. 

### `WireRealization.scale`

 Positive factor multiplying the spectral wire distances to recover the given labelled
  distances. 

### `RealizableUpToScale`

 Realizability up to a common positive scale, in the sense of Section 2.2. 

### `RealizableUpToScale.relabel`

 Restrict or repeat any of the labels in a realized configuration. 

### `RealizableUpToScale.smul`

 The choice of units for the distance matrix does not affect realizability. 
