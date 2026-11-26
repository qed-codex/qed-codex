---
{
  "module": "OAI/Algorithms/SubexponentialSAT/TruncatedConvolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TruncatedConvolution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TruncatedConvolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The elementary update schedule implemented by the fixed convolution loop.
This module defines values only; it assigns no execution cost to them. 

### `addProduct`

 Add one product into one existing coefficient slot. 

### `row`

 A row of the triangular product schedule, beginning at output slot i. 

### `rows`

 Fuel is the number of remaining output slots, so a row uses only that
many right-hand coefficients. All writes therefore have degree below D. 

### `run`

 Exactly D output slots; callers supply the actual zero coefficient. 
