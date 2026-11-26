---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderFieldRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldRuns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native payload scans of the incident cuts

Each completed field scan copies exactly the specified interval to the
designated buffer. Every word outside that buffer still has its input value.
Source intervals refer to the original packed processor headers.


### `FieldCopy`

 The prefix written to scratch, together with a frame for all other cells. 

### `copy_field_native`

 A fixed, fifteen-instruction table copies every bit of the occupied source
field and preserves all memory outside the destination. Each step has three
probes. Empty fields have the empty execution and leave all cells intact. 

### `padding_step`

 The guard reads two words and returns the next cursor precisely on a zero
bit. Its successful trace leaves memory untouched. 

### `padding_native_iff`

 On arbitrary cut input, the full padding scan succeeds exactly if every
padding bit is zero. It touches only the specified interval, even on malformed input. 

### `padding_native`

 Every successful padding call has precisely two probes, and its entire
segment preserves every cell. 
