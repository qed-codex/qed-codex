---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRadixRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed radix-digit rows for all label exponents

The machine reads one fixed-width binary exponent per row, in descending
label order. Each field is most-significant-bit-first. It prepends the radix
digits of each exponent to the output. Thus the finished table is ordered by
increasing label, with the most significant digit first in each row.

A unary width counter is spent during extraction to build the radix round
counter. The quotient produced by the division has the original width, so
clearing its bits restores the width counter for the next exponent.


### `Port`

 The packed exponent input, unary row and width counters and the radix-conversion register
bank. 

### `ready`

 The ready state between rows has no pending quotient or rounds. 

### `rowTicks`

 Instruction count for extracting one z-bit exponent and converting its z requested radix
digits using a w-bit divisor. 

### `radixRows`

 The loop consumes one unary mark per binary exponent field. 

### `rowsTicks`

 Instruction count for converting the specified number of exponent rows, including the
row-counter updates and final exit. 

### `packedInput`

 Source rows are supplied by descending label and highest binary bit first. 

### `packedTable`

 Destination rows are ordered by ascending label, then descending radix
place. Within each digit the bits are little-endian. 

### `radixRows_runs`

 All rows of the exponent table are converted by the same finite code.
The input suffix, the original divisor and the width counter are preserved.
All intermediate stacks are empty on return. 

### `packedTable_cell`

 Lookup at row `i`, column `j` returns the encoded digit for power
`z - 1 - j`. The suffix can carry any data already on the table stack. 

### `packedInput_eq_reverse`

 Reversing the RAM's ascending, little-endian binary word stream puts
both the rows and their bits into the input order of the conversion loop. 

### `nativeRows`

 Entry point when the RAM's binary exponents are already on a separate
stack in increasing label order. The saved-candidate stack of the division
kernel is available to receive this stream before the first divide. 

### `native_array_runs`

 Conversion directly from the serialized exponent array on a cut, using
the same word-array equivalence as the RAM transcript. 

### `radixRows_space`

 Peak total bit storage during the whole table conversion is polynomial in
the number of labels and the two binary widths. The input suffix and any
previously accumulated digits are included in the bound. 
