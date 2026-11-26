---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadProgramPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadProgramPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PackingHeadProgramPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed counted loop over the existing flattened head prefix. Every
iteration copies the candidate and counts its true bitwise intersections with
one prefix word. No per-coordinate metadata or selected-pair stream is supplied. 

### `command_eval`

 Existing candidate bytes and flattened prefix bytes are the real inputs.
The unary prefix length is consumed; the candidate is preserved. 
