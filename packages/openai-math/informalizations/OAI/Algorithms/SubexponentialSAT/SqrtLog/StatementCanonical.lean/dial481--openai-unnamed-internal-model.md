---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/StatementCanonical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/StatementCanonical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/StatementCanonical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical primitive-machine statement of the stronger SAT target

All input and machine semantics are the audited original definitions.  The
machine is chosen once per fixed width, before all input sizes and formulas.
The final target below is a proposition, not an asserted existence theorem.


### `DecidesWithBound`

 Correct decision on every canonical input, with a measured primitive trace.
There is no density promise, oracle, or large-input-only qualification. 

### `Feasible`

 The machine and all constants may depend on width only. 

### `MainTheorem`

 The complete uniform fixed-width target; no inhabitant is supplied here. 

### `mainTheorem_iff_explicit`

 Expansion of every semantic abbreviation in the target's input and output
contract.  This is an equivalence of statements, not a proof of either side. 
