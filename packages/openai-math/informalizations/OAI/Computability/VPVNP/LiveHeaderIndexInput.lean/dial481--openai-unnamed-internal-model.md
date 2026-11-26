---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderIndexInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderIndexInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderIndexInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the index in the physical live-group headers

Group `g` in the contraction has one-based number `g.val + 1`. Its bits
occupy slot zero of the first `h+2` processor headers. The native scan reads
those packed words and writes only its designated scratch, leaving all four
fields of every processor header available to the later phases.


### `IndexFrame`

 Only the copy buffer and the two summary words can change. 

### `index_scan_native_framed`

 The original scan invariant and the full memory frame hold on the same
deterministic segment. 

### `physical_index_bit`

 Slot zero of each occupied processor holds the corresponding bit of the
one-based group number, including the highest bit of the last group. 

### `physicalMemory`

 The actual memory installed for a live group in the contraction. 

### `physicalMemory_word`

 Readback of all four physical header bits as their original packed word. 

### `PhysicalIndex`

 Exact summaries and bit arrays available to the live program after the
scan. All later reads of the site headers see the prescribed physical words. 

### `physical_index_scan_native`

 Run the index scan starting at the actual header memory of the group,
with its two scalar scratch cells initially zero by RAM initialization. 
