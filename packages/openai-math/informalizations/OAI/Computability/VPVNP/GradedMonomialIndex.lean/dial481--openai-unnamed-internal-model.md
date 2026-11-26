---
{
  "module": "OAI/Computability/VPVNP/GradedMonomialIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GradedMonomialIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GradedMonomialIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming indices for bounded monomials

Appendix D orders monomials by total degree and then lexicographically. The
outer radix digit stores the degree, and the remaining digits store the
exponents, with variable zero in the most significant position. Removing the
codes with an inconsistent degree gives a dense indexing. Both directions use
counter loops, so neither needs a list of the monomials.


### `countCodes`

 Count admissible codes strictly below the bound. 

### `selectCode`

 Scan an interval until the zero-based ordinal of a valid code is reached.
The loop keeps only the current code, remaining interval and remaining ordinal. 

### `denseCount`

 Dense numbering of the selected indices of a finite interval. 

### `denseEquiv`

 The ordinal of each selected code and the inverse ordinal query.
Both use scans of the same interval. 

### `rawSize`

 Unfiltered addresses consist of one degree digit and `t` exponent digits. 

### `digit`

 Read a single exponent by radix division and remainder. 

### `admissible`

 Test that the exponent digits of a raw monomial index sum to its recorded total degree. 

### `size`

 Number of monomials through degree `D`, obtained without a monomial table. 

### `exponentVector`

 Build the formal exponent vector for a tuple in the finite label alphabet. 

### `rawCode`

 Graded-lex key of a bounded monomial, before removing unused codes. 

### `enumeration`

 Computable dense graded-lex enumeration of all bounded monomials. 

### `indexedDigits`

 Read the exponent vector at a dense ordinal, without constructing a support set. 

### `degree_eq_outer`

 The outer radix digit stores the total degree. 

### `enumeration_strictMono`

 Dense ordinals have strictly increasing graded radix keys. 

### `constant`

 The constant monomial gives dense ordinal zero, including when there are
no variables or when the degree bound is zero. 
