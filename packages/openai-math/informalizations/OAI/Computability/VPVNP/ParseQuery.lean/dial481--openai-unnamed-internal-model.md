---
{
  "module": "OAI/Computability/VPVNP/ParseQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Querying a grammar coefficient by leaf assignments

In equation (8.1) of *VP and VNP differ over every field*, the queried monomial
contains one distinct variable for each bit position. Its coefficient is the sum of
the parse weights, counting each bijective assignment of terminal occurrences to
matching query positions once.


### `list_prod_X_eq_monomial`

 A list of terminals contributes one copy of each listed variable. 

### `terminalExponents_eq_query_iff`

 The terminal exponent vector matches the queried monomial exactly when the two
words have the same multiset of variables. 

### `coeff_eval_query_multiset`

 Extract the coefficient by comparing multisets of terminal variables. 

### `coeff_eval_query_bijections`

 For an injective query this coefficient counts one weight for each parse and each
bijective, label-preserving assignment of its leaves to the queried positions. 

### `coeff_eval_paired_bijections`

 The query of (8.1) pairs the position index with the requested bit.
Distinct first coordinates make the query injective over every coefficient semiring. 
