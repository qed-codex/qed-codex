---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpConvolutionControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpConvolutionControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed finite control for triangular, truncated convolution

Polynomial coefficients occupy equal-width flat cells. Both input arrays have
D cells. The left array is consumed; the right array is retained. The output
array is preallocated with D zero cells. Unary loop counters and indices are
runtime stacks, so changing D does not change this control program.

The scalar product-and-accumulate command is inserted as a fixed command. Its
concrete implementation uses the quartic multiplier and the persistent cell
updater; it is never a semantic-function instruction.


### `copy`

 Order-preserving copy; stack 120 is reserved scratch. 

### `takeCell`

 Stack 104 holds the unary coefficient width, and 121--122 are scratch. 

### `innerStep`

 One actual (i,j) iteration. The inserted fixed command consumes operands
198/199 and accumulates into output cell indexed by unary stack 103. 

### `outerStep`

 At row i, stack 106 has D-i tokens. Its full copy limits the inner loop
to D-i products; the outer copy loses one token for the next row. 

### `command_size`

 Finite control size is independent of every array dimension and value. 
