---
{
  "module": "OAI/Computability/VPVNP/EvaluatorMonomialSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMonomialSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMonomialSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A fixed stack control for the monomial query schedule

The only two callbacks in this control are matrix-entry steps. Every other
instruction, from addressing the compact binary digit to advancing the row or
column, is the same at every exponent width. The continuation effect equals
the ordered sequence of index choices in the paper's digit program.


### `machine`

 Finite scheduler code parametrized solely by its two matrix-step subroutines. 

### `budget`

 This instruction budget permits both matrix steps to use variable time
on different index paths. 

### `LabelCallback`

 The label step preserves its current binary counter while updating the
payload by the matrix-index choice. 

### `machine_realizes`

 With the two matrix-step semantics, the stack program realizes the
chronological action sum at every clock covering its explicit bound. 
