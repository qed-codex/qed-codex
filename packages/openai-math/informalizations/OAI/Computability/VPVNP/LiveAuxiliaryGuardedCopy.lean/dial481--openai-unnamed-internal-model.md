---
{
  "module": "OAI/Computability/VPVNP/LiveAuxiliaryGuardedCopy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryGuardedCopy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveAuxiliaryGuardedCopy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the indirect cursor guard on the complete sparse header copy

Each live call rereads the last descriptor's packed end. The source sweep
writes only its current sparse destination, so all descriptors retain their
values across the active calls. At the packed end one additional call reads
the limit and accepts.


### `lift_prefix`

 Add the four indirect-guard instructions to each call of a successful
source prefix. The two runs have identical memory at every return. 

### `guarded_copy_native`

 The actual auxiliary copy component performs one guarded call for every
populated word and one closing call. Its final memory is precisely the sparse
installation used by the virtual auxiliary machine. 
