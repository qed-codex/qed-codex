---
{
  "module": "OAI/Computability/VPVNP/VerifierFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierFormula.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic formulas for Boolean witness verification

Formulas give explicit circuits for products of local constraints in a VNP summand.
Compilation uses one gate per binary node, including products of constants.


### `Formula`

 An arithmetic formula with scalar and variable leaves. 

### `add`

 Form a binary addition node with summands `a` and `b`. 

### `sub`

 Form a binary subtraction node with minuend `a` and subtrahend `b`. 

### `mul`

 Form a binary multiplication node with factors `a` and `b` in that order. 

### `size`

 Gate count excludes scalar and variable leaves. 

### `degree`

 Syntactic degree bounds the degree of the formal polynomial even after cancellation. 

### `eval`

 Evaluate a formula in the ring `A`, interpreting each constant with `s`, each variable with
`x`, and each binary node by its ring operation. 

### `polynomial`

 The formal multivariate polynomial represented by a formula over a commutative ring,
interpreting constants by `MvPolynomial.C` and variables by `MvPolynomial.X`. 

### `compile`

 Compile the formula to a straight-line program of exactly its binary node count. 

### `prod`

 Product of a finite family of formulas, starting with a scalar one. 
