---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public schedule and scratch addresses for live header recovery

A group's number and its incoming and outgoing cuts stay in external memory.
The stage order, allocated buffer sizes and per-stage limits are public. Each
bounded field scan consults the private descriptor before probing a site.


### `Sizes`

 The four field sizes selected before the simulation exponent is chosen.
The chain has height `h+1`. The exponent array has `e=tZ` individual bits. 

### `Sizes.h`

 The height parameter of the live chain, whose two halves each contain two to this power
  groups. 

### `Sizes.delta`

 The cut block width used to bound exterior and padding scans. 

### `Sizes.advice`

 The number of distributed advice bits copied into the live header workspace. 

### `Sizes.e`

 The number of bits allocated to each exponent payload. 

### `Sizes.config`

 The serialized bit length allocated to each evaluator configuration. 

### `Stage`

 The stages of header recovery, from copying index and advice through metadata, primed
indices, and per-field descriptor and scan calls. 

### `stages`

 Descriptors and their consumers always alternate. The two descriptor
words can therefore be reused for all eight fields. 

### `Sizes.capacity`

 The public number of positions available for scanning the specified incident field. 

### `calls`

 A finite bound on each stage's number of microcalls. A bounded scan
uses one last, zero-probe call at its public limit to hand off. 

### `probes`

 Per-stage local probes per active call, before the linking tag reads. 

### `callBound`

 Allocating both sides and each public bound costs only polynomially many
calls. No multiplicative factor of the number of sites occurs. 

### `costBound`

 The nested native stage dispatcher adds one tag probe per call and at
most one tag write at handoff. Including the enclosing dispatcher and the
call itself gives a bound of eleven cost units per call. 

### `widthAddr`

 Widths for the auxiliary header occupy three consecutive words. 

### `flagAddr`

 Address of the selected first, midpoint, first-half, or last flag in header scratch. 

### `firstTailAddr`

 Address of the scratch flag identifying the first evaluator group. 

### `tagAddr`

 Address holding the selected live-header mode tag. 

### `offsetAddr`

 Address of the scratch word giving the next incident field's source offset. 

### `countAddr`

 Address of the scratch word giving the next incident field's occupied length. 

### `borrowAddr`

 Address of the borrow bit carried through primed index construction. 

### `indexBase`

 Start of the unpacked one-based group index in header scratch. 

### `highAddr`

 The cell after the group-index digits recording the highest set-bit position. 

### `populationAddr`

 The cell recording the number of set bits in the group index. 

### `leftIndexBase`

 The first cell of the unpacked left primed index, after the index summary. 

### `rightIndexBase`

 The first cell of the unpacked right primed index, after the left index. 

### `adviceBase`

 The first advice cell after both primed index arrays. 

### `exteriorBase`

 The base of the reserved exterior payload interval on the selected incident side. 

### `exponentBase`

 The base of the selected side's exponent array after both exterior reservations. 

### `configBase`

 The base of the selected side's evaluator configuration array after the exponent arrays. 

### `limit`

 First address available to another module. The tag used to dispatch
among the header stages is at `base`, separate from the emitted mode tag. 

### `dest`

 The destination address of a copied incident payload, with a dummy zero address for padding
checks. 
