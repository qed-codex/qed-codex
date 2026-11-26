---
{
  "module": "OAI/Computability/VPVNP/SpectralMidpointTower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMidpointTower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMidpointTower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The countable union of finite spectral midpoint extensions

For Corollary 2.5, retain the original parties and index the new parties by
their creation times. A pair is scheduled at arbitrarily late stages, so a
stage at which both parties already exist adds their midpoint. Old distances
are preserved at every subsequent stage. Every finite list therefore has
its full distance matrix in one finite spectrum.


### `birth`

 A party named by its creation time first exists at the next stage. 

### `scheduled`

 The left unpairing coordinate encodes the pair and the right coordinate
can be chosen arbitrarily large. 

### `exists_midpoint_tower`

 The finite spectral pseudometric extends to a countable pseudometric
space with a midpoint for each pair. Each finite configuration of the new
space occurs, with scale one, in a finite spectral point. 
