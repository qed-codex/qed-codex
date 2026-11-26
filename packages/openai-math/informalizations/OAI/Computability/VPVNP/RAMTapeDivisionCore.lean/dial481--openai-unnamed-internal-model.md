---
{
  "module": "OAI/Computability/VPVNP/RAMTapeDivisionCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeDivisionCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed stack control for restoring division

The control reverses the dividend to expose its most significant bit, tests
the divisor for zero, and initializes a zero remainder of the same width. A
forward scan saves the divisor, candidate bits and trial difference on three
scratch stacks. The restore scan puts the divisor back and uses the final
borrow to choose the new remainder.


### `Port`

 Ports for the dividend, its reversed feed, divisor, quotient, remainder, and three
trial-subtraction stacks. 

### `State`

 Control of restoring division, including dividend reversal, zero-divisor handling, trial
subtraction, and quotient-bit emission. 

### `code`

 Perform binary restoring division from the most significant dividend bit. For a zero
divisor emit a zero quotient and return the dividend as the remainder. 

### `Data`

 Bit stacks for restoring division, including the trial remainder and difference used to
resolve each quotient digit. 

### `Data.input`

 Dividend bits before reversal into most-significant-first order. 

### `Data.feed`

 Remaining dividend bits in the order in which division consumes them. 

### `Data.divisor`

 Divisor word restored after every trial subtraction. 

### `Data.remainder`

 Current partial remainder of the division. 

### `Data.quotient`

 Quotient digits accumulated as the dividend bits are consumed. 

### `Data.saved`

 Divisor bits held temporarily during initialization or trial subtraction. 

### `Data.original`

 Candidate remainder bits saved before subtraction for the borrow case. 

### `Data.difference`

 Trial-difference bits saved for the case in which subtraction succeeds. 

### `Data.stacks`

 Read the division bank by its stack port. 

### `Data.set`

 Replace one of the eight division stacks. 

### `tick`

 One deterministic transition, written using concrete record projections
to simplify the verified word-level macros. 

### `Run`

 An execution of the division control between two states and banks in exactly the given
number of stack steps. 
