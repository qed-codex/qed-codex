---
{
  "module": "OAI/Computability/VPVNP/ExponentTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExponentTrace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExponentTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Accumulating the nominated production and gadget exponents

At each live first-half cut, the program checks the primed exterior bits
and the new cumulative exponents against the preceding cut. Section 14.1
requires that a fixed sequence of pair paths determine exactly one sequence
of cut strings, with zero initial exponents and zero padding. Here `inc`
combines both kinds of label counters in the order used by the evaluator.


### `Word`

 Fixed-width RAM word used to store a cumulative label exponent. 

### `partialSum`

 Sum of the per-pair increments before a given cut. 

### `LiveBits`

 A complete sequence of first-half cuts has one binary word for every
nonempty cut numbered `i+1` with `i < 2^h`. 

### `Exterior`

 Primed exterior cuts, including the two empty endpoint strings. 

### `counters`

 Decode the running counters; before the first group all counters are zero. 

### `Valid`

 The local checks performed by each live pair group. The equality of
natural numbers enforces rejection on overflow. 

### `existsUnique_live`

 For any fixed exterior choices and local pair paths whose prefix sums fit,
the local checks admit exactly one binary first-half cut assignment. 

### `firstHalf_no_overflow`

 Instantiation with the paper's `Z = 2H` exponent width, where `H=h+1`.
Every pair contributes less than `2^(2r)` to each label, even if later
cancellation gives zero after evaluating the term's gadget labels. 

### `middle_counters`

 At the middle cut the exponent vector passed to the evaluator is the
sum of the increments for every primed pair. 
