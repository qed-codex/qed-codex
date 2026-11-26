---
{
  "module": "OAI/Computability/VPVNP/LivePublicExpr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicExpr.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicExpr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Length-only operands of the live instruction table

The physical reader supplies the input length, address width, bucket size and
word width. Literals belong to the fixed program. Arithmetic is performed on
natural numbers before packing each output as a word. `Fits` checks every
intermediate result, including inputs to division and logarithms.


### `Geometry`

 Public dimensions read by the live processor, comprising input length, site-address width,
bucket capacity, and RAM word width. 

### `Geometry.n`

 The physical input length in bits. 

### `Geometry.d`

 Bit width of the site address, so a group has two to this power sites. 

### `Geometry.H`

 The per-site RAM bucket capacity. 

### `Geometry.w`

 Bit width of a RAM word in this geometry. 

### `PublicExpr`

 Length expression formed from geometry parameters, literals, natural arithmetic, constant
division, binary logarithms, and powers of two. 

### `eval`

 Evaluate a public expression in natural numbers, using truncated subtraction, floor
division, and the indicated floor or ceiling binary logarithm. 

### `Fits`

 Bound on every intermediate register. The denominator of `divConst` is
also a program literal and must fit if division is performed with word arithmetic. 

### `natPow`

 Fixed nonnegative integer powers use repeated multiplication. 
