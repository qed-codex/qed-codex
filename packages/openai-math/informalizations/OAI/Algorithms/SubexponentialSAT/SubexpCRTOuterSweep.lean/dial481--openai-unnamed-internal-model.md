---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Ordered execution of the concrete outer CRT tape loop. The only remaining
premise is an actual execution of its arithmetic middle command on the exact
loaded state; all loading, index updates, traversal guards, and transport costs
are discharged here. This premise is instantiated by the concrete CRT services.


### `transportCost`

 Physical per-node cost, excluding the arithmetic middle command. The
index copy contributes nine steps per already processed node. 

### `sweepLoop_run`

 The loop invariant records physical processed order, remaining order,
matching jet order, and the unary index. The arithmetic premise is an actual
finite-program trace, not a supplied answer or cost annotation. 
