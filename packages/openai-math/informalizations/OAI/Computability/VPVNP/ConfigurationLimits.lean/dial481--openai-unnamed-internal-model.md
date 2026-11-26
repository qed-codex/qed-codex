---
{
  "module": "OAI/Computability/VPVNP/ConfigurationLimits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ConfigurationLimits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ConfigurationLimits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Limits of scaled finite spectral configurations

The compactness step in Lemma 2.3 uses a positive lower bound on the diameter
of a normalized configuration. For a fixed set of `k ≥ 2` used parties, the
spanning-tree estimate supplies the lower bound `1 / (k - 1)`.


### `exists_scaled_configuration_limit`

 A nonzero coordinatewise limit of scaled configurations is realized by a
point of the same compact spectrum at a positive scale. The coordinates can
be the ordered pairs of a finite label set. 

### `exists_wire_configuration_limit`

 A nonzero coordinatewise limit of normalized configurations on fixed
parties is realized on the same parties. Labels may repeat. 

### `Realizes`

 A matrix of labeled wire distances realized at one spectral point and one
positive common scale. 

### `realizes_limit_of_finite_patterns`

 After normalization on the used parties, there are finitely many label
patterns. One pattern occurs along an infinite subsequence, so its spectrum
realizes the nonzero limiting configuration. 

### `zero_wire_configuration`

 Repeating one party realizes the zero configuration at unit scale. 
