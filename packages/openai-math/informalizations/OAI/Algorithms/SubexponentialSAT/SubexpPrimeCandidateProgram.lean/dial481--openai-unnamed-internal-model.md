---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeCandidateProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeCandidateProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeCandidateProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Calling the primality test inside the candidate search

The inner test uses nine Boolean registers and ten stacks. The outer search
adds two stacks for its remaining count and scratch. The wrapper assigns the
inner stacks to the first ten positions and preserves the outer two positions.
The candidate remains on stack 9 and the test result is register 8.


### `callInner_eval`

 Actual subroutine traces lift with exactly the same source-step count. 

### `candidateTest`

 This is the fixed compiled primality test, with two additional framed
stacks for the outer first-success controller. 

### `candidateTest_execution`

 Total execution of a closed primality test. The original candidate and
both outer controller stacks survive the invocation exactly. 

### `candidateTest_correct`

 Numeric correctness on the candidate interval used by prime search. 

### `candidateTest_trace`

 Source-level trace of the fully closed candidate body. 

### `candidateTest_primitive_execution`

 Compiler-derived primitive execution; no polynomial or asymptotic
prime-search bound is asserted by this existential step-count theorem. 
