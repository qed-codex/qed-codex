---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateCramer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCramer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCramer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Two top-degree determinant queries for a greedy coordinate

Appendix D.2 obtains a coordinate from a nonsingular minor and the minor with
one row replaced. Their top pencil coefficients have the same sign. Division
can therefore use the scalar returned by each Schur computation directly,
including in characteristic two.


### `topPencil`

 The Schur evaluator for the outer top coefficient of a constant matrix. 

### `sign_mul_topPencil`

 The Schur output differs from the determinant by the same sign at every
matrix of the given order. 

### `topPencil_div_map`

 Two machine outputs can be divided without correcting either sign. This
also holds after mapping the executable scalar ring into the advised field. 

### `replacedMinor`

 The canonical numerator for a selected-row representation. 

### `topPencil_div_rowCoordinate`

 Packed-ring queries for the two minors produce the scalar appearing in the
greedy coordinate formula. 

### `Extra`

 Keep the numerator outside the inverse's entire workspace. A second external
stack is used temporarily to copy it into the multiplier's query operand. 

### `Port`

 Stack ports for inversion and multiplication together with the numerator, denominator, and
copying workspace. 

### `frame`

 Boundary of the quotient operation. The input denominator and numerator
are kept on distinct read-only ports. The output is the multiplier accumulator. 

### `digits`

 Pack the extension-field coefficient vector as fixed-width binary limbs for the quotient
routine. 

### `quotientCall`

 Invert the denominator in the polynomial basis and multiply by the saved numerator. 

### `quotientClock`

 Only the inverse, one operand copy, and one multiplication are charged here. 

### `quotientCall_runs`

 Install an inverse run in the quotient bank and perform the remaining
arithmetic by the literal finite multiplication machine. 

### `minorQuotient`

 Native result of the two top pencil computations and the quotient call. 

### `minorQuotient_greedy`

 Specialization to the two matrices selected by the greedy scans. 

### `minorQuotient_suffix`

 The monomial-basis ordinal is offset past the independent equation rows. 

### `divide`

 Concrete finite quotient program, with the inverse obtained by binary powering. 

### `divideClock`

 Clock bound for the finite-field division, including inversion and multiplication at the
stated degree and width. 

### `divide_runs`

 Division by the determinant takes polynomial time and preserves both input
scalars and all advised field data. 

### `frame_length`

 At a clean field boundary every live limb buffer and the exponent advice
have polynomial length. 

### `machine`

 Concrete Cramer program consuming the two determinant subqueries. 

### `Host`

 Separate frame stacks for the two root calls, and a bank for their field
arithmetic. The quotient reads the two engine result ports directly. 

### `host`

 Combine the denominator engine, numerator engine, and quotient arithmetic into one disjoint
physical bank. 

### `quotientPort`

 Wire the denominator and numerator to the actual output stacks of their
Schur engines. All other quotient ports have their own storage. 

### `query`

 Run the two Schur determinant engines and divide their returned coefficients to obtain the
Cramer coordinate. 

### `query_runs`

 Run both literal determinant engines. At the boundary their returned
scalars are already located at the inverse's base and the multiplier's
numerator, so no field-element copy from the engine output is required. 

### `constantEntries`

 Scalar entry oracle for the constant coefficient matrix of a pencil. 

### `depth`

 Depth allowance for a top-degree Schur query on an `r` by `r` minor. 

### `clock`

 Bound the determinant's instruction count using its descriptor-tree arity, depth, and
per-step cost. 

### `space`

 Bound the peak stack height of the determinant engine, including suspended frames and the
entry reader. 

### `entryBank`

 Initialize a determinant query at its top-degree root with an empty stack of suspended
frames. 

### `resultBank`

 The determinant engine's return configuration holds its scalar answer and an empty stack of
frames. 

### `topPencil_runs`

 Install the bounded Schur engine at the top pencil coefficient. Its result is
already encoded at the limb width used by the field arithmetic routines. 

### `native_runs`

 Instantiating the two Schur calls, the concrete inverse and the final
multiplication gives the packed Cramer quotient with a common polynomial
space cap. The two ready auxiliary banks are returned separately. 
