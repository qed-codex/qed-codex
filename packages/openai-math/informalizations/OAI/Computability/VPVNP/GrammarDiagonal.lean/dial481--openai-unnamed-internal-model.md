---
{
  "module": "OAI/Computability/VPVNP/GrammarDiagonal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarDiagonal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarDiagonal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The diagonal criterion for the explicit grammar and machine

In Proposition 9.1 the live sites run the clocked machine defining the
integer family. For each primed pair we use its actual universal grammar
label queries and count all joint parse choices with the nominated histogram.
The first-half gadget paths and the tail evaluator still have to realize
their specified path multiplicities within the program's budget.


### `Nomination`

 A nomination gives one fixed-width counter for every production label.
All possible counter settings are included. 

### `multiplicity`

 The integer coefficient of the nominated histogram, counted by the pair
parser for the fixed incident exterior bits. 

### `noGrammarSimulation`

 The two-mode simulation cannot coexist with the grammar label equations.
This is the finite algebraic part of Proposition 9.1 with the paper's site
counts, complete nomination ranges, and exact pair histogram multiplicities. 
