---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFCodeTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFCodeTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFCodeTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact list transport through literal codes

These equalities preserve clause order and the last-occurrence conventions.
They connect the encoded normalization programs to the typed executable CNF
operations, rather than identifying only their finite-set semantics.


### `normalizedInput_eq_normalize`

 The extra pass in the typed worklist does not alter order or multiplicity. 

### `normalize_literalCode`

 Exact encoded normalization, including last-occurrence choices and order. 

### `normalizedInput_literalCode`

 This is the list-level interface consumed by the actual normalizer. 

### `petal_filter_map`

 The actual petal filter commutes with injective literal encoding. 

### `normalized_formulaList_codes`

 The canonical external syntax reaches exactly the same ordered leaf input. 
