---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenNoWrites.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenNoWrites.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenNoWrites.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External memory through a shrinking hidden-field scan

The scan reads the count, resident IDs, and selected term cells. It consumes
the field guesses and stores them privately. Every event sequence preserves
external memory, including an empty scan and arbitrary guessed field values.


### `fieldEvents_noWrites`

 One row reads its external headers and writes its guessed bits in the
private bit bank. 

### `events_noWrites`

 Arbitrary guessed fields leave every external word untouched throughout
the count probe, per-field loop and terminating test. 

### `after_events`

 The post-trace external memory agrees at every address with the supplied
memory, regardless of the owner or the encoded field values. 
