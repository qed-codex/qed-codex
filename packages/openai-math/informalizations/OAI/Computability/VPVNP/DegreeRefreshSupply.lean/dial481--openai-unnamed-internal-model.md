---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshSupply.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshSupply.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshSupply.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The expander supply motif of a degree refresh

Section 7.3 of *VP and VNP differ over every field* divides both arc masses
by the old arc mass. The two copies of the ordered port pairs then have
unit mass, and every directed expander arc has mass `D / d₀`. The Poincaré
bound for the spectral wire pseudometrics supplies the comparison required
by Theorem 6.1. The flattening spectral point also detects connectivity.


### `SpectralPortBound`

 The common Poincaré bound for every labeling of the ports in every
spectral wire pseudometric on the port set. 

### `SpectralPortBound.connected_and_pos`

 The same Poincaré hypothesis implies connectivity and positivity of the
bound. The one-party flattening gives two ports at distance one. 

### `expanderSupply`

 Use every directed arc as one supply edge. Its source's first outgoing
slot is the local selector anchor. 

### `tieMass`

 Each segment tie has unit mass after dividing out the old arc mass. 

### `expanderMass`

 Each expander arc has mass equal to the ratio of the old degree to the new degree. 

### `expander_distanceEnergy`

 The common port bound gives the fixed-motif comparison with the paper's
constant `2 γ d₀ / dH`, independent of the order `D`. 

### `exists_expander_block`

 Fix a single block of exact base identities and a uniform width-energy
error, with the slack `H' = H + 1` used at the degree refresh. 
