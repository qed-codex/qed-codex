---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient streams for multiplication in the advised field

One Horner round scans the accumulator, modulus and multiplier in increasing
degree order. The preceding accumulator limb supplies the shift. Its last limb
supplies the reduction coefficient for the whole round. The scan records the
number of prime-residue additions, multiplications and negations performed.


### `ScanState`

 Live streams in a Horner round. The output grows in reverse order. 

### `ScanState.modulus`

 Remaining low-degree-first coefficients of the monic modulus below its leading term. 

### `ScanState.multiplier`

 Remaining low-degree-first coefficients of the multiplier. 

### `ScanState.accumulator`

 Remaining coefficients of the accumulator from the preceding Horner round. 

### `ScanState.output`

 Newly computed coefficients stored in reverse degree order during the scan. 

### `ScanState.previous`

 Old accumulator limb carried forward for the polynomial shift. 

### `ScanState.work`

 Number of prime-residue operations charged so far in the coefficient scan. 

### `step`

 One row consumes one limb of each input. The two products and two sums
are operations in the prime residue ring. 

### `run`

 A tail-recursive scan with one transition per coefficient. 

### `ScanState.limbs`

 Count the live limbs of the scan, including the digit and reduction coefficient. 

### `shift`

 Coordinates of a shift, seeded with an arbitrary preceding limb. 

### `ProductState`

 The counters measure prime-residue operations. Each round starts by
negating the last limb and then executes the row scan. 

### `ProductState.coefficients`

 Current product accumulator, stored as coefficients in increasing degree order between
  Horner rounds. 

### `ProductState.work`

 Cumulative prime-residue operation count across completed Horner rounds. 

### `round`

 Process one Horner digit using the negated top accumulator coefficient for reduction, then
reverse the new coefficient list. 

### `product`

 The machine reads Horner digits from the highest degree down. 

### `product_correct`

 The complete stream multiplier returns the Horner product, performing
exactly `e * (4 * e + 1)` prime-residue operations. 

### `scan_bits_le`

 Count the three persistent input lists conservatively in addition to all
live scan limbs. The bound holds after any number of steps of any round. 
