---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Encoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Encoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Encoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# An explicit binary encoding of finite CNF formulas

Numeric fields are unary on the binary alphabet: `n` is `n` true bits and
one false bit. Lists use an explicit escape frame, and both levels of finite
sets are sorted before encoding. No enumeration of semantic truth values or
noncomputable choice participates in the encoding.


### `encodeNat`

 Unary natural-number field, terminated by a false bit. 

### `readNat`

 Read a unary field and return the unconsumed suffix. 

### `frame`

 Escape each data bit with a true bit; terminate the frame by false. 

### `readFrame`

 Decode one escape frame and return its unconsumed suffix. 

### `encodeList`

 Explicit list syntax: false ends a list; true introduces a framed item. 

### `literalCode`

 Literal syntax contains its variable index and polarity, independently of semantics. 

### `clauseNumbers`

 Sort the injective numerical representations of a clause's literals. 

### `cnfNumbers`

 Canonical order of the explicit literal lists of the formula's clauses. 

### `encodeCNFBody`

 The payload is a list of literal-code lists, in explicit binary list syntax. 

### `encodeCNF`

 Full binary formula syntax, including the ambient number of variables. 

### `encodeFormula`

 The encoding also distinguishes formulas with different variable-coordinate types. 

### `formulaBitLength_upper`

 A polynomial upper bound for the actual encoding, without any semantic oracle. 
