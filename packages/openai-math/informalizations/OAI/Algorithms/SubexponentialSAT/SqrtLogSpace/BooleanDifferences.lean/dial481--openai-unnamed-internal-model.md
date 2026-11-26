---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/BooleanDifferences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/BooleanDifferences.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/BooleanDifferences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Boolean finite differences (ETH, Lemma `boolean-differences`).
The finite sets in this module specify sums; they are not operational enumerators. 

### `supportFamily`

 The original support counting envelope. 

### `pairFamily`

 Valid correction pairs form a subset of the square of the support envelope. 

### `supportFamily_map_equiv`

 Coordinate transport preserves the exact support counting envelope. 

### `pairFamily_map_equiv`

 A coordinate equivalence transports the iterator's pairs exactly. This is
an internal indexing change, not a change of the ambient assignment universe. 

### `evalAt`

 Substitution of the Boolean characteristic vector of a set. 

### `difference`

 The coefficient of the Boolean multilinearization indexed by `E`. 

### `support_card_le_totalDegree`

 Degree controls the number of distinct variables in every monomial. 

### `evalAt_eq_sum_differences`

 Recovery at one Boolean point; high-degree supports do not contribute. 

### `trueSet`

 Boolean assignments retain all ambient variables, including unused ones. 

### `sum_eval_eq_sum_differences`

 ETH Boolean finite differences over an arbitrary commutative ring.
The polynomial is allowed to depend on the assignment being summed. 

### `coeff_sum_eval_eq_sum_differences`

 Every retained Taylor coefficient is recovered using the same pair family.
The hypothesis is the precise degree cost: each formal correction variable carries Z. 

### `truncated_sum_eval_eq_sum_differences`

 The entire truncated Taylor polynomial, also for J = 0 and an empty variable type. 
