---
{
  "module": "OAI/Computability/VPVNP/LiveExponentPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native path multiplicity and resource bounds of exponent addition

For any initialized buffers the exponent stage accepts either once or zero
times. A successful run has one data call for every physical cut digit, one
accepting end call, and no binary choices. The count covers all finite native
call streams, including streams of unintended lengths.


### `stageReports`

 All successful digit reports followed by the accepting call. 

### `pathCount`

 The cardinality of native accepting paths for any report cap. 

### `stageResources`

 Total native cost, call count and per-call clock/probe bound. 
