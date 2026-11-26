---
{
  "module": "OAI/Computability/VPVNP/PairNativeGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading live geometry inside a pair simulation burst

The eleven public words of the pair include the live length and address width
at slots six and seven, and the literal prefix and its length at slots zero
and one. The remaining geometry comes from bounded register arithmetic with
the fixed numerator and denominator chosen for this live evaluator.


### `program`

 Load the live length, address width and literal prefix from the pair's public words, then
compute the word width and rounded bucket size in registers. 

### `ticks`

 Exact tick count for loading the geometry, including the power computation and the
ceiling-logarithm loop on `n^a`. 

### `ticks_le`

 For fixed ratio the arithmetic takes at most linearly many instructions
in the bit length, including the final loop test. 

### `Fits`

 Bounds on the power, denominator, rounded numerator and shift count that make the bucket
computation exact in `w`-bit registers. 

### `eventually_fits`

 All register bounds hold uniformly at every sufficiently large length
for each fixed choice of the two exponents and address multiplier. 

### `Result`

 Postcondition for the geometry loader. Registers 4 through 7 hold the length, address
width, word width and bucket size, and registers 8 and 9 hold the public prefix length and
word. 

### `program_execute`

 In any linked occurrence, loading the pair geometry consumes only ticks.
The continuation receives the original memories and choice stream. 
