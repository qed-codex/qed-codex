---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePostPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical connection from the call loop to the local memory pass

The sorter reads the call loop's completed record buffer and the shared
guard's two predecessor records. Its address, width, slot count and remaining
incident tape use the original parser registers. All sorting scratch has its
own labels.


### `postPorts`

 Connect sorting input to the call loop’s output, reuse the parsed fields and guard records,
and assign separate ports to sorting scratch. 

### `installCall_post`

 A physical call replaces only the occupied input block of the sorter. 

### `post`

 Run the complete local sorting and memory-checking pass on the processor’s connected ports. 
