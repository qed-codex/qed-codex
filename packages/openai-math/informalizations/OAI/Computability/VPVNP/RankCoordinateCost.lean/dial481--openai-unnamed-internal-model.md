---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-depth resource bounds for Appendix D coordinate queries

The augmented row count, its column count and its rank fit under a common
binary size bound. The base scalar reader can have a singly exponential
clock and polynomial stack height. The two prefix scans in a minor entry
access the original matrix and its transpose. The determinant caller visits
these entries one at a time. Repeated calls multiply clocks and share the
maximum of their stack bounds.


### `Budget`

 Time and peak height of a physical stack subroutine. 

### `Budget.time`

 Upper bound on the number of stack-machine instructions in the subroutine. 

### `Budget.space`

 Upper bound on the peak height of its stacks during execution. 

### `Budget.thenRun`

 The two subroutines use the same named bank and return at their boundaries. 

### `Budget.repeated`

 A loop bound multiplies only the time. 

### `Parameters`

 Parameters common to the original rectangular matrix and its Cramer minors.
`bits` bounds the logarithms of both original dimensions. `local` covers the
short Schur actions and the fixed input/output adapters of each scalar read.
`aux` is the maximum initial stack height at those boundaries. 

### `Parameters.bits`

 Common bound on the binary logarithms of the original matrix dimensions. 

### `Parameters.addr`

 Bit width of addresses used for matrix entries and suspended frames. 

### `Parameters.limb`

 Bit width of one base-field coefficient in the packed scalar representation. 

### `Parameters.degree`

 Extension degree, hence the number of base-field coefficients in a scalar. 

### `Parameters.localWork`

 Allowance for short Schur actions and the entry reader's setup and return steps. 

### `Parameters.aux`

 Maximum initial height of auxiliary stacks at the reader's call boundaries. 

### `descriptor`

 Running a bounded number of sequential scalar reads within a descriptor,
with short setup and teardown. The caller's suspended frames are included in
its initial height. 

### `gramDescriptor`

 A Gram entry requires at most two underlying rectangular entry reads. 

### `gramDescriptor_covers`

 The actual weighted-Gram descriptor and all saved stack frames fit this
budget whenever the short-action allowance covers its register overhead. 

### `singleDescriptor_covers`

 A constant-matrix descriptor reads one selected entry. Its signed-entry
adapter may spend a short additional allowance. This checks the time and
peak-height formulas of the actual Schur description routine. 

### `rankScale`

 Sum the dimension bit bound, the ceiling binary logarithm of descriptor time, the local
work allowance, the address and limb widths, and the field extension degree to bound
rank-query time. 

### `rank`

 Common envelope for every rectangular prefix in either orientation. 

### `rank_covers`

 The actual clock and cap from the rectangular rank control fit the envelope. 

### `arithmetic`

 Bound for one arithmetic register operation, with its initial word already in place. 

### `prefixScan`

 The prefix tester computes the next length, requests its rank, compares with
the ordinal, then advances its cursor. This is the clock of `PrefixWords.machine_runs`
at the largest permitted prefix. 

### `dimension`

 Two independent rank calls followed by subtraction. 

### `suffix`

 Compute the combined ordinal, perform the row scan and remove the equation prefix. 

### `minorEntry`

 Recompute the row and column indices independently, then read either
the original entry or the replacement entry of the target row. 

### `determinant`

 A Schur determinant call on a minor, charging entry time and space separately. 

### `divide`

 The inverse and multiplication stage has polynomial clock and can pay this
entire clock in space on top of its small input bank. 

### `cramerDescriptor`

 Reserve the quotient workspace already in the determinant contract. This
makes the post-determinant room hypothesis of `Cramer.SchurPair.native_runs`
hold even for a one-dimensional minor. 

### `coordinate`

 Complete fixed-depth scalar query. The suffix lookup locates the input
monomial. Its offset and the two prefix ranks also supply the output ordinal
and dimension. Both determinant subcalls use the same per-entry envelope. 

### `cramer_covers`

 The joint determinant and division cost in the native Cramer theorem.
The common cap also supplies room for division after both engines return. 

### `LogBound`

 The ceiling of the base-two logarithm of the budget is eventually bounded by a polynomial
in the input size. 

### `forShape`

 Any concrete matrix with these dimensions fits the common shape.
The allowance includes the cost of formatting a weighted Gram entry. 

### `Feasible`

 Feasible clocks and caps are measured on different scales. 

### `Small`

 The word widths, logarithmic matrix shape, and short-action allowance
are polynomially bounded in the input length. 

### `feasible_coordinate`

 Composition covers both expensive scans in each minor without placing any
exponential clock in a space bound. 

### `coordinate_time_space`

 A single polynomial exponent bounds the complete clock, and a separate
polynomial bounds the peak space. Both hold uniformly at every length. 

### `forSlice`

 Instantiate the two matrix dimensions from the actual graded Macaulay
enumeration. The row count includes the equation prefix and the monomial suffix. 
