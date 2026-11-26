---
{
  "module": "OAI/Computability/VPVNP/MotifParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral equations for the fixed motif maps

For each point of the demand grid in Theorem 6.1, impose its base tensor
identity in every output coordinate. Distinct entries of the selected local
maps are separate indeterminates. The equations can thus be specialized in
any commutative ring, using the same integer tensors and the same bases.


### `Data`

 Integral arrays and the selectors indexing their local images. 

### `Data.Selector`

 Finite type of admissible supply selections for a given demand grid point. 

### `Data.demand`

 Integer tensor to be expanded at the chosen demand grid point. 

### `Data.supply`

 Integer supply tensor used by one selector in the local-map expansion of the demand
  tensor. 

### `Entry`

 Each grid point, selector, party, row and column specifies one variable. 

### `Output`

 One equation for every joint output coordinate at every grid point. 

### `localMap`

 The local matrices read from a single parameter assignment. 

### `equation`

 Difference of the two sides of a base identity at one output coordinate. 

### `IsSolution`

 Simultaneous vanishing of the integral equations. 

### `eval_equation`

 Evaluating a base equation contracts the actual local matrices over the
ring of the assignment. 

### `solution_iff`

 Specialization of all the equations is equivalent to all the ordinary sum
identities, as equalities of arrays in the original demand bases. 

### `exists_solution`

 Base identities at individual grid points give a single simultaneous
solution by assigning their matrix entries to their own variables. 

### `wireData`

 The fixed integral tensors for the selectors in the spectral comparison. 

### `wire_solution_iff`

 Specialization recovers the binary wire identities over the assignment's
ring. All their matrix indices are taken in the original wire bases. 

### `exists_wire_solution`

 Spectral base identities over the chosen field supply all the parameters
of a single integral equation system at once. 

### `entryExponents`

 Counting repeated parameter indices gives the exponent vector of one
matrix entry in the repeated local map. 

### `prod_entries_eq_monomial`

 A product of base entries, including repetitions, is one monomial with
coefficient one. The empty product also satisfies this formula. 

### `prod_entries_degree_le`

 One selected base entry per copy contributes at most one degree per copy. 
