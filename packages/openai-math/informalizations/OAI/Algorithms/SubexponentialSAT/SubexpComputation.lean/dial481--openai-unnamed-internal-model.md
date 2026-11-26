---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpComputation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComputation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpComputation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Precise computational target of the subexponential SAT manuscript

The source is `source/subexponential-sat.pdf`, Theorem 1.  The input and
primitive transition model are unchanged from `SubexponentialSAT.Computation`.  Both
constants, the polynomial degree, and the finite machine are chosen before
the input size.  In particular the growing layout parameters cannot be
encoded as size-dependent advice in the machine.

This module defines the target and proves elementary closure and compiler
lemmas.  It does not assert that a solver satisfying the target exists.


### `logLog`

 The positive base-two iterated logarithm used in Theorem 1, including its
specified shift at small inputs. 

### `scale`

 The actual subexponential scale, not a free exponent function. 

### `runtimeBound`

 The two constants are independent: the outer multiplicative constant
and the constant in the exponent can both depend on the fixed clause width. 

### `runtimeBound_pow`

 A fixed-degree polynomial slowdown preserves the target exponential
scale.  The degree must be fixed before the input size. 

### `one_le_runtimeBound`

 Sequential input handling and a fixed polynomial overhead may be added
to a source runtime without changing the asymptotic class. 

### `DecidesWithBound`

 One fixed finite primitive machine reads the concrete raw CNF encoding,
returns a correct answer, and has an actual bounded transition trace. 

### `MacrostepDecidesWithBound`

 The same contract at the finite-alphabet stack-machine level.  A separate
proved compiler, rather than an identification of macrosteps with bit steps,
is used below to obtain the primitive contract. 

### `Feasible`

 Uniformity is expressed by the existential machine preceding every input
in `DecidesWithBound`. 

### `MainTheorem`

 The full statement of Theorem 1 of `subexponential-sat.pdf`.
No inhabitant is supplied merely by this definition. 

### `macrostep_to_primitive`

 The already checked finite-alphabet compiler supplies all simulation
premises, so a complete macrostep solver would suffice for Theorem 1. 
