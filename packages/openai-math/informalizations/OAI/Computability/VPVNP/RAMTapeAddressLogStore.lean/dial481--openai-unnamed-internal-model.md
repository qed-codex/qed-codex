---
{
  "module": "OAI/Computability/VPVNP/RAMTapeAddressLogStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prepending a private RAM write

The forward pass transfers the address and value to two scratch stacks. The
return pass restores the input words and pushes a copy of each bit onto the
corresponding log stream, low bit first in the completed log. A final marker
records the entry, including when both words have width zero.


### `StoreState`

 States for saving the new address and value, restoring their input stacks, and prepending
the write to the log. 

### `storeCode`

 Stack instructions that prepend the address and value to the log and push an occupancy
mark, including for zero-width words. 

### `store_run`

 A private store preserves the source words and realizes exactly one cons
of the native newest-first `WriteLog`, in a number of steps independent of
its previous length and of the numerical address. 
