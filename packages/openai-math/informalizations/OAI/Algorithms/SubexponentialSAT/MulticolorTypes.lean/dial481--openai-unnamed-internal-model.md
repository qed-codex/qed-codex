---
{
  "module": "OAI/Algorithms/SubexponentialSAT/MulticolorTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MulticolorTypes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MulticolorTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multicolor universal types and consistent incidence slots

The number `r` of colors is an explicit natural parameter throughout. No
finiteness instance or cardinality identity treats it as a fixed constant.
The joint fiber uses a head color different from the selected slot color,
as required by Sections 3.1 and 3.4 of the subexponential construction.


### `natCard_universalType`

 The cardinality form independent of the chosen `Fintype` instance. 

### `card_universalType_rat`

 Cast form used by the rational deviation and block-threshold inequalities. 

### `Spectator`

 Coordinates not changed by the swaps at positions other than `t`. 

### `jointEquivPairs`

 A joint fiber is the product of free head--slot pairs at all other
positions and the untouched slot color at `t` and all other slot words. 

### `ExactJoint`

 Auxiliary fiber with both selected colors pinned to `g`. 

### `jointExactJointEquiv`

 A mismatch joint has `r-1` possible selected slot colors, all with the
same remaining free coordinates as the auxiliary pinned fiber. 

### `card_joint`

 The mismatch joint occupies exactly `(r-1)/r²` of the block. 

### `card_joint_mul_sq`

 Division-free form of the exact joint-size identity. 

### `typeFromWords`

 The color-independent slot embeddings of `SlotAssignment` are reused. 

### `localTypeEquiv`

 The exact local product correspondence remains valid for growing `r`. 
