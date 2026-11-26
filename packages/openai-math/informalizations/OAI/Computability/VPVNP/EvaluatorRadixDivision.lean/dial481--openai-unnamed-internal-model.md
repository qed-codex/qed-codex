---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRadixDivision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixDivision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRadixDivision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary-to-radix conversion for the streamed evaluator

The input exponent is a most-significant-bit-first binary stack. A fixed
restoring division table handles a divisor of any positive value, independently
of the dividend width. One division round returns the quotient in the original
input format and prepends a divisor-width little-endian remainder to the digit
stack. The loop count is supplied on a unary stack. Hence the output starts
with the most significant requested digit, including leading zero digits.


### `Port`

 The restoring-division registers, the unary count of remaining divisions and the stack of
accumulated radix digits. 

### `reverseOnto`

 The control consumes the source in head order, pushing onto the destination. 

### `bank`

 The machine's integer inputs and scratch are precisely the division word
ports. The counter and the growing digit string belong to the caller's loop. 

### `ready`

 The bank at a division-round boundary, containing the reversed dividend, divisor,
remaining-round tally and accumulated digits. 

### `digitRoutine`

 One radix-conversion round. Divide the dividend, install the quotient for the next round
and prepend the remainder bits to the digit stack. 

### `divide_spec`

 Positive-divisor division accepts arbitrary, possibly unequal widths. 

### `digitTicks`

 One complete divide-and-emit pass, measured in elementary bit instructions. 

### `radixDigits`

 A fixed number of base-`Q` digits, ordered from the most to the least
significant, as in the Frobenius evaluator. 

### `radixDigits_eq`

 The digit in place `j` is the residue of the quotient by `Q ^ j`. The
stack exposes the highest place first. 

### `encodedDigits`

 Fixed-width little-endian encoding of each digit, concatenated without
separators. A reader knows the field width from the divisor. 

### `radixRoutine`

 Positive counter marks launch a divide-and-emit pass. Empty input to
the loop returns immediately. 

### `radixTicks`

 Instruction count for the specified number of restoring-division rounds on a z-bit dividend
with a w-bit divisor. 

### `radixRoutine_runs`

 Exact normal return of the fixed finite routine. It preserves the divisor,
retains the high quotient after the requested rounds, and emits exactly one
fixed-width binary block per round. 

### `full_radixRoutine_runs`

 A full input bit width of base-`Q` rounds suffices whenever `Q ≥ 2`.
Every such run leaves a zero quotient and all the digits of the exponent. 
