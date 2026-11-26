---
{
  "module": "OAI/Computability/VPVNP/RAMRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological probe records of a burst RAM execution

In Lemma 10.1 each external read or write emits a five-word record, carrying
its call's starting cost and its ordinal among the probes of that call.
Internal steps and binary choices produce no records. These timestamps are
strictly increasing, and the record-level memory checks recover the read
semantics of the original events.


### `countProbes`

 The number of external word probes made by the events. 

### `Report.probes`

 Number of external read and write events in this call report. 

### `eventRecords`

 Probe ordinals start at zero and advance only at external reads and writes. 

### `probeRecords`

 All non-initialization records emitted by the sequence of calls. 

### `readsCorrect_probeRecords`

 Checking all read records chronologically is equivalent to checking the
actual events, starting from any prescribed external memory. 

### `padded_read_check`

 The sorted-record check in Lemma 10.1 tests precisely the read answers of
the original call reports, including the first read at an initialized address. 
