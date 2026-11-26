---
{
  "module": "OAI/Computability/VPVNP/RAMRecordOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMRecordOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic comparison of complete RAM record slots

The sorting network moves a whole five-word record at each comparison.
The address and timestamp decide the primary order. When keys tie, the
kind and value distinguish the remaining payload using fields already in
the record. The unique empty slot sorts after every nonempty one.


### `Kind.code`

 Tie-breaking rank of an initialization, read, or write in the sort order, numbered zero,
one, and two respectively. 

### `OrderedSlot`

 Physical record with the network's deterministic total order. 

### `OrderedSlot.record`

 Optional memory record at a sorting wire, with the empty option representing a padding
  slot. 

### `OrderedSlot.code`

 Lexicographic sorting key for an occupied slot, using address and timestamp followed by
kind rank and value. Padding sorts above every record. 

### `paddedKey_mono`

 Every ascending comparator output is ascending in the paper's primary
key even when a tie required consulting the remaining fields. 
