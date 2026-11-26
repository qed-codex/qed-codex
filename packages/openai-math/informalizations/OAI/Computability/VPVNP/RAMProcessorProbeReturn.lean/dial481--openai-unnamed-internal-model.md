---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeReturn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeReturn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeReturn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splicing a permitted external probe into a completed call

A successful probe contributes one unit of cost and one chronologically
stamped record. A later rejection remains a rejection even when earlier
probes wrote records into the site's private buffer.


### `ProbeLink`

 Accounting needed to prepend an admitted probe to a call return. It relates the two
snapshots' budgets and identifies the charged event's timestamped record ahead of the
continuation. 
