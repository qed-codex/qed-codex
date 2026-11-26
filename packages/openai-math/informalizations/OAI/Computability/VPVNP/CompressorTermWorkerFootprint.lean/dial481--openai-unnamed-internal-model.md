---
{
  "module": "OAI/Computability/VPVNP/CompressorTermWorkerFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses accessed by a native term-worker pass

The two demand scans use the current input row. The payload reader probes the
repetition count just stored in the second descriptor header. All stores land
in the current descriptor. These event-level bounds let the same choices run
after a change to the scheduler's control memory.


### `call`

 At any successful call, even with an arbitrary tape and fuel, the worker
advances one ordinal. It reads its own demand row and repetition header and
writes exclusively in the term row. 

### `segment`

 The footprints of any contiguous segment are contained in the union of
its rows. The predicates can be widened to fit the scheduler's memory layout. 

### `strided_segment`

 With the paper's strided layout, every successful segment reads between
the first demand cell and the end of the descriptor arena. Its writes are
confined to that arena, including for a partial pass starting at a later row. 
