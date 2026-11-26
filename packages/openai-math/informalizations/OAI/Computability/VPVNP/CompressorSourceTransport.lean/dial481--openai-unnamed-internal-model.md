---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transporting native source runs across scheduler writes

The online calendar changes its control cells between calls. If the
original reports read only data cells, the same worker produces exactly
the same reports in any memory agreeing on those cells. Every prefix of
the run preserves the data agreement. A separate write condition preserves
the scheduler's control cells throughout the source scan.


### `Agree`

 The two memories return the same word at every address satisfying the data predicate. 

### `Reads`

 Every read recorded in the event list addresses a cell satisfying the data predicate. 

### `Writes`

 Every write recorded in the event list addresses a cell satisfying the data predicate. 

### `segment`

 The sequence of native calls is identical under any changes to addresses
outside its read region. Private state resets and branch choices are included. 

### `after_outside`

 No call in the native segment changes a cell outside the permitted writes. 

### `after_control`

 Inserting a prefix of online control writes leaves the original source
run executable and all of its data cells identical in the resulting memory. 
