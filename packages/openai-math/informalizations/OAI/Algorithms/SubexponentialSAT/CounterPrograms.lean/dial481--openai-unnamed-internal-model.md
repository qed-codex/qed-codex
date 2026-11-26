---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CounterPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable binary counters on Boolean stacks

The head of a stack is the least-significant bit.  Leading zeroes are allowed:
there is no hidden normalization precondition, and zero testing scans the bits.
The arithmetic functions below specify the results of finite instruction-table
programs; the machine execution theorems appear after the specifications.


### `value`

 The unsigned value of a little-endian Boolean stack. 

### `value_eq_toNat`

 Compatibility with the arithmetic module's identical little-endian convention. 

### `ripple`

 The same finite carry/borrow control works in both directions.  `true` is
increment; `false` is decrement, whose value contract requires positive input. 

### `isZero`

 A direct finite Boolean zero test, valid even for noncanonical encodings. 

### `counterRegs`

 Three fixed Boolean registers: current bit, presence bit, and an accumulator. 

### `counterStacks`

 The value stack and one scratch stack; neither stack is part of finite control. 

### `rippleProgram`

 Eleven fixed labels implement carry/borrow and scratch restoration.
The `carry` parameter is a fixed program bit, not an unbounded control value. 

### `ripple_restore_trace`

 Exact instruction count of the complete scratch-restoration loop. 

### `rippleCost`

 Exact instruction count, ending at the halt label before executing halt. 

### `ripple_trace`

 Complete program correctness, allowing arbitrary initial scratch contents.
The old scratch contents are restored to the front of the result in reverse. 

### `increment_runs`

 Increment has an actual finite-table trace and a linear instruction bound. 

### `decrement_runs`

 Decrement executes the same fixed-size table; the positivity precondition
is needed only for its arithmetic interpretation. 

### `ripple_terminal_trace`

 Complete execution from the language's actual input convention through halt. 

### `zeroProgram`

 A ten-label zero test. It preserves the data stack, clears scratch, and
returns its answer in Boolean register 2. 

### `zero_scan_trace`

 Exact trace through scan and restore, preserving every scanned data bit. 

### `zero_trace`

 The zero-test answer, counter preservation, scratch clearing, and cost are
all witnessed by a trace of the executable finite instruction table. 

### `relabelInstr`

 Specialization of the shared linker to identical data ports. 

### `relabel_trace_to_exit`

 The actual shared linker transfers the trace ending before the exit instruction. 

### `countdownProgram`

 A bounded countdown loop. Labels 0--9 test the counter, 10--19 decrement
it, label 20 is the iteration boundary, and label 21 is the exit. 

### `countdown_iteration`

 One positive iteration is a measured trace of the combined table, and
strictly decreases the binary counter while preserving its width. 

### `countdown_runs`

 The bounded loop really terminates after repeatedly decrementing its input
counter. Its runtime is polynomial in the binary width and numeric loop bound;
the bound itself is data on the stack, never a program label or register. 

### `boundedCounterLoop`

 Reusable bounded-counter loop rule for an arbitrary actual finite program.
The hypotheses are local measured executions (zero exit and one positive
iteration), not a cost annotation for an uninterpreted mathematical function.
The invariant may track any caller work stacks and registers. 

 ## Deriving a binary counter from an input list 

### `lengthStacks`

 Input data, binary count, and increment scratch, all on Boolean stacks. 

### `lengthProgram`

 Count a list by consuming one bit and incrementing a binary stack counter.
The program has fourteen fixed labels; the input length is never in control. 

### `length_accumulate`

 General accumulating count: a pre-existing binary counter gains exactly
one for each consumed input bit. `B` is a proved width bound, not machine state. 

### `length_correct_from`

 The utility accepted by callers whose current value/presence bits are dirty.
Only the accumulator bit must start false; both live data bits are overwritten. 

### `length_correct`

 A fixed finite program produces the binary representation of the raw input
length with a proved polynomial bound on actual primitive source instructions. 
