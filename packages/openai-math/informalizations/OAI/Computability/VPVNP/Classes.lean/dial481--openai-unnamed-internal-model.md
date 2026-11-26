---
{
  "module": "OAI/Computability/VPVNP/Classes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Classes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Classes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Nonuniform arithmetic complexity classes

A family is indexed by its length. Its variables may be any finite type at that length.
The bounds are asymptotic, with an exponent and a leading constant independent of the
length. Circuits compute formal polynomials, and only Boolean witness variables are
specialized to field elements in the definition of VNP.


### `PolynomiallyBounded`

 There are fixed natural numbers `A`, `d` and `N` such that `f n ≤ A * n^d` for every `n ≥
N`. 

### `Family`

 A sequence of formal polynomials over `F` whose variable type `σ n` may depend on the index
`n`. 

### `PFamily`

 Both the number of variables and the total degree of the indexed polynomials are
polynomially bounded in the family index. 

### `IsVP`

 The family has polynomially bounded variable count and degree, and each member is computed
exactly as a formal polynomial by arithmetic circuits of polynomially bounded size with
arbitrary field constants. 

### `witnessValue`

 Substitution of the bits of a single witness, leaving the output variables formal. 

### `IsVNP`

 A polynomial family obtained by summing a VP family over all Boolean assignments to a
polynomially bounded number of witness variables, with the output variables left formal. 

### `PProjects`

 The source index can grow polynomially and need not be monotone. 

### `VNPComplete`

 The family belongs to VNP and every VNP family over the same field is obtained from it by a
polynomially bounded reindexing and substitutions of variables by target variables or field
constants. 

### `not_isVP_of_eventual_size`

 The strict lower bound required in Theorem 1.1 excludes membership in VP. 
