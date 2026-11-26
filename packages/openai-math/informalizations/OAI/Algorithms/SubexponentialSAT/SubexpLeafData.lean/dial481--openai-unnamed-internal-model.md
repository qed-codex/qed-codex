---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLeafData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLeafData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLeafData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Factor data in the emitted order of a sparse leaf

The input is the actual typed list of literal lists. Clause-set uniqueness is
the normalizer/worklist invariant; no sorted finite-set enumeration is used.
Unary factors precede clauses, and clause scopes retain the last-occurrence
order of the concrete deduplicator.


### `clauses_nonempty`

 The actual empty-clause scan supplies the nonempty-scope condition
needed before invoking the layout constructor. 

### `clauseEquiv`

 The physical clause index and its finite-set semantic clause. 

### `literals`

 Retrieve the original literal order of a semantic clause. 

### `factors`

 The exact factor order: all unary chunks, then the emitted clause list. 

### `clauseScope`

 The same last-occurrence deduplication used by the raw scope producer. 

### `scope_stream`

 The scope stream in the very same unary-then-clause order. 

### `clauseScope_codes`

 The typed chunk scope is exactly the numeric scope produced from the
raw signed literal codes. This equality preserves the deduplication order. 
