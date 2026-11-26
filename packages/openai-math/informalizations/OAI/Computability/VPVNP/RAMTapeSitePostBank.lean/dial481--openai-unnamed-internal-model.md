---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePostBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The shared bank for sorting and checking the predecessor records 

### `Extra`

 Additional post-pass ports for the previous boundary record, sent boundary record, and
unary address width. 

### `Port`

 Combined bank for the sorting stages and the boundary-record checks. 

### `bank`

 Extend a sorting bank with serialized predecessor and sent records and the unary address
width. 

### `blockPort`

 Port carrying the serialized block currently being sorted or checked. 

### `widthPort`

 Unary word-width port shared by the sorting row and boundary scanner. 

### `slotsPort`

 Port holding the unary number of slots in the local sorting block. 

### `flagPort`

 Port collecting the validity flags produced during sorting. 

### `addressPort`

 Port holding the site address bits for the sorting pass. 

### `incidentPort`

 Port carrying the remaining incident bits to the sorting row’s receive stream. 

### `addressWidthPort`

 Unary site address width retained for initializing the sorting schedule. 

### `previousPort`

 Port containing the serialized incoming predecessor record. 

### `sentPort`

 Port containing the serialized record sent at the outgoing boundary. 

### `boundaryPorts`

 Connect the final boundary scanner to the sorted block, endpoint records, word width, saved
bits, and slot count. 

### `terminal`

 Run the final site-boundary decision and check the flags collected during sorting. 

### `initialBank`

 Sorting and boundary bank at the initial schedule position, with the full incident tail
available. 

### `finalBank`

 Sorting and boundary bank at the final schedule position, with the incident tail exhausted. 
