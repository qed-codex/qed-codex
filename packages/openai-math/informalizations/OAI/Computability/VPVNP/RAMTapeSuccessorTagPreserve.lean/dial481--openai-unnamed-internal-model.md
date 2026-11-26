---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorTagPreserve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTagPreserve.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorTagPreserve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a successor tag and restoring the input word

After classifying each bit, push it onto the temporary stack. Once the tag
has been decided, transfer those bits back. The caller receives the tag in
finite control and can still read the whole word.


### `KeepState`

 States for classifying a word while saving its bits, then restoring them with the tag held
in control. 

### `codeKeep`

 Classify the source word, move its bits back from scratch, and finish with its tag in
finite control. 

### `keep_run`

 Classify the source using an empty scratch stack. The two passes restore
all stacks after exactly four instructions per bit and two empty pops. 
