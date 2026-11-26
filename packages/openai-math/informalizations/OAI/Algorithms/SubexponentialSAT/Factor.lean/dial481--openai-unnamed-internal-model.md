---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Factor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Factor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Factor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite Boolean-valued factor systems

This module formalizes the finite sum of products in Sections 2 and 3 of the
candidate exposition.  Factor tables have genuine local domains, so dependence
only on a scope is enforced by their type.  Counting is an actual finite sum of
natural-number products.  No running-time assertion is made here.


### `Pattern`

 A finite-scope pattern.  Finiteness of the index types is requested only by
those constructions which enumerate them. 

### `Pattern.Bounded`

 The nonempty-scope, arity, and incidence hypotheses of Lemma 3.1. 

### `System`

 A factor reads exactly the coordinates in its declared scope. 

### `evalFactor`

 Evaluate one local table on a global assignment. 

### `Satisfies`

 An assignment satisfies the system when every local table accepts it. 

### `instDecidableSatisfies`

 Satisfaction is decidable by checking the explicitly finite factor index. 

### `factorValue`

 The natural-number indicator of one factor accepting an assignment. 

### `evalFactor_congr`

 Locality is enforced by the table domain, rather than assumed as an axiom. 

### `weight`

 The product appearing as one summand of the factor count. 

### `weight_eq_indicator`

 The product of Boolean-valued indicators is the indicator of satisfaction. 

### `satisfyingAssignments`

 The actual finite set of satisfying assignments. 

### `count`

 The sum of products defining the exact integer factor count. 

### `count_eq_card_satisfying`

 The sum of products counts exactly the satisfying assignments. 

### `count_eq_card_subtype`

 A subtype-cardinality form convenient for transporting solutions by an
explicit equivalence. 

### `count_pos_iff`

 Positive count is equivalent to the existence of a satisfying assignment. 

### `count_eq_zero_iff`

 A zero count is equivalent to unsatisfiability. 

### `count_le_card_assignments`

 The finite count is no larger than the number of assignments. 

### `count_le_pow`

 The bound used when selecting the prime-power counting modulus. 

### `count_congr`

 Extensional equality of acceptance predicates preserves the exact count. 
