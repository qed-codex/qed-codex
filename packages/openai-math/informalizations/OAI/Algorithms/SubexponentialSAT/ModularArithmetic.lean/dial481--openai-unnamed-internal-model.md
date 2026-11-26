---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ModularArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary long division with finite-bit operations

The executable functions below inspect Bool/list constructors only: they do not
call Nat division, multiplication, comparison, or subtraction on encoded values.
Natural arithmetic appears solely in specifications and event-count proofs.
The event count is not asserted to be a primitive Turing-machine runtime.


### `differenceBit`

 One complete binary subtraction cell. 

### `subCarry`

 Fixed-width subtraction. Its specifications require equal input widths.
The unmatched cases only make the executable function total. 

### `padTo`

 Copy the given bits into a word with the requested shape, adding zero
bits at the most significant end. No lengths are calculated by the routine. 

### `shiftReduce`

 Shift the current remainder, then use one fixed-width subtraction and
its final borrow bit to select the new remainder. 

### `reduce`

 Long division processes the most significant input bit first by recursion
on the tail of a little-endian word. The remainder width grows harmlessly. 

### `reduce_correct`

 Correct modular reduction, proved without Nat division in the algorithm. 

 A measured finite-control subtraction transducer. 

### `subStep`

 One transition reads two bits, changes one Boolean register, and pushes
one bit. It never evaluates the natural number represented by a stack. 

 Instrumentation with events carrying only finitely many Boolean values.
The logs record every padding/subtraction cell and each shift/selection.
They are not a primitive-machine simulation certificate. 

### `subEvents_trace`

 The subtraction portion of the logged execution is an actual measured
trace, of exactly the event count, of the finite-control transducer. 

### `reduceLogged`

 A complete binary-reduction execution with its finite-operation log. 

### `reduceLogged_count`

 Exact count: m padding cells, then two scans and two finite operations
for each input bit. Remainder width grows by one bit at each stage. 

### `reduceLogged_count_le`

 A quadratic bound in a common input-word width. This counts concrete
finite-operation events, not assumed unit-time arithmetic on Naturals. 

 Modular addition and multiplication combine the concrete binary
arithmetic runs with the concrete long-division run. 

 An explicit finite ring expression for geometric correction. Its
operation-node count is a ring-operation bound, separately from bit costs. 

### `geometricExpr`

 Horner evaluation avoids separately constructing all the powers. 

### `inverseExpr_operations`

 The explicit inverse expression uses exactly 4μ+1 ring operations. 

### `inverseExpr_multiplications`

 Of those operations, exactly 2μ+1 are multiplications. 
