---
{
  "module": "OAI/Algorithms/SubexponentialSAT/JetCRT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/JetCRT.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/JetCRT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reconstruction from formal polynomial jets over a commutative ring

These results use unit differences of nodes, not a field assumption. Jets are
formal Taylor polynomials modulo `X ^ D`; no factorial divisions occur.


### `nodePower`

 The local modulus for an order-`D` jet at `a`. 

### `nodeIdeal`

 The ideal of polynomials whose order-`D` jet vanishes at `a`. 

### `jet`

 The formal order-`D` Taylor polynomial, using `X` as the local coordinate. 

### `modulus`

 The product of all powered linear local moduli. 

### `eq_of_dvd_sub_of_degree_lt`

 Divisibility at all nodes determines a polynomial below the total degree. 

### `eq_of_jets_of_degree_lt`

 Actual truncated formal Taylor polynomials determine the global polynomial. 

### `eq_of_jets_of_natDegree_lt`

 The natural-degree form is convenient for bounds on the global count polynomial. 

### `exists_unique_representative`

 CRT followed by monic division supplies the unique bounded-degree representative
of any family of local polynomial residues. This is an existence theorem, not a
claim about computability or bit complexity. 

### `jet_unshift`

 Shifting a local polynomial back to the global coordinate and then taking
its jet recovers exactly its truncation. 

### `exists_unique_of_jets`

 Every family of formal truncated local expansions has a unique global
polynomial of degree below the sum of the local orders. 

### `cofactor`

 The product of all local moduli except the one at index `i`. 

### `exists_bezoutCoefficients`

 Unit-separated nodes provide Bézout certificates for the explicit formula. 

### `reconstructWithBezout`

 A finite-sum CRT formula followed by monic reduction. Its Bézout coefficients
are explicit input data; producing those coefficients efficiently is separate. 

### `reconstructWithBezout_spec`

 Correctness of the explicit CRT formula, over a commutative ring. No field
operations or derivative/factorial expressions enter this certificate. 

### `reconstructJetsWithBezout`

 The explicit formula with inputs expressed in their local coordinates. 

### `reconstructJetsWithBezout_eq`

 Applying the certified finite-sum formula to the correct local data recovers
the original polynomial under its degree bound. 
