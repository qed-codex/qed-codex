---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairEntries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairEntries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairEntries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reading matrix entries from the physical flags and exponents

The equality word selects exactly the coefficient of the specified formal
monomial, also when the target is obtained by label multiplication or
Frobenius before taking the certificate power. The equation arm's flag
and residual exponents give the shifted scalar coefficient directly.


### `powerMatch_entry`

 No marked coordinate is used for a source monomial in the appended matrix. 

### `targetScale`

 The parameters used for a powered target row. 

### `targetMark`

 One-based variable index to increment for a label-multiplication query. Frobenius uses zero
so every coordinate is left unmarked. 

### `equationEntry_at`

 Decode the integer/affine row block. The ordered buffer has exactly
the difference exponents passed to the coefficient reader. 
