---
{
  "module": "OAI/Computability/VPVNP/RAMTapePrivateISABank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISABank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePrivateISABank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Staging registers on the private-log ports

The private load and store routines share two staging words. All remaining
architectural ports retain their values while the log kernel is running.


### `stagedBank`

 A bank in which the query and output log ports are occupied. 

### `install_logBank`

 Installing the ten streams of a native log routine replaces precisely
the staged query, output, and log. The ambient registers are preserved. 
