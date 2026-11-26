---
{
  "module": "OAI/Computability/VPVNP/RAMSortAddressBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortAddressBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortAddressBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Intermediate register widths for sort addresses

The addresses in Lemma 10.1 are computed by a bounded number of word operations.
For that interpretation the intermediate products in the triangular layer number
also have to fit. We bound the largest register value in each address expression,
including its inputs, by a fixed polynomial in the array length and the word width.


### `IndexExpr.peak`

 The largest value appearing at any node in the straight-line evaluation. 

### `IndexExpr.evalWord`

 Register semantics: the output of each elementary operation is reduced modulo
`2^bits` as soon as it is written. 

### `IndexExpr.evalWord_eq`

 A word evaluator recovers the exact address if all intermediate registers fit. 

### `addressEnvelope`

 A uniform bound for all register values in the sort address calculations. 

### `wireAddress_peak_le`

 Global index, XOR partner and direction test. The shift arguments and the mask
itself are included, even when the output direction bit is zero. 

### `fieldAddress`

 Computing the physical address of an individual bit adds its in-record offset
only after computing the start address. 

### `fieldAddress_peak_le`

 The maximum register value includes the product before division by two in the
triangular ordinal and the product of the field number and the field width. 

### `addressEnvelope_lt_paperWord`

 For Section 9's choice `w = (r+10)^4`, all the sorting registers fit as soon
as the logarithm of the array length is at most `(r+10)^2`. In particular, for
`h+d ≤ C*r` this holds for every `r ≥ C`. 

### `addressEnvelope_lt_paperWord_of_linear`

 The explicit eventual threshold for a linear phase bound `C*r`. 
