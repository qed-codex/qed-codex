---
{
  "module": "OAI/Computability/VPVNP/JointLabelEvaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelEvaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointLabelEvaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Applying the finite-algebra evaluator to the small-circuit label equations

At a length with a circuit of size at most `n^c`, the grammar assignment and
the fixed motif solution descend together. The prime is fixed in positive
characteristic and has polynomially bounded bit length in characteristic zero.
The resulting finite algebra therefore satisfies all instances of (8.1) and
all the local wire identities, with one normalized evaluator for every label
exponent vector.


### `degreeBound`

 Degree bound for all grammar and motif equations, raised to at least three for the
finite-algebra construction. 

### `primeBits`

 When the joint grammar and motif equations have a characteristic-zero solution, descent
yields a finite model at a prime bounded by two to this exponent. 

### `primeBits_polynomiallyBounded`

 The exponent in the good-prime size bound is polynomial in the input length. 

### `exists_evaluator_of_circuit`

 An actual small circuit and motif solution yield the finite-algebra
evaluator for the joint system. Both characteristic cases preserve the
specified quantifier order with respect to the input exponent vectors. 

### `evaluator_label_identities`

 The single reduced algebra furnished by the evaluator satisfies every
path-count coefficient identity and every fixed motif equation simultaneously. 
