---
{
  "module": "OAI/Computability/VPVNP/MotifBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed base identities for wire motifs

In Theorem 6.1, a finite supply grid beats each demand grid point at every
spectral point. The supply witness may depend on the spectral point.
Taking the direct sum of the supply grid and applying strict comparison
yields one copy bound for all powers. Distributing the powers yields actual
ordinary sums of local maps. Each summand is indexed by one copy and an
ordered list of grid points, with widths added edge by edge.


### `binaryWires`

 The ordinary tensor of binary equality wires with a given integer width profile. 

### `payload`

 The supply widths of a selector are the totals of the selected grid profiles. 

### `BaseIdentity`

 The base identity (6.2) before grouping repeated copies by payload. 

### `StrictAtSpectrum`

 The supply profile in the strict width comparison can vary with the spectral point. 

### `uniform_base_identity`

 A single copy count gives base identities for every demand profile in a
finite grid and every power, over the specified field. 

### `connected_grid_base_identity`

 The weighted comparison (6.1) gives a simultaneous base identity on the
integer width grid at every positive denominator multiple. 

### `exists_base_block`

 Choosing the denominator multiple before the tensor power makes the
selector fraction as small as prescribed. The same base identity works for
all rounded demand profiles and bounds the norm of every selector's payload. 
