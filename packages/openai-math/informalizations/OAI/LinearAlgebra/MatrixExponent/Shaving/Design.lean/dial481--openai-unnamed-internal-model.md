---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Shaving/Design.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Shaving/Design.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Shaving/Design.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iteration budgets

Work with exponents of two throughout. A grouping of `2^r` blocks
consumes exactly `r` bits of the block index. After `s j` such
groupings there are `2^(M l)` blocks, each descended from stacks
of `2^t` independent copies.


### `stage_parameters`

 Set `G=2^g`, `q=2^p`. Choose a round count `j`, stack exponent `t`
and height exponent `l`. The final bound covers the complete replication
cost with group exponent `c(j+1)`, uniformly before seeing any input. 

### `group_exponent`

 Choose the exponent controlling all group sizes before the height
is known. The factor `C^(j+1)` covers growth in host occurrences. 

### `iteration_slack`

 Check both admission conditions of round `i`. Here `A` counts all
allocated occurrences at the current grouping step and `T,L` are the
initial scale and total width budget. 


# Volume and arity at the end of a stage

The iteration saves `h^a` in total width. Split the logarithmic slack
`aδ` between the descriptions, the cost of realizing the transcript, and
the remaining constant factors.


### `polylog_le`

 Any fixed power of the logarithm fits in any positive power budget. 

### `assembly_remainder`

 Quasipolynomial work in the height uses at most `1/h` of a linear
input-size budget. 

### `assembly_saving`

 `P` is the processor count, `V` the record volume, `m` the input size,
`S` the initial block count and `d` the replication factor. The five volume
terms are common work, short control, terminal payloads, exposed bits,
and the subpolynomial additive error. 


# Dyadic parameters of one round

Write `D = 2^d`, `G = 2^g`, `q = 2^p`. Run exactly `2g` beats.
Any fixed power of the logarithm of `D` fits into both `G` and `q/G`.


### `choose_round`

 The beat multiplier and all logarithmic losses are independent of
`D`. The lower cutoff on its logarithm is arbitrary. 
