---
{
  "module": "OAI/Computability/VPVNP/RAMSharedFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSharedFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSharedFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexing shared assignments by physical sends

A shared assignment in Lemma 10.1 consists of one successor message for each
of the first `S-1` sites and one sorting send per layer and site. The final
successor send and the initial successor receive are clamped. The following
equivalences retain exactly the bits of those actual messages.


### `SendIndex`

 Index of one transmitted bit, either on an internal successor wire or in a specified site’s
outgoing block for a sorting layer. 

### `sendBit`

 The physical source endpoint of each indexed send. 

### `indexOfSend`

 Recover the array indices of an actual sender from its endpoint. 

### `sendIndexEquiv`

 Bijection between successor-or-sorting array indices and their physical shared sender
endpoints. 

### `SendArrays`

 One successor vector for each internal boundary and one block vector for
each sorting exchange. Each array entry is the vector sent by the named site. 

### `sendArraysEquiv`

 Reindex an assignment on shared bits as the array of successor messages and the
layer-by-site array of sorting blocks. 

### `incidentEquiv`

 Reconstruct compatible incident fields from sender-indexed message arrays. 

### `incidentBits`

 Linear local bit address for a site's physical sender arrays. 
