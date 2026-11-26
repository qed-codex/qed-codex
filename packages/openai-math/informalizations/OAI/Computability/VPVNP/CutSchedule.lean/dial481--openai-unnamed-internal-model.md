---
{
  "module": "OAI/Computability/VPVNP/CutSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CutSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CutSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cut widths in the paired chain

The primary paper uses a chain of length `2^H`. Equation (9.1) allocates
`(H − ⌊log₂ i⌋) Δ` bits to the interior cut numbered `i`. On the first half
this is exactly the width of the doubled primed cut plus one block. On the
tail there is one block. The field layouts below keep the mode at the first
position and the zero padding at the end.


### `width`

 Number of bits on a cut, with both missing endpoint cuts clamped. 

### `width_tail`

 On every nonempty cut in the tail, including the middle cut, the width is one block. 

### `width_double`

 Doubling the primed cut number saves exactly one block, even at the
middle cut where the doubled primed cut is the empty endpoint. 

### `Bits`

 A width-`w` Boolean word indexed by the integers from zero to `w - 1`. 

### `splitBits`

 Split a cut into its contiguous left and right fields. 

### `firstHalfLayout`

 The first-half layout in Section 14.1 in the order mode, exterior primed
bits, exponents, padding. Exponents use the RAM's fixed-width binary encoding.
A zero width gives the unique empty bit string. 

### `tailLayout`

 Tail cuts store one mode, the evaluator configuration, and trailing padding. 

### `firstHalf_unique`

 Exterior bits and the accumulated label exponents uniquely fix each
first-half cut string once the mode and canonical zero padding are imposed. 

### `tail_unique`

 The configuration and mode determine exactly one canonically padded
tail cut, also when no padding is needed. 

### `accumulated_lt`

 Every prefix sum of local `2r`-bit increments fits in the paper's `Z = 2H`
bits when `2r < H`, as verified in Section 14.1. 
