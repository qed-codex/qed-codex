---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFactorCountSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorCountSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFactorCountSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving setup of a factor-local assignment count

The fixed program copies a unary arity, counts the copy into a binary exponent,
and invokes the actual preserving power routine.  The base and unary arity are
retained verbatim.  The number of bits in either input is runtime data.


### `length_eval`

 The copied unary input is consumed, with the binary count in port 2. 

### `count_eval`

 A reusable preserving unary-to-binary counter, with only three initially
empty assigned work/output stacks. All other caller stacks are arbitrary. 

### `budget`

 A polynomial in the base width and unary arity, including all setup calls. 

### `setup_eval`

 The only changed stacks are the binary exponent and the binary fuel.
Every work stack is restored to its initial empty state. 
