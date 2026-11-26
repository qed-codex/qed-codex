---
{
  "module": "OAI/Computability/VPVNP/SpectralTangent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralTangent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralTangent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rescaling at a basepoint of a wire metric space

Lemma 4.1 passes to a simultaneous limit of rescaled configurations. An
ultrafilter tending to infinity takes that limit for all bounded marked
sequences at once. Its pseudometric retains every finite configuration when
the cone of spectral configurations is closed. Fractional points can be
chosen term by term.


### `tangentScale`

 The rescaling factors at the successive terms of a marked sequence. 

### `tangentFilter`

 The filter used for simultaneous convergence of all marked distances. 

### `Tangent`

 Sequences at uniformly bounded rescaled distance from the basepoint. 

### `Tangent.point`

 Sequence of marked points whose rescaled distances to the basepoint have a common upper
  bound. 

### `tangent_dist_tendsto`

 Rescaled distances converge to the distance in the tangent pseudometric. 

### `tangent_hasFractions`

 A geodesic fraction can be taken independently at each term. 

### `tangent_realizableConfigurations`

 Finite configurations pass to the tangent space by closedness of each
realizable cone. The common positive scale absorbs the rescaling factor. 
