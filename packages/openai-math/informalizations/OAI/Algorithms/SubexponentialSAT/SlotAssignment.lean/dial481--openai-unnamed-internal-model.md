---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SlotAssignment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SlotAssignment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SlotAssignment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Incidence slots and globally consistent factor words

Section 5.4 assigns each coordinate's incident factors to different slots.
The same factor word is then used at every incidence of that factor.  The
slot numbers themselves need not agree at different coordinates.

The ordered constructor and the slot-filling operations are computable.  An
additional constructor for arbitrary finite factor types chooses an enumeration.
No running-time bound or probabilistic independence assertion is hidden here.


### `Incident`

 The actual factors incident to one coordinate. 

### `SlotMap`

 An injective slot assignment separately at each coordinate. 

### `card_incident_le`

 The incidence bound supplies exactly the cardinal inequality needed for slots. 

### `slotsOfCardLE`

 A finite slot assignment, using a chosen enumeration for each incident set. 

### `slotsOfBounded`

 Slot assignments exist for every bounded factor pattern. 

### `orderedSlotsOfCardLE`

 For ordered factor indices, sort the incident factors and use their ranks.
This constructor makes the fixed local ordering in the exposition explicit. 

### `orderedSlotsOfBounded`

 Computable slot assignment for a bounded pattern with ordered factor indices. 

### `Unused`

 Slots not used by the given embedding. 

### `preimage`

 Search the finite incident set for the unique factor assigned to a used slot. 

### `slotIndexEquiv`

 Every slot is uniquely either an incident-factor slot or an unused slot. 

### `slotWordsEquiv`

 Incident words and independently specified unused words are exactly all slot words. 

### `fillSlots`

 A convenient extension allowing padding values for all slots; used-slot
padding is ignored. 

### `card_incident_add_unused`

 The local seed correspondence has exactly the expected finite size. 

### `localTypeEquiv`

 Adding the independent head word gives precisely one universal type.
This finite equivalence is the local combinatorial input to uniformity proofs. 

### `typeFromWords`

 Create a coordinate type from one global word per factor and free local data. 

### `typeFromWords_incidence`

 All incidences of a factor read that same factor's global word. 

### `factor_word_consistent`

 The local slot numbers may differ at two incidences; their full words agree. 

### `typeFromWords_congr`

 Dependence on the global word assignment is confined to incident factors. 
