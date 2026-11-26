---
{
  "module": "OAI/Computability/VPVNP/CompressionBoundedBind.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBoundedBind.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBoundedBind.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composition of bounded compressor histories

When each branch of one compressor execution continues with a second execution,
the records of the combined execution consist of the original records of both
stages. Uniform local bounds are preserved and the selected chain lengths add.


### `StatePass.bounded_mono`

 A bound on a single pass may be enlarged without changing any records. 

### `bounded_mono`

 Enlarge the uniform bound throughout an execution tree. 

### `bindRecords`

 Append the actual continuation records at each leaf of an execution. 

### `bounded_bindRecords`

 A common bound on all elementary passes holds on every combined branch. 

### `length_more`

 Passing through one kernel adds one to the selected continuation length. 

### `exists_length_bindRecords`

 Each selected chain has the sum of the lengths of its actual prefix and suffix. 

### `length_bindRecords_le`

 Uniform bounds on the lengths of the two stages add after dependent continuation. 
