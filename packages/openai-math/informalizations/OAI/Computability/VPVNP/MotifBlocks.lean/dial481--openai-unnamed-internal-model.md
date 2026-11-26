---
{
  "module": "OAI/Computability/VPVNP/MotifBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifBlocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed block of wire identities for all demand widths

Theorem 6.1 of *VP and VNP differ over every field* chooses its rational
grids, common denominator multiple, tensor power, selector size and local
maps before seeing the demand widths. Only the rounded grid point, number of
repetitions and payload change with the widths. The energy error is uniform.


### `FixedBlock`

 Data fixed before the demand widths are supplied, including the local
base identities and the global additive error in the width energy. 

### `FixedBlock.radius`

 Positive rational radius bounding the supply-width grid. 

### `FixedBlock.grid`

 Strict demand and supply grids for the chosen masses, spectral comparison, and radius. 

### `FixedBlock.multiple`

 Common positive multiplier used with the grid denominator to obtain integer wire widths. 

### `FixedBlock.power`

 Positive tensor power used in the fixed base identities. 

### `FixedBlock.copyCount`

 Number of summands indexed by the copy selector in each base identity. 

### `FixedBlock.energyConstant`

 Uniform additive constant in the squared supply-energy bound after selector padding. 

### `scale`

 Width scale of one fixed base identity. 

### `selectorBits`

 Bits used to choose a direct-sum copy and the supply profile in each factor. 

### `repetitions`

 Number of fixed blocks required by the integer demand. 

### `sequence_payload_le`

 Every actual selector sequence is admitted by the numerical payload bound. 

### `exists_fixed_block`

 From the paper's spectral inequality obtain one block whose repetitions
cover every nonnegative integer demand and obey the stated energy estimate. 
