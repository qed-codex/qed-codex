---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Finite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Finite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Finite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Price determination at geodesic sites

An extension adds duplicate sites with upper bounds on every evaluation.
The prescribed endpoint inequalities and Busemann convexity identify
these duplicates up to distance zero.


### `enlarge_base`

 Additional old sites do not change closure tests on the marked ones. 

 # Geodesic determination on finite placements 

### `Agree`

 Compare possibly repeated finite markings by their prices. 

### `Cap`

 An upper bound on prices stable under products and restrictions. 

### `Cap.geodesic_le`

 A submean inequality propagates whenever the two endpoint wire
bounds force the prescribed positions on their geodesics. 

### `Agree.extend`

 The scales may differ, and the old sites need not exhaust either ambient
placement. Intermediate points can be added at different parameters. 

 # Evaluations of finite geodesic expressions 

### `Fits`

 A consistent evaluation at the sites named by e, restricted to one
term and all its subterms. 


# Uniform finite tests for geodesic distances

On a compact set of enlarged prices, pairs with a prescribed discrepancy
in a term distance are compact. Some old tensor separates each such
pair, so finitely many old tensors suffice with positive tolerance.


### `finite_terms_tests`

 Old tensor prices determine all distances among the indicated terms,
uniformly over complete realizations and repetitions of the markings. 
