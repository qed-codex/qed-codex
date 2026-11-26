---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Restore/Elect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Restore/Elect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Restore/Elect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The common template and label capacity for a reset 

 # Electing a valid reset uniformly over a batch 


# Budgeting a common permutation of old blocks

The permutation table itself is computed once, then broadcast.
The work quadratic in the number of block indices fits in the
host budget. Per host the circuit is linear in the number of indices.



# Electing a mixer

All pairwise tests of block indices take place on a single aggregated
array. There are fewer such pairs than host addresses. The only
arithmetic repeated at every block operates on short words.



# A sequence of encoded phases

The bound on elementary coefficients stays fixed across concatenation.
The rate and additive loss compose affinely. Separate limits keep long
addresses out of the polynomial charged at every block.


### `Sequence`

 The indices are incoming and outgoing core degrees and neighbor
widths, subdivision, step count, and the two affine coefficients. 

### `Enough`

 Uniform headroom, established once for the whole sequence. 

### `Inside`

 Invariants after exactly `i` elementary steps. 


# Choosing one repeatable block of encoded phases

Use the same gadget, subdivision and reset rotor for the quantitative
reduction and for the encoded sequence. The neighbor allowance after
reset is chosen before fixing the incoming allowance.


 # Checking headroom at each phase boundary 

 # Growth estimates for a single encoded phase 

 # Composition of an encoded sequence with uniform budgets 

 # Unconditional realization of a wire-saving batch phase 
