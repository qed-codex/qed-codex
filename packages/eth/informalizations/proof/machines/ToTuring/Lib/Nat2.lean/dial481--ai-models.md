---
{
  "module": "proof/machines/ToTuring/Lib/Nat2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Nat2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for binary numbers: product, quotient, remainder, powers. Product, quotient and
remainder are each one fold
over the binary digits, and a power with a unary exponent is one fold over a list of that length. In
every round the
intermediate values grow by at most a polynomial in the length of the input. 

 ### Lengths of sums, doubles and products 

### `len_dbl_add_le`

 The word of c + c + z is longer than those of c and z together by at most 4. 

### `len_le_of_le_dbl`

 A number that is at most 2c + 1 has at most one binary digit more than c. 

### `len_mul_le`

 The word of a product is at most as long as the words of the factors together. 

 ### Product 

### `foldr_bits_mul`

 The product, read off the binary digits of the second factor from the top: double, and add m if
the digit is 1. 

### `mul`

 The product of two numbers in binary is polynomial-time. 

 ### Quotient and remainder 

### `divStep`

 One round of the division by d taught at school, in base 2: s is (quotient, remainder) of the
digits read so far, b is the
next digit. 

### `divStep_spec`

 A round takes quotient and remainder of n to those of 2n + b. 

### `foldr_bits_divStep`

 The rounds over all digits of n, from the top, give quotient and remainder of n. 

### `len_divStep_le`

 A round makes the word of the pair longer by at most 6. 

### `divFold`

 Quotient and remainder together, as one fold. 

### `div`

 The quotient is polynomial-time; the divisor 0 is a separate case (the quotient is then 0). 

### `mod`

 The remainder is polynomial-time; the divisor 0 is a separate case (the remainder is then the
number itself). 

 ### Powers 

### `pow_const`

 A power with a fixed exponent is polynomial-time: k products. 

### `foldl_replicate_mul`

 Multiplying n times by b multiplies by b ^ n. 

### `pow_unary`

 A power is polynomial-time if its exponent can be written in unary: every round makes the word
longer by at most the
length of the word of the base. 

### `two_pow`

 The case of `pow_unary` with base 2. 

 ### a / b ^ q with q in binary 

### `foldl_count_min`

 Counting up to q along a list. 

### `unary_min_length`

 The smaller of a number in binary and the length of a list can be written in unary. 

### `div_pow_min_size`

 In a / b ^ q the exponent may be cut off at the number of binary digits of a. 

### `div_pow`

 a / b ^ q is polynomial-time with all three numbers in binary: the exponent is first cut off at
the number of binary
digits of a, which can be written in unary. 
