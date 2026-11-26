---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrefixReject.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefixReject.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefixReject.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Rejection at a reached stage excludes all accepting live-header paths 

### `nativeStage`

 The single native header stage instantiated with its own row of public operands. 

### `nativeHeader`

 The complete linked header program instantiated at the given word width and workspace base. 

### `StagePrefix.suffix_of_accepted`

 For a deterministic successful prefix, an accepted path would have to
continue from its verified postmemory, persistent word zero, and actual tag. 

### `StagePrefix.rejects`

 If the reached component has no accepting source segment, its native
linker cannot advance beyond that stage or accept. Continuing source calls
only need to preserve the one reserved stage-tag word. 

### `StagePrefix.rejects_entry`

 Immediate rejection at a mode check needs no assumptions on that
component's behavior at other memories. 
