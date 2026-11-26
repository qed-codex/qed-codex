---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNativeSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNativeSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNativeSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Validity and storage bounds for the actual raw dictionaries produced by
native hash-row execution. No canonical-output premise is used. 

 Denotation of the concrete raw row recurrence used by the native program. 

### `clauseFold_congr`

 A clause fold only reads the variables of its listed literals. 

### `clause_polynomial`

 A marked clause uses this result directly, without an idempotent map. 

### `clause_list_polynomial`

 Direct clause-list form, used by the marked-clause factor. 

### `row_denote`

 The exact executable raw result denotes the canonical source polynomial. 

### `clause_denote_scoped`

 Only the incidence rows referenced by this clause need the intended value. 

### `row_denote_scoped`

 Missing variables may have zero rows: only literals actually read by this
factor require the intended incidence semantics. 

 Instantiation at the actual supplied-polynomial unramified ring. 

 Original literal identifiers remain unchanged when the native dictionaries
carry padded jets from the free coordinates of a branch. 
