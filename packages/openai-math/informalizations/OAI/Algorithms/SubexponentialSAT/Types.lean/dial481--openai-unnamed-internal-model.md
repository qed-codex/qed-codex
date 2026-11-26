---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Types.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Types.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Types.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Universal types

A universal type records a head word and one word per incidence slot.  The
head selects the side of the coordinate, whereas a slot records a factor color.
This file proves the sizes of the type universe and the one- and two-bit fibers
using explicit equivalences.


### `Word`

 A binary word indexed by interpolation positions. 

### `UniversalType`

 One head word and `Δ` slot words. No relation is imposed between their bits. 

### `equivProd`

 Explicit presentation as a Cartesian product of independent word spaces. 

### `blockSize`

 The size `N` of the complete universal block. 

### `side`

 Head side at a fixed interpolation point. 

### `joint`

 Joint head-and-slot fiber, denoted `J(t,g,i)` in the exposition. 

### `pinHead`

 Replace just one head bit. 

### `pinSlot`

 Replace just one bit of one slot. 

### `fullSideEquiv`

 Removing the chosen head bit leaves exactly one free Boolean bit. 

### `sideJointEquiv`

 Within a head side, removing the selected slot bit leaves one free bit. 

### `fullJointEquiv`

 The two pinned bits are independent, giving two free Boolean factors. 

### `card_side`

 Each head side contains exactly half the universal types. 

### `card_joint`

 A fixed head and a fixed slot color occupy exactly one quarter of the types. 

### `OtherPosition`

 All interpolation positions except the one fixed by a joint fiber. 

### `OtherSlot`

 The slots not used in the active head--slot pair. 

### `jointEquivPairs`

 A joint fiber is a product of independently free head--slot pairs at the
other positions, together with the completely untouched other slot words.
The two Boolean coordinates at the fixed position are restored as `g`. 

### `card_joint_via_pairs`

 The tensor-factor cardinality form used in spectral multiplicity counts. 
