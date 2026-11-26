---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCallInvariant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallInvariant.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallInvariant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds at the physical call boundary

A charge transfers one unit from the remaining global credit to the cumulative
cost. The private log and unspent fuel together remain bounded by the public
call clock. Every future probe therefore has room in the record buffer before
it is staged.


### `CallReady`

 Site-controller invariant at a call boundary, tracking the buffered records, public limits,
remaining credits, private clock and scratch-word lengths. 

### `InCall`

 Call-boundary invariant strengthened with the saved start and probe ordinal. The current
cost is the start plus one startup charge and the ordinal. 

### `segmentWork`

 Stack-step allowance for one segment of private instructions between external actions, as a
function of the word width and call clock. 

### `callWork`

 Stack-step allowance for an entire metered call, reserving `F + 1` segments at the
per-segment bound. 

### `CallReturn`

 One returned segment preserves the public bank and records, and reports
the extra probes of the current call with their original startup time and
the ordinals immediately following those already emitted. 

### `SegmentRun`

 The linked site controller rejects when local call execution fails, or returns to its
iteration test with the corresponding report, residual choices and buffered records. 
