---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Materializing the site's initial sorting block

The site reserves space for four slots per unit of bucket capacity and writes
its header and probe records there in chronological order. Every event is
visited once. The write pointer supplies the probe count of a completed call.
Unwritten slots read as padding.


### `appendEvents`

 Append five words on a probe, leaving private instructions and choices out
of the sorting block. The work includes the event test and loop control. 

### `recordBuffer`

 The array view uses a single constant-time indexed lookup. Missing slots
have the same zero-padding meaning as the full length-`4H` representation. 

### `recordBuffer_work`

 On all report lists returned by the site, the single-pass collection takes
at most a constant number of word operations per simulated instruction. 
