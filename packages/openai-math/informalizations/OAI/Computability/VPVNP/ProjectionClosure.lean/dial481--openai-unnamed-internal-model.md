---
{
  "module": "OAI/Computability/VPVNP/ProjectionClosure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ProjectionClosure.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ProjectionClosure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Closure of VP and VNP under p-projections

The family receiving a projection has polynomially many variables. Lift a projection
through the VNP sum by projecting the visible variables and keeping each Boolean
witness variable as a formal input to the new summand.


### `PFamily.of_pProjects`

 Formal variable-or-scalar substitution preserves a polynomial bound on the degree. 

### `Projection.withWitness`

 Extend a projection of visible variables by the identity on witness variables. 

### `Projection.witnessValue_comp`

 Specializing the Boolean witness before or after the visible projection agrees. 
