---
{
  "module": "OAI/Computability/VPVNP/WireGeodesic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireGeodesic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireGeodesic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fractional points in the spectral wire geometry

Corollary 2.5 and Section 4 of *VP and VNP differ over every field* use
the metric characterization of a point at a specified fraction along a
segment. The six-point transport inequality makes such a point unique in a
metric space and controls its dependence on both endpoints.


### `AtFraction`

 The two endpoint distances specifying a fractional point. 

### `HasFractions`

 Every pair admits an interpolating point at each fraction. 

### `FractionTransport`

 Equation (2.2), controlling interpolation along two segments. 

### `RealizableConfigurations`

 Every finite list of points is jointly realized up to one scale in a
spectral wire pseudometric. 

### `atFraction_unique`

 Metric separation gives uniqueness at every fraction. 
