---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable pieces of prime trial division

The numeric trial-division functions in the first section are specifications.
They are never instructions of a program. The executable zero test and Boolean
accumulator below contain only existing finite Boolean-stack instructions.
Candidate numbers, divisors, and remainders are runtime data.


### `eval_result_unique`

 Actual structured executions have a unique final data state.  The proof
uses the verified compiler and deterministic terminal configurations. 

### `eval_steps_unique`

 The exact instruction count of a terminating structured execution is
unique as well as its result. This allows proved execution bounds to be used
for every actual occurrence of a subroutine in a larger trace. 

### `trialFactors`

 Mathematical specification of testing a consecutive interval of divisors. 

### `trialPrime`

 Specification of complete trial division, including zero and one. 

### `trialPrime_eq_primeTest`

 This identifies the trial-division specification with the old schedule's
prime predicate; it does not identify a numeric function with executable code. 

### `scan_trialPrime_eq`

 Replacing the schedule's decidable predicate by the explicit finite divisor
scan preserves its mathematical prime-search result. 

### `zeroState`

 Data state of the existing binary zero-test subroutine. 

### `zero_terminal_trace`

 Complete zero-test trace, including its return/halt instruction, valid
for arbitrary incoming Boolean work registers. 

### `zeroCheck`

 Fixed finite zero-test program assigned caller-chosen, fixed ports. 

### `recordTrial`

 Accumulate one trial result. A zero remainder makes the prime flag false.
Both Boolean operations and the zero-test call are concrete instructions. 

### `recordTrialResult_flag_nondivisor`

 If the preceding actual remainder subroutine establishes its usual value
contract, this concrete accumulator records exactly nondivisibility. 

### `recordTrial_primitive`

 The verified accumulator has an actual primitive execution through the
proved compiler; this conclusion contains no assumed compilation certificate. 

### `divisionRegister`

 Division uses eight work registers; register eight is the caller's
primality accumulator and is outside the division program's register image. 

### `divisibilityTrial`

 A complete executable trial: binary remainder followed by the preserving
zero scan and update of the caller's primality accumulator. 

### `divisibilityTrial_correct`

 The program executes a genuine division on the supplied bit strings.
The modulus and input sizes are data, and all instruction tables remain fixed. 

### `divisibilityTrial_execution`

 Total execution contract, including a zero-valued modulus.  The numeric
remainder interpretation requires a positive modulus, but finite execution does
not: it is established directly by the concrete binary reduction program. 
