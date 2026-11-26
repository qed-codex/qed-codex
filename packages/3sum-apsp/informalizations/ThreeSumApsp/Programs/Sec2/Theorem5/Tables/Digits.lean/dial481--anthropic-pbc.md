---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Digits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Digits.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Digits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Tables of digits, by an odometer

The programs for Theorem 5 turn the number of a row or of a column into a string ("locate the output
strings", in the proof of Theorem 5), so they need the digits of these numbers in base 3 and in
base 4. digits(n, b, len, dst) writes, for every x < n, the len digits of x % b^len in base b, most
significant first, to the len cells from dst + x * len.  There is no division: row 0 is zero, and
row x + 1 is row x plus one, formed from the least significant digit on with a carry.

* The pure side: `carryInto b j x` is the carry into the place of weight b^j when 1 is added to x,
  defined as the routine computes it, and `placeDigit_succ` says that a place of x plus its carry,
  reduced if it reaches b, is the place of x + 1.
* `digitsPlace_spec` treats one place, `digitsInner_spec` one row, `digitsZero_spec` row 0, and
  `digits_spec` runs through the rows; `digits_entry` is the specification that the callers of the
  procedure assume.


 ## Adding 1 to a number, place by place 

### `placeDigit`

 The digit of weight b^j of x. 

### `carryInto`

 The carry into the digit of weight b^j when 1 is added to x: 1 into the last place, and then 1
as long as the digit plus the carry reaches b. 

### `placeDigit_lt`

 A digit is less than the base. 

### `carryInto_le_one`

 A carry is 0 or 1. 

### `add_carry`

 Adding a carry c to q: the last digit of q grows by c, or becomes 0 and gives a carry. 

### `succ_div_pow`

 The digits of x + 1 from the place of weight b^j on are those of x plus the carry. 

### `placeDigit_succ`

 **One place of the odometer.**  The digit of x + 1 is the digit of x plus the carry, or 0 if
this reaches b. 

### `mod_pow_div_mod`

 The digits below place len do not change when the number is reduced modulo b^len. 

### `getElem_digitList`

 The entry number q of the row of x. 

 ## The program 

### `Total`

 The local variables of digits: Total = n, Base = b, Len = len, Dest = dst (the arguments); Row
is the number of the row being written, Cur its address and Prev the address of the row before it;
Place is the place, Carry the carry into it, and Digit the new digit. 

### `digitsPlace`

 One place of the new row: the digit of the row before it plus the carry, or 0 if this reaches
b; in the second case the carry stays 1. 

### `digitsInner`

 The loop that forms one row from the row before it, from the last place on. 

### `digitsRow`

 One round of the loop over the rows. 

### `digitsZero`

 Row 0 is zero.  The place is not set at the beginning: local variables that are not arguments
start at 0. 

### `digitsBody`

 digits(n, b, len, dst). 

 ## One row from the row before it 

### `Placed`

 The memory after r places of the row of y + 1 have been written to the len cells from cur, from
the last place on; no other cell has changed. 

### `Placed.step`

 One more place. 

### `Inv`

 The state after r places: the place is len - r, and the carry is the carry into place r. 

### `digitsPlace_spec`

 **One place** of the new row is written, and the carry into the next place is formed. 

### `digitsInner_spec`

 **One row**: the loop over the places writes the row of y + 1 to the len cells from cur, from
the row of y in the len cells from prev. 

 ## The loop over the rows 

### `RowsDone`

 The state after the rows 0, …, i have been written: they stand in the table, and no cell outside
the table has changed. 

### `tRow`

 The time of one round of the loop over the rows. 

### `digitsRow_spec`

 **One round of the loop over the rows** writes row `i + 1`, the digits of `i + 1`, from row
`i`. 

### `digitsZero_spec`

 **Row 0** is zero. 

### `digits_spec`

 **digits** writes the table of digits and changes nothing else. 

### `digits_entry`

 **The specification that the callers of digits assume.** 
