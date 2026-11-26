---
{
  "module": "OAI/Computability/VPVNP/RAMLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The communication fields of the RAM transcript

Lemma 10.1 of *VP and VNP differ over every field* uses two successor fields and
two fields for each cross-site sorting layer. We number the layers in phase order,
with decreasing stride within each phase. A field bit has a contiguous local
offset and either a unique matching bit at another site or a prescribed zero.


### `layerCount`

 Number of cross-site layers for `2^d` sites. 

### `Layer`

 In phase `h + phase + 1` of an array with `2^h` positions per site,
the cross-site strides decrease from `2^(h+phase)` to `2^h`. 

### `Layer.phase`

 Zero-based phase of the cross-site sorting network, below the number of site-index bits. 

### `Layer.step`

 Zero-based step in a sorting phase, ranging from zero through the phase number in
  decreasing stride order. 

### `Layer.siteBit`

 Site-index bit flipped to find the partner at this layer, equal to the phase number minus
its step. 

### `Layer.ordinal`

 Translate a cross-site layer to its ordinal among all exchanges. 

### `layerAt`

 Decode a layer ordinal by comparing against one triangular prefix per phase. 

### `layerEquiv`

 Bijection between physical sorting layers and their consecutive field numbers. 

### `blockBits`

 One block in a sorting direction contains five words per padded record. 

### `Slot`

 Successor fields carry status, cost, state, and one final five-word record.
The direction is zero for send and one for receive. 

### `width`

 Number of incident bits at one site, counting both successor fields and a send and receive
block at every cross-site sorting layer. 

### `width_eq`

 Equation (10.1), with `d = log₂ S`. Both endpoints reserve both successor fields. 

### `width_le`

 A uniform constant in the asymptotic estimate of (10.1), with `H = 2^e`
and `S = 2^d`. The sort has `log₂ (4HS)` phases. 

### `offset`

 A contiguous, invertible bit address: the two successor fields precede the
send/receive field pair for each sorting layer in chronological order. 

### `Layer.partner`

 The common partner of all records sent by a site at this layer. 

### `peer`

 The missing successor send at the last site and receive at the first site
are represented by `none`. All other bits have one peer with opposite direction. 

### `direction`

 Direction of an incident bit, in both parts of the layout. 

### `peer_reverse`

 Each actual connection pairs two ports and can be traced from either end. 

### `Endpoint`

 One incident bit position specified by its site and its local communication slot. 

### `IsSend`

 Shared assignments carry one bit per existing send. There is no independent
assignment to a clamped field or to the receiving copy of a shared bit. 

### `SharedBit`

 A sending endpoint of an existing link, indexing the one Boolean shared with its matching
receiving endpoint. 

### `source`

 Locate a port's bit in the array of sends. A missing endpoint is zero. 

### `Compatible`

 Clamps and pairwise equality are exactly the constraints on incident bit values. 

### `assignmentEquiv`

 Shared assignments and compatible incident assignments have equal multiplicities,
including the one-site case where both successor fields are clamped. 
