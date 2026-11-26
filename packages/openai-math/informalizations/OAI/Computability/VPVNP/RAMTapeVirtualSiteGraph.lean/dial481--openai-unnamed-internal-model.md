---
{
  "module": "OAI/Computability/VPVNP/RAMTapeVirtualSiteGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeVirtualSiteGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeVirtualSiteGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The call graph on the parsed site's own incoming and outgoing fields

The controller emits a full-word initialization record for its auxiliary site. From
that bank the call loop tests its incoming cost bucket, simulates the private
instructions, checks the outgoing cut and closes the ordered record buffer.


### `Input.initSlot`

 Initialization record for the actual auxiliary site's address and header word. 

### `Input.staged`

 Fresh processor snapshot with its initialization fields in place. 

### `Input.entered`

 Snapshot after the native graph emits its first memory record. 

### `Input.validated`

 Auxiliary site reports accepted on the nominated private choice string. 

### `graphBudget`

 Work bound for initialization, interpreting all calls and closing the site. 

### `Input.GraphOutcome`

 Acceptance or rejection of the actual stack graph on the supplied private choices. 
