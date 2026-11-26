---
{
  "module": "OAI/Computability/VPVNP/LiveWordCapacity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveWordCapacity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveWordCapacity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word capacity for the live processor's public operand expressions

Only two exponentials occur among the static operands: the physical site
count and the virtual site count. For fixed address parameter both counts
grow polynomially in the input length. This suffices for *every intermediate
register* of an operand, including any multiplication before a division.
The later choice of the address parameter does not impose an upper bound
on the exponent of the permitted polynomial.


### `paperGeometry`

 Live processor geometry at input length n, with site address width and RAM word width from
the address parameter and bucket size H n. 

### `SitePowers`

 The syntax used by the complete fixed public bank. 

### `SitePowers.fits`

 Polynomial bounds and simultaneous intermediate word fit for one
fixed operand. The live bucket size may be any polynomially bounded function. 

### `fits_bank`

 Uniform threshold for every operand in any finite table. 
