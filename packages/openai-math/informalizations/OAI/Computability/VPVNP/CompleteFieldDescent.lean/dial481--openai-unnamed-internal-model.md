---
{
  "module": "OAI/Computability/VPVNP/CompleteFieldDescent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompleteFieldDescent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompleteFieldDescent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniformity across fields of a fixed characteristic

Section 15.1 of *VP and VNP differ over every field* proves its bounds for the
Hamiltonian cycle and permanent over an algebraic closure of the prime field.
The sums defining these polynomials commute with coefficient maps. Thus the
same threshold and exponent in a bound over that closure apply to every field
of the given characteristic, even when circuits use arbitrary constants.


### `circuitSize_intCast_descent`

 Every integer polynomial has minimum gate count over an algebraically closed
field among fields of the same characteristic. This includes characteristic zero. 

### `circuitSize_intCast_uniform_bound`

 For an integer family, a lower bound over one algebraically closed field
supplies a single threshold before quantifying over all fields of the characteristic. 

### `hamiltonianCyclePolynomial_size_descent`

 Comparison of directed Hamiltonian-cycle circuit sizes at the same order. 

### `permanentPolynomial_size_descent`

 Comparison of permanent circuit sizes at the same order. Scalar descent
applies in every characteristic, including characteristic two. 

### `hamiltonianCyclePolynomial_uniform_bound`

 A threshold for Hamiltonian cycles over the algebraic closure works uniformly
for every field of its characteristic. 

### `permanentPolynomial_uniform_bound`

 A threshold for the permanent over the algebraic closure works uniformly
for every field of its characteristic. 
