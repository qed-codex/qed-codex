---
{
  "module": "OAI/Computability/VPVNP/LiveConfigGatherRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGatherRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGatherRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The complete native configuration-gather scan

The persistent cursor visits every destination exactly once. Each successful
completion consists of one empty choice list per word. The individual reports
identify the actual writes and permit replay on the live group's external memory.


### `machine`

 Instantiate the gathering table on the live public operands to obtain its executable RAM
program. 

### `wordReport`

 The gather report for one indexed word of a configuration, using that word's index as the
persistent cursor. 

### `run_words`

 Exact choices and reports of a complete execution, for an array of
words whose source bits survive the earlier writes. 

### `run_array`

 Exact native completion and memory replay for the unpacked live cut:
the stage admits one deterministic transcript and installs every decoded
word in the destination bank. 
