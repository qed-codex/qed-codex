---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyRelocated.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyRelocated.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyRelocated.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Greedy preparation from an active scheduler frame

The worker receives the slot numbers followed by eight current-level controls.
It loads those controls into registers and runs the shared native record writer.
Both color and tag directories use the same placement of public operands.


### `controls`

 Control indices are those of the original greedy preparation block. 

### `publicWords`

 Public operand bank consisting of the slot numbers followed by the eight relocated walk
controls. 

### `prepareCode`

 Preparation instructions that load the relocated controls before running the greedy record
builder. 

### `preparePass`

 Schedulable pass that builds the relocated greedy records and returns its cursor in
register zero. 

### `prepare_one`

 A frame-based preparation call writes the same label and record as the
original greedy initializer, including the pointer to the next record. 

### `prepare_directory`

 The completed native scan installs the directory from arbitrary initial
memory. All external probes go to the mate arrays, labels and records. 

### `prepare_valid`

 The preparation reports meet the linked worker's exclusive guard. Each
prefix writes only the walk allocation, so the stop, parameters and tag can
be read from the same external frame at every call. 
