---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeFinish.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeFinish.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeFinish.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual node readout and loop continuation. The emitted coefficient stream
retains its order. Node temporaries are physically reclaimed before refreshing
the outer guard, and every completed node restores one fixed boundary bound. 

### `guardCursor`

 The outer node loop refreshes its guard after all inner controllers. 

### `finishNode`

 Called after actual node readout and append. The retained node accumulator
and theta are reclaimed before the next node, then the index and guard advance. 

### `result_high_frame`

 The node cursor, marked collectors and high pair inputs survive exactly. 

### `command_eval`

 Actual scalar caches and a Good empty-support node array suffice for the
whole readout, ordered append, cleanup, index update and fresh guard. 

### `run_space`

 All prefixes include the full incoming frame and every readout temporary.
The endpoint returns to incoming rather than iterating the transient bound. 
