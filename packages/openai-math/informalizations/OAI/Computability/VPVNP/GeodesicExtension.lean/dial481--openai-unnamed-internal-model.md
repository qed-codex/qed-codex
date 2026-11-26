---
{
  "module": "OAI/Computability/VPVNP/GeodesicExtension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GeodesicExtension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GeodesicExtension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The geodesic completion of a spectral wire pseudometric

Corollary 2.5 of *VP and VNP differ over every field* first forms the union
of successive midpoint extensions, then takes its metric completion.
The transport inequality guarantees that midpoints of Cauchy endpoint
sequences converge. Closure of finite configurations preserves spectral
realizability in the completion.


### `existsUnique_segment`

 Fractional points in a space with spectral transport form a unique
constant-speed geodesic between any two endpoints. 

### `exists_separationQuotient_isometry`

 Any distance-preserving map of a pseudometric space into a metric space
induces an isometric embedding of the quotient identifying points at distance
zero. 

### `exists_geodesic_completion_of_wire_transport`

 The completion step of Corollary 2.5, using six-point spectral transport
for Lemma 2.2. The isometric map sends exactly the pairs at wire distance
zero to the same point. 

### `exists_geodesic_completion`

 Corollary 2.5. Every finite spectral wire pseudometric embeds, after
identifying zero distances, into a complete geodesic space whose finite
configurations are realizable up to scale. Equation (2.2) holds throughout
the extension and the geodesic between each pair is unique. 
