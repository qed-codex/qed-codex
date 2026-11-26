---
{
  "module": "OAI/Computability/VPVNP/RAMMemoryMessages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMemoryMessages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMMemoryMessages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The memory checks in a single site's transcript

Starting with its own padded records, a site verifies its outgoing messages,
replays the sorting layers using the prescribed partners, and checks reads
against preceding slots. Together these independent checks enforce the true
memory semantics and uniquely determine all sorting and last-record fields.


### `SortSends`

 Blocks of ordered record slots sent by each site at each cross-site sorting layer. 

### `MemoryMessages`

 All outgoing sorting blocks and the last sorted records passed along successor links for
the memory check. 

### `MemoryMessages.sortSends`

 Claimed outgoing record block for every site at every cross-site sorting layer. 

### `MemoryMessages.lastRecords`

 Claimed last record sent to each succeeding site for checking the boundary of its sorted
  block. 

### `outputAt`

 The final local block is computed from the local records and the incident
sort sends, with the receive for each cross-layer taken from its XOR partner. 

### `MemoryAt`

 The site passes its sorting-layer message checks and verifies its output reads using the
predecessor record at its block boundary. 

### `sortedBlock`

 The site's block after running the full sorting network, with each ordered slot projected
to its optional memory record. 

### `actualMemoryMessages`

 The genuine sorting messages and predecessor records, computed in their
order of use. 

### `memoryAt_iff`

 Local checks force both families of messages. The only remaining test is
the immediate-predecessor rule in the sorted array. 

### `report_memoryAt_iff`

 The memory transcript for the actual RAM record blocks. 
