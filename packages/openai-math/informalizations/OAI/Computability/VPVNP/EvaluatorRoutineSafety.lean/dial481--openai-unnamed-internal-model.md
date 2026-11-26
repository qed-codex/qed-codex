---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRoutineSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutineSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRoutineSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Time and space contracts for evaluator routines

A caller may reserve a continuation after a subroutine's clock bound. Every
branch either halts inside the subroutine or returns with an encoded output
and the reserved clock. The space predicate holds at every active instruction.


### `Bounded`

 A routine contract that maintains the stack safety predicate at active instructions and
preserves the caller's reserved fuel upon a normal return. 

### `Bounded.of_runs`

 A deterministic prefix satisfies the all-branch contract when every
intermediate active state satisfies the storage invariant. 

### `Bounded.of_runs_with_room`

 An explicit polynomial clock on a deterministic call also bounds the
increase in the length of each stack along every prefix. 
