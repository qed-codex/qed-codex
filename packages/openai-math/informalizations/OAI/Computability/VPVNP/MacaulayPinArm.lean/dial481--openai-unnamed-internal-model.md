---
{
  "module": "OAI/Computability/VPVNP/MacaulayPinArm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPinArm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPinArm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Calling the affine pin routine on the decoded Macaulay row

The positive-divisibility branch takes its exponent buffer from the equation
scan. It copies the decoded pin index, reads the pin table, and returns the
field scalar directly on the matrix reader's result port.


### `mount`

 Route the affine query's exponent input to the equation scan's packed residuals and its
scalar output to the reader result. The other query ports use the embedded payload. 

### `machine`

 Copy the decoded pin index to the affine query's binary input, then run the query on the
reader's ports. 

### `Preloaded`

 The embedded payload ports contain the initial affine query frame for the given pin advice,
extension modulus and scalar word width. 

### `preload`

 Install the initial affine query frame at the embedded payload ports of the given stack
bank. 

### `cost`

 Tick bound for copying a width-`w` pin index and looking up its affine coefficient. 

### `bounded`

 One positive-divisibility affine call. The row decoder's register,
the flag, the powered scan and the immutable advice survive the call. 

### `coefficient`

 The same bus call returns the coefficient of the field polynomial used
in the Macaulay row, in the rank engine's power-basis representation. 
