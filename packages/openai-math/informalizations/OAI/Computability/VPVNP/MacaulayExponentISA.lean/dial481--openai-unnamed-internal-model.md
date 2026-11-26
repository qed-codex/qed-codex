---
{
  "module": "OAI/Computability/VPVNP/MacaulayExponentISA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentISA.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayExponentISA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed binary control for a shifted coefficient row

The two input words hold the exponent blocks of the source monomial and
the coefficient column. They can use different radices. The program checks
every coordinate, reports equality and divisibility, and returns any requested
digit of the residual. Marking one label before scaling covers multiplication
by that label. A scalar multiplier also covers the Frobenius query.


### `Parameters`

 Input registers store the source radix, column radix, multiplier, marked
coordinate and requested coordinate. Both coordinates use one-based numbers,
with zero disabling the mark or the requested output. 

### `Parameters.sourceBase`

 Radix used to extract a variable exponent from the source monomial. 

### `Parameters.columnBase`

 Radix used to extract a variable exponent from the column monomial. 

### `Parameters.scale`

 Factor applied to each source exponent after adding the possible one-variable shift. 

### `Parameters.mark`

 One-based coordinate at which to increase the source exponent by one before scaling. Zero
  disables the shift. 

### `Parameters.request`

 One-based coordinate of the exponent difference to retain. Zero requests no output digit. 

### `Work`

 Register values maintained while comparing the shifted and scaled source exponents with the
column exponents. 

### `Work.remaining`

 Number of exponent digits still to compare. It also gives the one-based coordinate of the
  next low radix digit. 

### `Work.source`

 Unprocessed part of the source radix block after removing the low digits already visited. 

### `Work.column`

 Unprocessed part of the column radix block after removing the low digits already visited. 

### `Work.residual`

 Stored column exponent minus the shifted source exponent at the requested coordinate,
  truncated at zero. 

### `Work.divides`

 Running conjunction of the coordinatewise inequalities needed for the shifted and scaled
  source monomial to divide the column. 

### `Work.same`

 Running conjunction of the exponent equalities for the shifted and scaled source and the
  column. 

### `Work.sourceDigit`

 Current source exponent after the optional one-coordinate shift and scaling. 

### `Work.columnDigit`

 Current exponent extracted from the low digit of the column block. 

### `registers`

 Registers 5--12 hold the work record, and the last two hold one and zero. 

### `table`

 Fixed 18-instruction register table that compares the two exponent blocks and retains the
requested residual digit. 

### `Fits`

 Constraints used at the physical arithmetic and comparison instructions. 

### `Trace`

 Execution of the exponent-comparison table for exactly n steps between the two indicated
control locations and work records. 

### `scaledDigit`

 Extract the low source digit, add one when the coordinate is marked, then multiply by the
query's scale. 

### `run_digits`

 The scalar row test, including the returned exponent at one arbitrary
label, runs on a fixed binary stack machine. 
