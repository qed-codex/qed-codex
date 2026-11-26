---
{
  "module": "OAI/Computability/VPVNP/CompletePolynomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompletePolynomials.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompletePolynomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact circuit sizes of the complete families under padding

The projections of §15.1 make exact circuit size monotone in matrix order. The
transfer theorem takes as inputs the lower bound for the hard family and its
p-projection from the matrix family. It covers every sufficiently large order,
including the gaps between consecutive orders in the reduction.


### `permanentCircuitSize_le_succ`

 Diagonal padding makes minimum permanent circuit size nondecreasing. 

### `hamiltonianCircuitSize_le_succ`

 Forced-arc subdivision makes minimum Hamiltonian-cycle circuit size
nondecreasing from order two onwards. 

### `matrixFamily_bound_of_projections`

 Given a polynomially bounded sequence of projection orders and an eventual
hardness bound, monotone padding transfers the bound to all large matrix orders. 

### `matrixFamily_bound_of_pProjects`

 A p-projection onto an eventually hard family forces the same type of bound
at every sufficiently large order of the source family, provided it admits padding. 

### `hamiltonian_bound_of_pProjects`

 The Hamiltonian-cycle implication in §15.1, with the Valiant reduction and
the hard-family lower bound supplied explicitly. 

### `permanent_bound_of_pProjects`

 The permanent implication in §15.1. Its use outside characteristic two
requires the p-projection supplied there by Valiant completeness. 
