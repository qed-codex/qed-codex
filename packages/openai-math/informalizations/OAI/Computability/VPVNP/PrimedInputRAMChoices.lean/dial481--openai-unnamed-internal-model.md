---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMChoices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMChoices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMChoices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the internal primed bits of Section 11

The first pass visits the `2Rn` endpoint positions in flattened address order. At
the designated endpoint of each shared bit it branches once and writes that choice
to scratch. All initial memory outside those writes is preserved. No consistency
test on a primed sorting or successor message is part of this pass.


### `owners`

 Designated positions in the order the first pass visits them. 

### `Assignment`

 A simultaneous choice of the shared bits indexed by their unique owners. 

### `bitAt`

 Only the restriction to the designated positions is used. 

### `branches`

 Branch choices in ascending endpoint order. 

### `branchEquiv`

 An exact-length branch stream is equivalent to the independent bit choices. 

### `CellControl`

 Control for the single call associated to a position. 

### `cellCall`

 The classifier, scratch address and successor state are computed from the public
position. This call takes one instruction at an unselected cell and three at an owner. 

### `scan`

 Scan the full endpoint list, retaining an exact branch stream. The address is
injective across all endpoints. The per-cell reports above implement its memory update. 

### `firstPass`

 Scan the entire input rectangle in order, consuming and storing one branch bit at each
designated owner and requiring the stream to be exhausted. 

### `firstPass_accepts`

 Both a short stream and a stream with extra branch choices reject. 

### `admissibleEquiv`

 Accepted streams are in bijection with all assignments, for arbitrary initial memory. 

### `store`

 Each selected position receives its prescribed word, independent of old scratch contents. 

### `store_outside`

 Addresses outside the writes keep their original words, including all headers in
an address range disjoint from the scratch array. 

### `scratchAddress`

 A contiguous rectangular scratch region following the headers. 

### `cellReport`

 A per-cell report, retaining the actual choice even when the overwritten word already
has the chosen value. `next` allows the caller to supply the encoded successor cursor. 

### `reports`

 Genuine per-cell reports for the first pass in its cursor order. 

### `after_reports`

 Replaying the actual event reports gives exactly the scratch updates. 

### `reports_cost`

 The paper charges one unit to start every call and one for every scratch write. 

### `firstPass_budget`

 At most one write probe and one call per cell. Unselected cells only use their call. 
