---
{
  "module": "OAI/Computability/VPVNP/MacaulayBaseAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayBaseAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayBaseAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Initial advice of the augmented Macaulay matrix reader

The private decoder words specify the number of original equations, affine
pins and multiplier monomials. Its two scalar banks contain the signed grammar
coefficient circuit and the actual pin mask and field values. Both are reusable
across all row and column queries. Scratch decoder registers may change, but
their widths and the exact leaf data are preserved by the ready predicate.


### `inputs`

 The source radix is the multiplier degree for an equation, and the point
bound for an appended powered monomial. The column radix is common. 

### `scalars`

 Encode the extension-field element zero or one selected by the Boolean flag, using v bits
per ground-field coordinate. 

### `leaf`

 The immutable leaf bank for the integer, affine and powered-monomial arms. 

### `registers`

 Canonical initial decoder registers. The two externally aliased addresses
and all dispatch outputs start at zero. 

### `RawPort`

 Physical working ports for the row decoder together with the coefficient-reader advice. 

### `initial`

 Initialize the row decoder with the equation, pin and multiplier counts and install the
scalar advice used by all row queries. 

### `ready`

 The decoder has the required counts and bounded register widths, and its leaf bank still
holds the specified coefficient and pin advice. 

### `ready_length`

 Every state permitted at a repeated-query boundary satisfies the same height
bound. The encoded matrix dimensions themselves may be exponential. 

### `ready_length_uniform`

 The physical ready cap follows from the common reader plan before the
particular field and its affine pins are chosen. 
