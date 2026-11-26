---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCodeAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCodeAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeCodeAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `rowInputs`

 The original physical row stage, independent of either old code-search
controller: inputs are the actually retained new search results. 

### `command`

 Native code construction uses the metadata producer and both streamed
searches before physically serializing their retained matrices. 

### `metadata_value_bound`

 Every numeric code dimension is already represented by a physical
unary word at the metadata boundary; its value is bounded by that word cap. 

### `metadata_bound_pos`

 The stored vertex word is nonempty, so a true metadata boundary has a
positive physical bound even in a zero-dimensional code. 

### `serializer_trace_space`

 Serialization is an actual polynomial-time phase, including its routing
and complete lower-bank cleanup, so instruction growth also bounds its prefix
storage. The preceding searches never use this argument. 

### `afterMetadata_eval`

 Concrete metadata words feed both searches and the serializer. The
serializer consumes exactly the matrices returned by those searches. 

### `command_eval`

 All physical services in code construction are instantiated. The exposed
intermediate state is the actual metadata-stage result and carries its proved
word cap for the later uniform numerical comparison. 
