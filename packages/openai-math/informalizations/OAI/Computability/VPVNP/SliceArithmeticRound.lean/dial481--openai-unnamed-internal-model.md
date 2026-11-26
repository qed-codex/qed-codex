---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticRound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticRound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticRound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The uniform coefficient loop of one Horner round

The loop consumes the three low-degree-first streams of limbs. The result is
pushed in reverse bit order so that one ordinary stack reversal prepares the
next accumulator.


### `Item`

 The three prime-field limbs consumed at one coefficient position of a Horner round. 

### `Item.old`

 Old accumulator limb saved as the shifted predecessor at the next coefficient position. 

### `Item.coeff`

 Coefficient of the defining monic polynomial below its leading term, used in reduction at
  this position. 

### `Item.factor`

 Coefficient of the multiplier at the current degree. 

### `Acc`

 The previous accumulator limb and the registers last written by a row.
The output list stores the new limbs from high to low. 

### `Acc.previous`

 Preceding old accumulator coefficient, supplying the shift term for the next row. 

### `Acc.coeff`

 Most recently loaded defining-polynomial coefficient in the row registers. 

### `Acc.factor`

 Most recently loaded multiplier coefficient in the row registers. 

### `Acc.result`

 Prime-field coefficient computed by the most recent Horner row. 

### `Acc.scratch`

 Temporary residue holding the Horner digit times the current multiplier coefficient. 

### `Acc.output`

 Coefficients emitted by the processed rows, stored in reverse degree order. 

### `next`

 Compute the shifted predecessor plus the reduction and digit products, prepend the result,
and save the old limb for the next row. 

### `fold_vector_output`

 The vector of streamed row results is the companion step of Horner's rule. 

### `packed`

 Pack low-endian words consecutively, retaining the full working width. 

### `registers`

 Register order of the Horner-row kernel. 

### `streams`

 The remaining stream inputs, the accumulated output, and the row markers.
Other caller ports and suffixes of the input streams are preserved. 

### `scan`

 One finite control for all moduli, word widths and extension degrees. 

### `scan_runs`

 A complete scan on the represented coefficient stream, including
arithmetic, register loads, output stores and loop tests. 

### `horner_scan_runs`

 The checked bit-stack execution for one digit reads each of the three input
vectors and writes the complete next accumulator in globally reversed bit order.
Register 6 contains the last output limb for the following reduction. 
