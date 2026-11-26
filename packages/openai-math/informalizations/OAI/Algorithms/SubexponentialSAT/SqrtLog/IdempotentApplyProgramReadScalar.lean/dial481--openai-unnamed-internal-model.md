---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramReadScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact native refinements for the scalar coefficient reader and injector.
All stacks outside the named outputs are preserved, including the ambient
low-product environment. 

### `scalar_eval`

 The scalar loader restores every work stack. Only the consumed source
prefix and the new constant dictionary differ from the caller state. 

### `constantBytes_scalarVector`

 The physical bytes are the standard singleton dictionary encoding. 

### `scalar_words_eval`

 Typed singleton bytes, with an explicit polynomial instruction count. 
