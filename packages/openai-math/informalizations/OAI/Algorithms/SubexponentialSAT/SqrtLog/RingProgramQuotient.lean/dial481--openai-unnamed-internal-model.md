---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramQuotient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramQuotient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramQuotient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual represented arithmetic in the quotient by a supplied monic
polynomial. Irreducibility is unnecessary for ring operations. Every structure
constant is supplied by the executable companion recurrence. 

### `quotientRing`

 This is arithmetic for every supplied monic polynomial. A separate finite
irreducible search upgrades this quotient to the intended unramified ring. 

### `quotientProgram`

 The executable program contains no polynomial-quotient or choice operation. 

### `quotientProgramRun`

 Explicit setup phase. Its returned program retains the materialized table,
and its cost includes all scalar callback events in constructing that table. 
