---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeLoopSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeLoopSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeLoopSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed node loop consumes the producer's framed cursor. Each actual
node execution supplies its own emitted coefficient word; no uniform choice
of byte representatives across register states is required. The indexed
invariant carries the complete retained query context between nodes. 

### `initialized_boundary`

 The actual initializer derives the first physical loop boundary from
the produced framed master, including an empty coefficient stream. 

### `initialized_frame`

 Retained ring words, cache masters and high-assignment data outside the
listed physical writes pass through node initialization unchanged. 

### `loop_eval_prefix`

 Induct on the number of physical node records still to be read. The
output list is a proof witness only; the machine retains the flat stream863.
All component prefixes share one cap, independent of the number of nodes. 

### `loop_resources`

 A single actual run emits all node words in order and halts with the
framed cursor empty, the exact unary node index, and the original boundary cap.
The final halt is included in both time and every-stack prefix bounds. 

### `guard_prefix_bound`

 The physical guard only reads the cursor. Its single instruction cannot
enlarge either an active stack or a preserved caller word. 

### `nodes_eval_prefix`

 Paid cursor initialization and the real initial guard precede the same
node loop. Dirty entry buffers are charged by the existing initializer, and
the accumulated stream starts empty before the first node is evaluated. 

### `nodes_resources`

 Add the one actual halt step to the same initialized node run. 
