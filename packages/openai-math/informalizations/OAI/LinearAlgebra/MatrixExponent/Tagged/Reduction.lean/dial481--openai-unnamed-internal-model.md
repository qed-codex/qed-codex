---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Tagged/Reduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/Reduction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/Reduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Width and sorting costs for many independent lists 

### `lift_range`

 Two sorting lifts pay for each doubling of the record width. 

### `parameters`

 Reserve enough exponent slack to absorb both width doubling and
parallel sort lifting, uniformly in the logarithm `v` of the batch size. 


# Signed distinctness and permutation verification

Each row of the first list either remains real (weight `-1`) or
receives a dummy flag (weight `1`). If a row is absent from the
second list, summing over its flag gives zero in every characteristic.


### `cancel`

 A signed test of distinctness on twice as many rows checks a permutation.
The first list must have distinct rows, as it does when tagged by position. 

 # Tagged permutation queries from element distinctness 

### `tag_of_distinct`

 A network testing `t` lists on independent inputs gives one checking
`t` independently specified permutations. The extra cost is linear in
the total input length and does not depend on the coefficient field. 

 # Restricting a batch by fixing extra inputs to accepting constants 

 # Transferring a distinctness batch to one large permutation verifier 

### `transfer`

 The replication exponent is `v`. Using `2^k` slices and `j` column
lifts costs at most a constant times `4^k 4^j` times the initial size. 


# From tagged permutations to independent lists

A batch of size `t` gives one permutation verifier on
`2^(w + floor (log₂ t))` rows at list width `w+1`. The cost of
lifting the sort and slicing the payload is absorbed by the assumed
power-of-logarithm lower bound.


### `manyList_full`

 The exact-network lower bound with a superpolynomial range of batch sizes. 

### `manyList_of_tag`

 Restrict the batch sizes to those needed by the compression iteration. 
