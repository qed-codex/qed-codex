---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSetupCostScale.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSetupCostScale.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeSetupCostScale.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A uniform numerical envelope for the actual finite code searches.
Search dimensions occur only in the exponential factor. Encoded metadata
lengths remain in a separate fixed polynomial factor. 

### `eventually_envelope`

 One cutoff works for all admissible dimensions and metadata lengths. 

### `eventually_envelope_with_words`

 Arbitrarily padded encodings retain their visible polynomial factor. 
