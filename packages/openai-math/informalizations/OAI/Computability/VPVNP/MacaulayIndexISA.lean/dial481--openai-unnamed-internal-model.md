---
{
  "module": "OAI/Computability/VPVNP/MacaulayIndexISA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayIndexISA.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayIndexISA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed register program for a dense monomial ordinal

The program enumerates raw graded radix keys in increasing order. At a key it
divides the exponent block by its radix exactly once per label and tests the
digit sum against the outer degree. A selected ordinal returns the raw key.
With the requested ordinal equal to the upper scan limit it returns the count
instead. The instruction table and number of registers are independent of the
degree bound and the number of variables.


### `table`

 The read-only registers, followed by cursor, count, remaining digits,
residual value, digit sum, scratch, one and zero. 

### `Parameters`

 The lower and upper radix blocks fit in one register each. 

### `Parameters.base`

 Radix for the digits encoding individual variable exponents. 

### `Parameters.arity`

 Number of variables and hence the number of digits inspected in each candidate key. 

### `Parameters.box`

 Size of the low radix block. Division by this value recovers the total-degree tag. 

### `Parameters.limit`

 Exclusive upper bound on the raw keys visited by the monomial scan. 

### `Parameters.ordinal`

 Zero-based rank of the valid monomial to return. Using the scan limit as the requested
  rank makes the program count all valid keys. 

### `Work`

 Mutable register values of the scan through graded monomial keys. 

### `Work.cursor`

 Raw key currently under consideration, or the exclusive endpoint after exhausting the
  scan. 

### `Work.count`

 Number of valid keys strictly below the cursor. 

### `Work.remaining`

 Number of variable digits still to examine for the current candidate. 

### `Work.value`

 Unprocessed suffix of the candidate's low radix block, divided by the radix after each
  digit. 

### `Work.total`

 Sum of the variable exponent digits examined for the current candidate. 

### `Work.scratch`

 Temporary register for an extracted digit or the total-degree tag used in the final
  comparison. 

### `word`

 Encode a natural number as a register word modulo two to the power w. 

### `registers`

 Lay out the five scan parameters, six work values, one and zero in the thirteen hardware
registers. 

### `Trace`

 Execution of the graded-key scanner for exactly n instructions between the two indicated
control locations and register configurations. 

### `digitSum`

 Sum the indicated number of least significant base digits, counting leading zeros if
necessary. 

### `Fits`

 Width conditions for the scalar scans and the digit-sum comparison. 

### `validKey`

 A raw key is accepted precisely when the digit sum of its low block equals the total degree
in its high block. 

### `Result`

 The return address is either the end of the range or the valid raw
address whose exclusive prefix count equals the requested ordinal. 

### `scan_physical`

 The actual bit-stack control has polynomial height even when the
number of raw addresses scanned is exponential. 

### `graded`

 The concrete register input for a graded key scan. 
