---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpBasePUnranking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBasePUnranking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBasePUnranking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual base-p digit extraction

A digit is obtained by the checked binary long-division program. Its remainder
is copied to the fixed width of the modulus, while the padded high bits are
removed. Repeated extraction uses the quotient as the next rank. The modulus,
arity, and all widths are data; the instruction table is fixed.


### `digit`

 Fixed-width little-endian digit returned by one division. 

### `high_bits_zero`

 The discarded high bits are zero when the modulus is positive. Their
removal is therefore justified rather than a truncation approximation. 

### `digitWords`

 Least-significant base-p digit first; each digit itself is little-endian. 

### `tapes`

 Division workspace 0--7; arity counter8; copied width9; transfer scratch10;
reversed digit stream11; final forward digit stream12. 

### `collectDigit`

 Fixed-width digit extraction and quotient preparation after long division.
The digit is prepended in reverse to a stream that is reversed once at the end. 

### `extractionStep_eval`

 One complete division/extraction step, including actual fixed-width copying
and restoration of the quotient as the next working rank. 

### `loop_eval`

 The runtime unary arity controls a fixed while loop. Division changes the
rank value but preserves its padded bit width, so each iteration has one common
explicit bound. 

### `budget`

 Explicit cost including all divisions, digit extraction, loop tests, final
stream reversal, and halt. 

### `command_eval`

 A real execution materializes all fixed-width digit records. The result is
least-significant base-p digit first, with little-endian bits inside each record. 

### `program_runsIn`

 The checked fixed program implements runtime-arity base-p unranking. 

### `control_size`

 The same finite table is used for every modulus, rank width, and arity. 

### `program_unranks`

 Combined machine-and-value contract for an in-range local table rank.
Every output record has the modulus's fixed bit width and denotes a valid field
label; the quotient after the requested arity has value zero. 
