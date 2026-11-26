---
{
  "module": "OAI/Computability/VPVNP/RAMTapePhysicalInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePhysicalInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePhysicalInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete uniform finite-stack reader for a live site

The only initially occupied stack contains the physical input. This fixed
control measures its length, prepares the exact widths, and extracts the
literal data fields. It retains the public length, address width, and bucket
capacity in unary for the site's remaining computations.


### `Public`

 Retained unary length and address-width tallies of the physical site reader. 

### `Registers`

 Complete reader bank combining parsing ports, parameter scratch, and the retained public
tallies. 

### `lengthPort`

 Port holding the measured length of the full physical input in unary. 

### `addressWidthPort`

 Port holding the computed site address width in unary. 

### `bucketPort`

 Port holding the computed bucket capacity in unary. 

### `physicalReader`

 Code independent of the length. The rational exponent of the live bucket
is `p/q` (in the paper, `1-δ`). 

### `physicalResult`

 All private scratch is empty at return. The length, address width and
bucket capacity are available alongside the actual prefix and data fields. 

### `physicalReader_runs`

 From just the original site tape, the fixed processor obtains its local
input with polynomially bounded bit-stack instructions. The public parameters
are computed on its branch path from the length. 
