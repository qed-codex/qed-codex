---
{
  "module": "OAI/Computability/VPVNP/RAMLocalWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLocalWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLocalWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pathwise work of a local RAM call

The bounds hold for every supplied bit stream, including a stream that ends
during a read, and every private state. A branch reserves one bit and a
permitted read reserves one word. The instruction and probe counters bound
the sum of these charges independently of whether the call succeeds.


### `runLocalCall_bounds`

 Pathwise bounds on dispatches, charged probes and reserved bit slots. 

### `runLocalCall_totalWork_le`

 Counting one unit per dispatch, per charged probe and per reserved bit. 

### `runChargedCall_bounds`

 The startup unit leaves one fewer probe slot in each of the three
allowances. If any allowance is zero the call uses no slots at all. 

### `runChargedCall_totalWork_le`

 Work of the charged interpreter on an arbitrary private bit stream. 

### `runChargedCall_probes_eq`

 On success, the accumulated counter gives the report's probe count. The
site loop can advance its charge using this counter without scanning events. 
