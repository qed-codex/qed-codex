---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeTrialPrep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeTrialPrep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeTrialPrep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete workspace preparation for a primality trial

The ambient machine has nine Boolean registers and ten Boolean stacks. Stack
5 holds the divisor, stack 7 the loop fuel, stack 8 controller scratch, and
stack 9 a preserved copy of the candidate. Register 8 is the primality flag.

Preparation clears stacks 0--4 and 6, then copies stack 9 to stack 6 through
the empty scratch stack 1. The lifted divisibility routine operates on stacks
0--6. Every operation below is compiled from actual finite bit instructions.


### `prepared`

 The expected division workspace, retaining all controller data. 

### `install`

 Install the seven-stack subroutine state, framing the three controller
stacks. This is a proof-level configuration map, not a machine instruction. 

### `prep_execution`

 Total finite execution, even for a zero-valued divisor. The numerical
modulo interpretation is refined below under the usual positive-divisor premise. 

### `prep_correct`

 Numerical correctness for the positive divisors used by the prime loop. 

### `prep_post`

 Every execution of the concrete body has the same postcondition, not only
the witness chosen by the existence proof. 

### `trialBound_le_uniform`

 Polynomial bound in the maximum incoming word length. Clearing arbitrary
dirty work stacks is included in this bound. 

### `prep_primitive_execution`

 Actual primitive-tape execution of the composed preparation and trial,
including the compiled command's final halt. 
