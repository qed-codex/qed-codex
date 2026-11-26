---
{
  "module": "OAI/Computability/VPVNP/RAMTapePhysicalHalting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePhysicalHalting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapePhysicalHalting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All-branch stopping of the literal stack interpreter

The deterministic seek and restore sequences implementing each stack operation
are followed along their actual table records. Each binary virtual choice
branches at a single literal row. Thus the same quadratic clock that bounds
the accepting-leaf count also bounds the duration of rejecting paths.


### `AllHalt`

 Every path of the literal table has stopped within the given clock.
A row with no successor rejects; the two distinguished terminal states halt
immediately, independently of the remaining clock. 

### `Runs.allHalt`

 A deterministic tape macro consumes exactly its run length. 

### `physical_allHalt`

 Lift the virtual all-path bound to the binary transition table. 

### `input_allHalt_labeled`

 On the actual raw input, every branch of a named stack program has halted
by the same quadratic clock used for its exact integer path count. 
