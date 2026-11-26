---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SAT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SAT.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SAT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete finite CNF syntax and semantics for the candidate SAT argument. 

### `Literal`

 `positive = false` represents a negated variable. 

### `width`

 Maximum literal count of a clause; the empty formula has width zero. 

### `Clause.IsTautology`

 A clause containing both polarities of a literal. 

### `absorb`

 Keep exactly the clauses having no strict subset among the clauses of `F`. 

### `bruteForce`

 An actual finite exhaustive search. No fast runtime claim is attached to this definition. 
