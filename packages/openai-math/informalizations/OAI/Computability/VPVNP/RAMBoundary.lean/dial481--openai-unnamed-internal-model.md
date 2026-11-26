---
{
  "module": "OAI/Computability/VPVNP/RAMBoundary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBoundary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMBoundary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Last-record fields in the distributed RAM transcript

In Lemma 10.1 each interior successor link carries the final physical slot of its
source's sorted block. The receiving validator uses this slot as the predecessor
of its first record. Flattening the blocks gives precisely the same read checks.


### `Sends`

 Each interior successor edge has one shared last-record field. 

### `flat`

 Physical slots in site-major order. 

### `lastSlot`

 Last slot of a nonempty block, including its padding if present. 

### `actual`

 The fields prescribed by the final sorted blocks. 

### `outgoing`

 The physical send at the final site is clamped. 

### `receive`

 An incoming field is the preceding site's shared send. The first receive
has the clamped value, so a read with no preceding write must return zero. 

### `singleton_clamps`

 At a singleton site both endpoint fields are clamped and there are no interior sends. 

### `checkAt`

 The validator checks each read using its incoming field and, when a successor
exists, checks its outgoing field against its own final physical slot. 

### `checks`

 Apply the one-site validator to the corresponding block of the sorted array. 

### `checks_iff`

 The outgoing checks force the complete assignment of interior fields.
The remaining site checks are equivalent to one scan of the physical array. 

### `existsUnique_checks_iff`

 Exactly one shared last-record assignment passes all the local checks
when the flattened physical array passes its global predecessor check. 
