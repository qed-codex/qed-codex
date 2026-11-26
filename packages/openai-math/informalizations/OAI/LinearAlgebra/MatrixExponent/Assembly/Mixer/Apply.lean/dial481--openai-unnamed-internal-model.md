---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Apply.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Apply.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Mixer/Apply.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Applying a single linear mixer in every host row

Decode the permutation once and broadcast it. Each row then uses
a Batcher gather on its own short records. The output separates
the group index from the within-group address.


 # Reading a butterfly in an indexed record format 

 # Autocorrelations of binary load words 

 # Weighted autocorrelation tables for one processor 


# Accumulating coefficients before testing mixers

Sum each column over hosts first. The quadratic-size candidate test
on the resulting single table is paid just once. Only the column
sums and the comparisons use long words.



# Computing the least-cost mixer

Each row carries a nonnegative integer load at each block and an
integer weight for each depth. Zero weights disable unused depths.
The circuit returns a single common choice, breaking ties by index.


### `compute`

 The input-scale work is linear in the number of hosts; the exhaustive
search on the block addresses is done only on the aggregated table. 


# Recovering the reset estimate from integer records

All loads may carry a common positive scale. Each position or
contact contributes one record, and unused records carry zero weight.


### `Encodes.bad`

 Computing the winner from short control words gives the same bound
as averaging over nonzero field multipliers. 


# From short records to the reset election

A host row carries one header per possible contact and one for its
own load. A header contains a live bit, a contact bit and a depth.
One local record per block suffices to recover all of the loads at
that position. Global host names do not enter the two lookup tables.


 # The load- and weight-extraction network 

### `elect_records`

 Only the scalar decoder and width parameters enter the seven labels. 


# Constructing the reset schedule from finite control words

The linear permutation and all base depths are determined from
loads, contact totals and the fixed parameters. No minimization over
completed diagrams is required.


### `schedule`

 Any sufficiently large dyadic parameter with the given error margin
works. Both data fields are explicit. The remaining fields certify them. 
