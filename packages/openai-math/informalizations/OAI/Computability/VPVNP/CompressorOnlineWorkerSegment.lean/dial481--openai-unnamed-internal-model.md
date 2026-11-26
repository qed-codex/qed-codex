---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineWorkerSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineWorkerSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineWorkerSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Extracting the source pass from an arbitrary accepting online run

Each active worker call contributes its original choice tape and complete
source report. After its closing guard, the remaining native calls run from
the calendar with precisely the memory produced by the recovered pass.


### `WorkerStep`

 The source pass preserves its public frame and returns a live cursor on
each active step. A caller may keep a stronger data-memory invariant and a
smaller source cap. No restriction is placed on the choice list. 

### `recover_worker_segment`

 Recover one whole pass and the actual suffix, including the empty closing
call. A zero-length pass still consumes exactly that closing call. 
