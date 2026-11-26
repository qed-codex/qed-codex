---
{
  "module": "OAI/Computability/VPVNP/MacaulayExponentPack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentPack.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentPack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing the exponent input of a scalar equation-coefficient query

One step per variable extracts a pair of radix digits, checks the monomial
divisibility condition, and prepends the little-endian word of their
truncated difference. Processing the low radix digits first leaves the
exponents on the output stack in the original variable order.


### `Streams`

 Stacks for the unary variable counter, the packed residual exponents and the temporary
word-copy buffer. 

### `Port`

 Stack addresses of the ten-register subtraction routine and its three auxiliary streams. 

### `arithmetic`

 Registers zero and one store the radices, two and three the residual
source and column, four the divisibility flag, five through eight the
arithmetic scratch, and nine a zero word. 

### `emit`

 Prepend a copy of the current residual exponent word from register seven to the packed
output stack. 

### `body`

 Read one pair of radix digits, update the divisibility flag, and prepend their truncated
difference to the output. 

### `machine`

 Repeat the residual-exponent body once for each marker on the variable counter. 

### `frame`

 Register stacks with n remaining variable markers, the current packed output and empty copy
scratch. 

### `bodyCost`

 Tick bound for one digit comparison and one residual-word copy at register width w. 

### `Holds`

 Representation of the live registers at a variable boundary. 

### `packed`

 Concatenate fixed-width little-endian exponent words in the given variable order. 

### `initial`

 Set the source and column radices and raw keys, initialize divisibility to true and clear
the scratch registers. 

### `pack_rows`

 A raw-key pair yields the actual ordered formal-polynomial exponent buffer
and the exact divisibility flag consumed by the equation-row dispatcher. 
