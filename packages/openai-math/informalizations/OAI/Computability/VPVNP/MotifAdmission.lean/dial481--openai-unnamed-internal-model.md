---
{
  "module": "OAI/Computability/VPVNP/MotifAdmission.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifAdmission.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifAdmission.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer admission tests for a fixed rational wire motif

Theorem 6.1 of *VP and VNP differ over every field* selects a demand grid
point and a block repetition count from the input widths. The outer supply
index is admitted by testing a rational quadratic bound. Clearing the fixed
mass denominators gives integer algorithms for all three operations.


### `denominator`

 Common denominator of the reciprocal edge masses. 

### `weight`

 The positive integer coefficient of one squared width after clearing denominators. 

### `energy`

 Integral numerator of the squared width norm. 

### `norm_sq_eq`

 The integral energy with its fixed denominator recovers the real norm. 

### `sqrtDigits`

 Consume one base-four digit per recursive step. The result with enough
digits is the binary integer square root. 

### `floorRoot`

 Executable floor square root of a rational energy. Binary input length
bounds the number of recursive steps. 

### `ceilRoot`

 Ceiling of the square root of an unsigned fraction. At a perfect square
the decrement prevents a spurious additional copy. 

### `copies`

 Executable number of block repetitions. 

### `copies_eq`

 The integer calculation gives the ceiling used in the real width estimate. 

### `admit`

 Test the two integer sides of the payload constraint. 

### `coversCoordinate`

 Check that a nonnegative rational grid point dominates the normalized
demand in one coordinate, without division by the demand norm. 

### `selectGrid`

 Choose the first covering point in a fixed ordering of the finite demand grid. 

### `selectGrid_exists`

 The strict demand grids have a covering entry, including at zero demand
where each coordinate of the demand vanishes. The choice depends only on the
ordered table, masses, and input widths. 

### `energy_le`

 Every variable energy accumulator, including intermediate partial sums
of its nonnegative summands, has a fixed quadratic magnitude bound. 

### `copies_le`

 A fixed coefficient bounds the repetition count linearly in the input width. 

### `payloadCap`

 A finite search box containing every admitted outer payload. 

### `admit_operands_le`

 Explicit quadratic bounds on both integers compared by the payload test
on a linearly sized candidate box. 

### `grid_operands_le`

 Quadratic bounds for the integer comparisons used to select a grid point.
Both coefficients are fixed for a fixed grid table. 

### `operand_bits_le`

 Quadratically bounded operands have bit length at most a constant plus
twice the binary logarithm of the input width. 

### `payloadCap_le`

 The finite payload search box is linear in the original maximum width. 

### `copies_root_steps_le`

 The recursion depth in the executable ceiling test is bounded in terms
of the original maximum width and the fixed mass coefficients. 
