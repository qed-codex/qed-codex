---
{
  "module": "OAI/Computability/VPVNP/DiagonalClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DiagonalClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DiagonalClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Choosing the length and field widths of the diagonal chain

Section 9.1 fixes the chain height using the evaluator's running time before
choosing the processor-address multiplier. The exponent width itself depends
on the height. The evaluator's polynomial factor in that width is absorbed
in the tail clock without increasing the exponent of its exponential factor.
The cut-width exponent is also chosen before the processor multiplier, since
its quartic word width is eventually at most the input length for each fixed
multiplier.


### `tail_clock`

 On exponent inputs of width `Z=2 n^a`, the singly exponential evaluator
fits in the `2^(n^a-1)` tail groups. The polynomial degree in `Z` may be
arbitrary, and the choice of `a` depends only on the exponent envelope. 

### `parameters`

 The order of choices of `a,d₁,d₂,B` for the evaluator. A polynomial tape
radius at every fixed polynomial exponent width suffices, independently of
its exponentially larger clock. 
