---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapPortAgreement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPortAgreement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPortAgreement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Port comparisons for the grouped motif map

A party visits the source incidences in a fixed edge order, then the target
incidences in that order. A loop contributes both of its ports. Within each
port the selector copies are consecutive. Agreement of the resulting two
word arrays is the selector test in the motif entry algorithm on page 21.


### `Port`

 The two incidences of a self-loop are distinct ports. 

### `portTag`

 Read a half-wire tag through its source or target incidence. 

### `ports`

 The comparison schedule uses only the party, supply graph and fixed edge numbering. 

### `leftTags`

 The incident-port array in port-major order. 

### `rightTags`

 Each block repeats the anchor's selector sequence. 

### `consistent_iff_scan`

 Pointwise equality of the two resident arrays computes precisely the
motif selector agreement test, including an empty selector sequence. 

### `consistent_native`

 On the two resident tag arrays the fixed native dispatch branches exactly
as the grouped motif entry does. All inputs incur the same instruction count. 
