---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CNFNormalize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CNFNormalize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CNFNormalize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


Raw input normalization for the frozen counting manuscript, lines 1758–1762.
The ambient type remains `Fin n` throughout, including unused variables.


### `eval_formulaSet`

 List multiplicities have exactly the usual disjunction/conjunction semantics. 

### `rawCount_normalize`

 No variable restriction or unit propagation occurs in this normalization. 

### `encodeRawCNF_length_upper`

 Raw repetitions remain charged in the encoded input length. 

### `encodeRawCNF_length_polynomial`

 For fixed width the complete raw binary input has quadratic size in `n + m`. 

### `encodeRawCNF_normalize_length_bound`

 Normalization bounds the output language for fixed declared `n`, even with
arbitrarily many raw repetitions and without a width promise. 

### `encodeRawCNFBody_length_eq`

 Sorting literals and clauses changes their order but not the serialized size.
The hypotheses exclude both literal repetitions and semantically duplicate clauses. 
