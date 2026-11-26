---
{
  "module": "OAI/Computability/VPVNP/RAMRecordIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Row-major indices for grouped transcript records

The initial record array of Lemma 10.1 has one fixed-width block per group.
Flattening those blocks reads the global array in increasing address order.


### `flatten_ofFn_blocks`

 Reading consecutive aligned blocks enumerates exactly the entries of the large block. 

### `getElem`

 Look up a slot in the flattened array by its group index and within-group offset. 
