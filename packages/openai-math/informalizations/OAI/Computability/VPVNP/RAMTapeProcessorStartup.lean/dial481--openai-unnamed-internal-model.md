---
{
  "module": "OAI/Computability/VPVNP/RAMTapeProcessorStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeProcessorStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeProcessorStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the live processor's public bank and initial-record words

Starting with only the raw site input, the program parses its literal prefix and fields,
computes the public bounds and the two cost endpoints, and zero-extends the parsed address
and four header bits into the two words used by the initial memory record.


### `recordResult`

 The two record words occupy their dedicated stacks in the prepared bank. 

### `recordResult_site`

 Every parsed input and tally in the setup bank survives the record preparation. 

### `recordResult_extra`

 All public output registers, including the empty shared scratch bank. 

### `recordStartup`

 Fixed processor preparation, including both words of the initial record. 

### `recordClockCoefficient`

 Clock coefficient for public startup including preparation of the initial record’s address
and header words. 

### `recordStartup_runs`

 The only initially occupied stack carries the complete input, including the program prefix.
On return all parsed fields, cost and fuel registers, and initial-record words are present. 
