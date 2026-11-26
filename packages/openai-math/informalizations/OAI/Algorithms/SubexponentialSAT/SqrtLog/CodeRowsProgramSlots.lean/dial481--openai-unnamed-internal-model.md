---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CodeRowsProgramSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Sparse local-slot specifications. A row lists at most D original clause
indices, including any zero coefficients; shortening only removes slots whose
actual shifted edge index lies outside the original m coordinates. 

### `rowPayload`

 Forward payload inside an outer row frame. The standard frame reader
returns its reversal, exactly the raw tuple ABI expected by the materializer. 
