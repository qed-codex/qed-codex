---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafQueryFrontendReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual frontend neither reads nor writes outer carried tapes. 

### `frontend_avoids`

 Syntactic avoidance includes peeks, so arbitrary carried words cannot affect time. 

### `frontend_avoids_outerCarried`

 The concrete frontend does not read or write tapes 320, 322, or 332. 

### `frontend_eval_rebase_outerCarried`

 Replacing any outer carried words leaves the actual frontend duration unchanged. 
