---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Lower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Lower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Verification/Lower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite support from a Shannon entropy bound

Keep every atom of weight at least `exp (-L)`. No zero-weight atom
contributes, and the discarded mass times `L` is bounded by the entropy.
Both entropy and the scale logarithm are taken in natural units.


### `entropy_gap`

 A positive gap remains at support rate `3*η+ε`. This includes
entropy rate zero without requiring that the seed be deterministic. 

 A mixture of a uniform verifier and two constant decisions. 

### `Support.entropy`

 Pay for the original seed with probability just above the required
acceptance gap. Its error is chosen small enough to preserve that gap. 

 # A polynomial encoding of all output blocks 

### `sound`

 Enough distinct successful evaluations force every coefficient
of the block residual to vanish. 

 # Arithmetic instructions and equality tests in a block sketch 

### `sketch_cost`

 The large rectangular multiplication is the only non-linear
part. Each scalar of the padded inputs contributes at most two gates. 

 Simulating each seed separately preserves its decision and probability. 


# The rectangular expression in the verification characterization

This evaluates the tradeoff and both critical budgets from the last
paragraph of Section 8. Identifying the rectangular expression with
the cost of randomized arithmetic and equality-test trees is a
separate theorem of the cited work on verification.


 # From a rectangular algorithm to uniform public-seed verification 


# The cost forced by independent output combinations

The finite bound uses the actual field exponent. At the benchmark,
the bound yields the verification tradeoff whenever a verifier
provides enough independent output combinations at low border rank.



# Public-seed verification lower bounds

Both budgets give a finite set of seeds with a strict acceptance
gap. Its size bounds the loss of independent output combinations.
Reading entries gives a quadratic bound even for large seed sets.

