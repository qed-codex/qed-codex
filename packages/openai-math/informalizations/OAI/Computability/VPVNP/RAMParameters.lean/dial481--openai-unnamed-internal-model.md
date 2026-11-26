---
{
  "module": "OAI/Computability/VPVNP/RAMParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer computations of the transcript parameters

The prescribed rational multiples of the binary logarithm can be rounded
using only integer powers and integer logarithms. In particular a processor
need not compute any real-valued function to determine its field widths.
The virtual site count is the least power of two satisfying the budget
inequality of Section 11.


### `roundedUp`

 Ceiling of a nonnegative rational multiple of `log₂ n` computed over
integers. For fixed numerator and positive denominator the powers have
`O(log n)` bits. 

### `roundedDown`

 Floor used for the number of compression blocks. 

### `addressWidth`

 The rounding of the live address width from §9.1. 

### `virtualSiteExponent`

 Binary site count for the virtual group in §11. 

### `virtualSiteExponent_le_iff`

 The chosen number of virtual sites is exactly the least permitted power of
two, including cases in which a single bucket covers the entire budget. 

### `eventually_liveInputFits`

 For the actual live choices of Section 9, the whole literal and shared
input is available to the coefficient program at every sufficiently large
length. 
