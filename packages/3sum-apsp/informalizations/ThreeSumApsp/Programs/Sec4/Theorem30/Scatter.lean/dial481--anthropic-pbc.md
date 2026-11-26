---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Scatter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Scatter.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Scatter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A string put at the levels of the inner set

Proof of Theorem 30: a query forms each leaf or box "from the private leaf".  The output string is
the list of its L digits, and the levels of its inner set are the positions of the digit 9.  The
routine copies this list and replaces its digits 9, from the left, by the digits of a second string
(`Spec.scatter`).  If star = 1, the leading digits 9 of the second string (the levels of F_V,
Section 4.2) are written as stars (`Spec.starRunIf`).

One pass, with a pointer into the second string and a flag that says whether the leading run of
nines is still going on.  `Scatter.scatter_step` says what the first digit of
`scatter w (starRunIf flag s)` is and how the rest looks, in terms of the digit, the flag and the
pointer that the program computes (`outDigit`, `nextRun`, `nextPtr`); `Scatter.round_runs` says
that a round of the program computes them.  The invariant (`Scatter.Inv`) is that the digits written
so far, followed by what is still to be written, are the whole string.


 ## One more digit 

### `outDigit`

 The digit written at a position where the first string has x and the pointer is at a digit y of
the second string; run = 1 says that the leading run of nines is still going on. 

### `nextRun`

 The flag after that position: a digit other than 9 of the second string ends the run. 

### `nextPtr`

 The pointer after that position. 

### `scatter_step`

 The first digit of what is still to be written, and the rest. 

### `Progress`

 After i positions: the digits written so far, the flag and the pointer. 

### `Progress.ptr`

 The pointer has passed one digit for each nine of the first string. 

### `Progress.rest`

 The digits written, followed by what is still to be written, are the whole string. 

### `Progress.ptr_lt`

 At a nine of the first string the pointer is inside the second string. 

### `Progress.succ`

 One more position: the digit, the flag and the pointer are those that the three functions
give. 

 ## The program 

### `First`

 The local variables of scatter: the arguments (the addresses of the two strings and of the
copy, the length, and the flag, whose first value is the argument star), the position, the pointer
into the second string, and the digit to be written. 

### `scatterRound`

 One round: read a digit of the first string; if it is a nine, take the next digit of the second
string in its place, as a star if it is a nine of the leading run; write the digit, and go on. 

### `scatterBody`

 scatter(first, second, dst, len, star): copy the first string, with the digits of the second
string in place of its nines.  The locals that are not arguments start at 0. 

### `round_runs`

 What a round does, for the digit x of the first string and the digit y of the second string at
the pointer. 

### `Inv`

 Before round i the first i digits have been written at out. 

### `scatter_spec`

 **scatter** writes `Spec.scatter wl (starRunIf star sl)`. 
