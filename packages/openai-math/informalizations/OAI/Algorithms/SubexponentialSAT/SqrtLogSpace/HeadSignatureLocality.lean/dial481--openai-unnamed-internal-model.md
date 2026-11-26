---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSignatureLocality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSignatureLocality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSignatureLocality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact full-integer head labels and fixed-high cancellation, extracted
unchanged from HeadSourceLocality. All raw rows and original coordinate IDs
are retained; source-product locality remains in the importing module. 

### `signature_eq_of_free`

 Equal fixed-high bits cancel; the remaining exact signature is the full
integer signature on the actual free coordinates of this head. 

### `freeLabel`

 Actual full integer keys use every emitted raw row, restricted only to
this head's free original coordinates. 
