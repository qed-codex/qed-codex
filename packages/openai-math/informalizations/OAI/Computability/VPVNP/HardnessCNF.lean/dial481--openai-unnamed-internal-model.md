---
{
  "module": "OAI/Computability/VPVNP/HardnessCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling a CNF test into a finite query program

The payload assigns one bit to each Boolean variable. Each occurrence of a literal
becomes one read state. A matching literal skips the rest of its clause, and an
exhausted clause goes directly to the rejecting halt.


### `Literal`

 The bit must equal the indicated polarity for this literal to hold. 

### `CNF`

 A list of clauses over `k` Boolean variables. Each clause is a disjunction of signed
literals. 

### `literalCount`

 Number of literal occurrences, counting repetitions within or across clauses. 

### `Satisfies`

 An assignment satisfies the formula when every clause contains a literal whose required bit
matches the assignment. 

### `stateCount`

 The compiler reserves two halting states, then adds one state per literal. 

### `State`

 The query evaluator has one control state per literal occurrence, in addition to its two
terminal states. 

### `Block`

 During assembly of a clause, the first matching literal jumps to `pass`
(the start of the remaining clauses), and exhaustion jumps to `reject`. 

### `eval_push_succ`

 Existing states keep their behavior when a new literal is prepended. 

### `query`

 A query program deciding whether the payload satisfies a CNF. 

### `query_eval_iff`

 At most one query per literal is sufficient, including for formulas with
empty clauses and the empty conjunction. 
