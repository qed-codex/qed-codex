---
{
  "module": "OAI/Computability/VPVNP/SlotBitCounts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBitCounts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBitCounts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Independence of the color bits in Appendix C

A position in Lemma C.1 of *VP and VNP differ over every field* has one bit
per base color and a separate outgoing-slot coordinate. Fixing the endpoint
types of a translated arc fixes precisely two distinct color bits.


### `freeBits`

 Restricting a function away from its prescribed coordinates forgets exactly
the values that are forced. 

### `card_prescribedBits`

 Exact number of bit vectors with prescribed values on any subset of colors. 

### `card_oneBit`

 One endpoint test cuts the color vectors in half. 

### `card_twoBits`

 Prescribing the two endpoint types fixes two independent color bits. 

### `card_translatedBits`

 An arc translation may displace either endpoint test. 

### `card_translatedBits_slots`

 Free choice of the independent outgoing slot multiplies the endpoint count
by the degree. 
