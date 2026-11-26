---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedyPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing a greedy vertex record in a fresh burst call

Eight header words in external memory identify the current level's mate,
displacement and assignment arrays, its first record, and the record stride.
One finite instruction table uses the persistent vertex index to initialize
its label, write the two header fields and emit all operand rows. It returns
the next vertex index. The public slot-number table is independent of the
graph, the current level and the word width.


### `controlWords`

 The eight control words for preparing a greedy record, including its first address and its
stride of two header words plus operand width. 

### `prepareBody`

 The shared record writer runs once the eight controls occupy registers 2 through 9. 

### `prepareCode`

 Native preparation code that loads the eight control words and initializes the vertex
record and its operand rows. 

### `prepareMachine`

 Instantiate the record-preparation machine with the given word width and public slot-number
table. 

### `GraphOutside`

 Both directed mate arrays are outside the entire prepared directory. 

### `prepareBody_trace`

 Installing a vertex record from loaded controls. Both the low-address
initializer and the scheduler's frame-based initializer run this same suffix. 

### `prepare_one`

 The call installs the complete record and clears the corresponding mutable
label. All inputs other than the fixed slot numbers come from external memory. 
