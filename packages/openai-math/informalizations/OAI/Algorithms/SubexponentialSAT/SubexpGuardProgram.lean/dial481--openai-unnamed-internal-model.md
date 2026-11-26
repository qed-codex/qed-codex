---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpGuardProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGuardProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGuardProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete binary guard control for the subexponential schedule

The comparator below has a fixed instruction table, reads arbitrary-width
little-endian binary words, and uses only Boolean operations and stack pops.
Schedule arithmetic is not an instruction of this program.


### `carry`

 Borrow propagation with implicit high zero bits. 

### `carry_iff`

 The final borrow is the strict comparison, even for unequal word lengths. 

### `program`

 Eight one-bit registers, two stacks, and twelve fixed labels. Register zero
is the result; both operand stacks are consumed. Entry resets the borrow bit. 

### `round_trace`

 A concrete nonterminal round, including its branch instruction. 

### `loop_trace`

 Exact instruction count for the data-dependent loop. 

### `run`

 Complete comparator contract. Leading zero bits and unequal widths are allowed. 

### `restrictState`

 Restrict caller data to the fixed ports of a subroutine. This is assertion
notation, not an instruction available to the program. 

### `compare_call`

 A measured comparison call on fixed injective ports, with every other
caller register and stack preserved. 

### `workRegister`

 The accumulator lives outside the comparator's eight work registers. 

### `checkPair`

 Compare one pair, invert strict-less, and conjoin the result into register 8. 

### `checkPair_eval`

 Concrete comparison-and-accumulation contract. Pair operands are consumed;
all other stacks, including a caller's retained copies, are preserved. 

### `guard`

 Fixed control: initialize the accumulator and check the three numeric pairs. 

### `guard_eval`

 All three numeric comparisons execute as one fixed structured program. 

### `EncodesChecks`

 The caller supplies already-computed binary encodings of the five numeric
quantities and the constant 32. This is a data relation, never an instruction. 

### `guardPass_iff_ready`

 The bit produced by the concrete guard is precisely the source readiness
predicate, once the independently computed numeric operands are represented. 

### `dispatch`

 Both continuations are actual structured programs; the test is one actual
Boolean branch instruction after executing the numeric guard. 

### `guard_primitive_execution`

 Compilation yields an actual primitive execution between the corresponding
encoded internal configurations, with fixed program-dependent overhead. 

### `loadThirtyTwo`

 Eight physical instructions write the little-endian word for 32. 

### `earlyGuard`

 The first guard can run before the remaining schedule arithmetic. 
