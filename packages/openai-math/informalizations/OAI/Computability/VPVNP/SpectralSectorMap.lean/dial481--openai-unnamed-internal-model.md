---
{
  "module": "OAI/Computability/VPVNP/SpectralSectorMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorMap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interpolation on a sector of the spectral wire geometry

Section 4.1 constructs a sector from two constant-speed segments or rays
whose distance at parameter `r` equals `c * r`. Equation (2.2) forces
affine interpolation of sector coordinates to trace a constant-speed segment.
Taking the radial parameter set to be `Icc 0 R` gives a triangle, and taking
it to be `Ici 0` gives the entire quadrant.


### `sectorDomain`

 Coordinates in the nonnegative quadrant with radius in `S`. 

### `sectorDomain_convex`

 Convexity of the radial interval gives convexity of the sector. 

### `sectorPoint`

 The point at fraction `v / (u + v)` on the chord joining the two rays at radius `u + v`.
The total function is used only on its sector domain. 

### `sectorPoint_boundary_distances`

 Distances from the two ends of the chord at the given radius. 

### `sectorPoint_axis_left`

 The horizontal coordinate axis agrees, up to distance zero, with the first ray. 

### `sectorPoint_axis_right`

 The vertical coordinate axis agrees, up to distance zero, with the second ray. 

### `ray_fraction`

 A constant-speed boundary ray carries affine combinations of parameters to fractions. 

### `sectorPoint_atFraction`

 Interpolating the coordinates of any two points in the sector interpolates their
images at the same fraction. This applies to both boundary and interior points. 

### `chord_distance_of_le`

 Exact distance between two fractions of the same chord, before passing to the metric
quotient. 

### `sectorPoint_distance_le`

 A uniform continuity estimate comparing two slices. In particular it has no denominator
at the vertex of the sector. 

### `sectorPoint_continuousOn`

 The sector map is continuous on the closed triangle or quadrant, including its vertex. 
