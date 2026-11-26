---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeSearchProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeSearchProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeSearchProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite-control prime trial enumeration

The trial body is the concrete binary division, zero scan, and Boolean update
from `SubexpPrimeTrialPrep`.  No semantic primality predicate is an instruction.
The divisor and remaining count are little-endian binary words on stacks 5 and
7; stack 9 retains the candidate and register 8 accumulates nondivisibility.


### `trialScan_correct`

 A closed execution theorem: every divisor in the supplied interval is
tested by the actual remainder routine. All program tables have fixed size. 

### `trialScan_prime_correct`

 Complete trial division after concrete data initialization: the flag
decides primality, including the empty divisor interval for candidate two. 

### `primeTestCmd`

 The complete trial-division program includes all binary counter
initialization. Its instruction table is independent of the candidate. 

### `primeTest_execution`

 Total execution on every word, with the candidate preserved. Numerical
primality correctness below concerns candidates at least two. 
