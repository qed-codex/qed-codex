---
{
  "module": "OAI/Computability/VPVNP/CrossingSpectralBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingSpectralBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingSpectralBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectral bounds for the two shifted crossing cuts

Section 3.2 of *VP and VNP differ over every field* places four terminals and
two pairs of auxiliary centers at a single spectral point. The two cuts have
independent ranks. This file derives the numerical inequality in the wire
distances from the integral factors and local restrictions.


### `crossing_value_le`

 The sum of the spectral values of the two cut networks bounds the value
of the original wires, including when some of the wire dimensions vanish. 

### `crossingNetwork_value`

 The four terminal wires and one rank wire give the cost of either cut.
Reversing the second wire exchanges its assignments to the two centers. 

### `crossing_spectral_inequality`

 The spectral inequality used in the proof of norm rigidity. Both pairs
of centers and all four terminals may occupy arbitrary, even coincident,
parties at the same spectral point. The cut ranks need not agree. 
