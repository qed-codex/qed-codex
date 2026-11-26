---
{
  "module": "OAI/Computability/VPVNP/ScalarDescent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ScalarDescent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ScalarDescent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descent of exact polynomial computations

Section 1 of *VP and VNP differ over every field* passes from a circuit over an
arbitrary field to the same circuit topology over the algebraic closure of the prime
field. Each scalar input of the topology can first be replaced by a parameter. The
coefficients of the resulting formal output are polynomials in these parameters.
Hilbert's Nullstellensatz descends the simultaneous coefficient equations to any
algebraically closed extension of the base field.


### `polynomialSystem_descent`

 A polynomial system in finitely many unknowns that has a solution in an extension
field of `k` has a solution in every algebraically closed extension of `k`. 

### `formalOutput_descent`

 An exact specialization of a formal output polynomial over a parameter ring descends
simultaneously in all its coefficients. This applies to a circuit with any degree of
intermediate cancellation, using its scalar inputs as the parameters. 
