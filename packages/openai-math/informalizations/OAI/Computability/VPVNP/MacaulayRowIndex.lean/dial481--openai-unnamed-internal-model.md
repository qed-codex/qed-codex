---
{
  "module": "OAI/Computability/VPVNP/MacaulayRowIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRowIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRowIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entrywise queries in the finite-slice coefficient matrix

The indexed matrix of Appendix D is given by a scalar equation-coefficient
routine. A Macaulay entry needs at most one call to it. The appended rows and
targets are powered monomials, so their entries require only exponent tests.


### `rowEquiv`

 Dense address of an equation and a multiplier monomial. 

### `equationEntry`

 Coefficient of a monomial multiple of an equation, read at a dense column index. 

### `powerEntry`

 An entry of a powered monomial row, computed without forming a polynomial. 

### `powerEntry_eq`

 A coefficient lookup agrees with taking the indicated power in the formal
polynomial ring. This identity also covers power zero and the empty tuple. 

### `monomialAt`

 The original (unpowered) monomial represented by a dense ordinal. 

### `entryCoordinate`

 A coordinate in the list of original monomial ordinals. Non-basis
ordinals return zero. All matrix arguments are entry routines. 
