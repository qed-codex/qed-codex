---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BinomialMultiplicity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialMultiplicity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BinomialMultiplicity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact multiplicities for the four-state local eigenbasis

The main count is proved for any finite alphabet with one distinguished state.
It is a genuine cardinality theorem, obtained by recording the distinguished
support and choosing a non-distinguished label on its complement.


### `negativeSupport`

 Positions at which a word takes the distinguished negative label. 

### `weight`

 The number of negative local basis labels in a word. 

### `supportFiberEquiv`

 A word with prescribed negative support is exactly an assignment of
nonnegative labels on the complementary positions. 

### `card_weight`

 Exact binomial multiplicity for an arbitrary finite alphabet. 

### `pairWeight`

 The exact weight convention used by the tensor product local eigenbasis. 

### `card_pair_weight`

 Three positive local basis labels and one negative label give the claimed
`choose(q,w) * 3^(q-w)` multiplicity. 

### `weightedProductEquiv`

 Extra independent labels contribute their full cardinality at every weight. 

### `weightedProductLeftEquiv`

 The same decomposition with the spectator label first, as in the explicit
spectator eigenbasis. 

### `sum_multiplicities`

 Summing every weight multiplicity recovers all four-state words. 

### `sum_multiplicities_with_unused_bits`

 The same total with independent unused bits. 

### `regression_two_positions_one_negative`

 Small enumeration computed by the kernel, independently of the general
cardinality formula. 

### `regression_two_positions_one_unused_bit`

 The independent unused bit doubles the six words in the preceding example. 
