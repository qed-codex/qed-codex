---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorPrelude.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPrelude.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPrelude.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing and entering the complete burst-site graph

A freshly parsed site has empty architectural registers. The prelude creates
width-correct zeros in those registers and stages the five-word initialization
record. The caller supplies the zero-extended site address and the four-bit
header packed in a word, exactly the values produced by the input preparer.


### `Snapshot.bare`

 Stack bank of a freshly parsed site, with empty private register stacks ready for
initialization. 

### `Snapshot.withInitFields`

 Stage the initialization record's tag one, saved site address and zero probe ordinal in the
snapshot. 

### `boot`

 Initialize the private registers and write log for a fresh call, then stage the
initialization record fields. 

### `graphDone`

 Test whether the control is at the site graph's successful completion label. 

### `graphRoutine`

 Normal graph completion transfers the padded block to the next local
validator. A rejecting row halts the entire path. 

### `callSite`

 Boot a freshly parsed site and execute its graph from initialization-record emission
through successful completion or rejection. 
