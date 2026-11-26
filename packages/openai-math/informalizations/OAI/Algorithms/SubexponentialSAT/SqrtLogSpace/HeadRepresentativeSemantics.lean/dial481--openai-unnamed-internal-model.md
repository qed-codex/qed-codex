---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadRepresentativeSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadRepresentativeSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadRepresentativeSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `merge_fold_ofFn`

 Exact meaning of repeated executions of the original ambient merge scan.
A head's supplied word need only agree with the target at its selected coordinates. 

### `representative_heads`

 All representative heads reconstruct the full ambient assignment, with
fixed-high coordinates retained. Head order and repeated visits are harmless. 

### `merge_candidate_ofFn`

 Updating the owned head in the reconstructed representative preserves
all foreign-head bits, including fixed-high coordinates. 

### `headOrder_stream`

 The actual chosen-ID word fixes the ascending selection order. 

### `selected_headOrder`

 The native selected-bit scan emits exactly the current head's ambient
coordinates in the already emitted headOrder, including the empty head. 

### `headOrder_highCount`

 The physical selected-mask population is the actual emitted head width. 

### `selected_supportBits`

 The concrete local correction word is the support indicator at the
same ascending head positions used by the cursor and full matrix columns. 

### `head_correction_iff`

 Combined with NativeHeadSelect.prepared_E/prepared_H, this identifies
the actual gate test with membership in E at original head coordinates. 
