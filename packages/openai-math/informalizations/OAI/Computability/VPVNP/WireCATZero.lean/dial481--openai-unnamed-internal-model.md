---
{
  "module": "OAI/Computability/VPVNP/WireCATZero.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireCATZero.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireCATZero.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# CAT(0) completion and the six-party wire inequality

Combining Corollary 2.5, the shifted crossing rigidity, and the squared
midpoint comparison yields a complete CAT(0) target for each spectral point.
The completion still has finite configurations realized by spectral points
over the same coefficient field. Lemma 6.2 then applies to its six wire parties.


### `hasCATZeroSegments_of_realizable`

 Every geodesic space with finite configurations realized by wire metrics
satisfies the CAT(0) squared-distance comparison (4.2). 

### `euclideanSectors_of_realizable`

 At equality in Lemma 4.1, the sectors based at the midpoint and ending
at the third vertex are Euclidean throughout. 

### `exists_catZero_completion`

 A complete CAT(0) space realizes all the distances of the given wire
pseudometric. Its own finite distance arrays remain spectrally realizable. 

### `catZero_embedding`

 Distance-preserving CAT(0) realization used in the cube obstruction. 

### `sixParty_wire_energy`

 Lemma 6.2 for the actual six-party wire distances of a spectral point. 
