---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordering actual compressor arc records at each endpoint

In a single endpoint fiber the high-order relative key already distinguishes
all genuine arcs. Hence adding the absolute lane as a low-order address digit
preserves their order. The padding records come afterwards, in dummy-number
order at the unique dummy source for this fiber.


### `endRole`

 The orientation bit selects the outgoing (false) or incoming (true) role. 

### `dummyEnd`

 From the source site of a dummy, recover its site at the selected end. 

### `actualEnd`

 The actual endpoint used as the owner of an arc record's field. 

### `paddedBaseId`

 Base identifier used by the regularized slot permutation. 

### `address_lt_iff_relative`

 The absolute-address comparison in one genuine endpoint fiber is exactly
the comparison of the two relative keys used by the base slot numbering. 

### `actualEnd_card`

 Every actual endpoint has all the surviving slots and every padding slot. 

### `addressRank`

 A zero-based position within the endpoint row obtained by scanning the
entire numeric address space. 

### `addressRank_eq_slot`

 Address order in either endpoint fiber agrees with the full regularized
slot indexing, both on genuine arcs and on the dummy tail. 
