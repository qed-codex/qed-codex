---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteGraphInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteGraphInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteGraphInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The call graph on the parsed site's own incoming and outgoing fields

The controller first emits the compulsory local initialization record. From
that bank the call loop tests its incoming cost bucket, simulates the private
instructions, checks the outgoing cut and closes the ordered record buffer.


### `Input.initSlot`

 Compulsory first record built from the parsed address and header words. 

### `Input.staged`

 Controller snapshot after fresh-call initialization and staging the address for the
compulsory record. 

### `Input.entered`

 Controller snapshot immediately after emitting the site’s compulsory initialization record. 

### `Input.validated`

 Abstract site validation for the instantiated program, actual incoming and outgoing
summaries, and the given private choice bits. 

### `graphBudget`

 Budget for initial-record emission, all bounded site calls, and closing the padded record
buffer. 

### `Input.GraphOutcome`

 Execution outcome matching abstract site validation. Failure reaches rejection, and success
closes the initialization record followed by the probes in order. 
