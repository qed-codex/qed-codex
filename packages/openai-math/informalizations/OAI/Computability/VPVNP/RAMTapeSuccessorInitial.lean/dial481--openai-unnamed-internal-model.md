---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorInitial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorInitial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorInitial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The public initial state at the first processor

After checking the incoming zero clamp, the first processor needs the public
initial word in its state register and a running flag. The word-copy scan
overwrites the destination while restoring the public word. The next two
instructions replace the top status bit and preserve the tail of that stack.


### `Port`

 Ports for copying the public initial word into the incoming state register and setting its
running bit. 

### `normalize`

 At an absent incoming edge, install the initial running configuration. 

### `normalize_runs`

 With two empty scratch stacks, normalization takes eight instructions per
word bit plus five fixed instructions, regardless of the old state and flag. 
