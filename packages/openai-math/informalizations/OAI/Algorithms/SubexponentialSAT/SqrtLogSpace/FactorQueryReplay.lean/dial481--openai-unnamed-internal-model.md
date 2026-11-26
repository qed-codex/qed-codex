---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorQueryReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorQueryReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FactorQueryReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual assignment program neither reads nor writes collector tapes320
and322. Certificates include the cache constructor, dispatcher peeks, source
specialization, arithmetic, parser iterations and all cleanup instructions. 

### `setup_avoids`

 The concrete constant encoder and every paid cache copy avoid the
collector words, including any temporary reads in their implementations. 

### `assignment_avoids`

 No tape operation in the fixed accepted-assignment implementation touches
an outer collector tape. This includes reads, not only final-state framing. 
