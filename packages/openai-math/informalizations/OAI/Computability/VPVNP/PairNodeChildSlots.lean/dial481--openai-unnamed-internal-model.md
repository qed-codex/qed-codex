---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling all half-wire arguments of a child

A finite scan enters the width and guess block at each of the old site's
outgoing slots, then its incoming slots. The fixed slot ordinal is added
to the first physical port. The destination cursor advances by the width
actually read at that port. The scan consumes exactly the semantic child
payload and leaves it in one private interval.


### `guessRegs`

 The first physical port of an old site is kept in register 8. 

### `Sites`

 Addresses of the instructions that compute the physical port, look up the field width, and
guess the field bits for each directed child slot. 

### `Sites.setup`

 The two instruction addresses that load the slot ordinal and add it to the site's first
  physical port. 

### `Sites.header`

 The six instruction addresses for the width lookup, including the inverse-incidence
  lookup on incoming slots. 

### `Sites.guess`

 The seven instruction addresses for guessing the slot's field and writing its bits to
  consecutive private cells. 

### `first`

 Entry address of the first slot's setup block, or the supplied return address for an empty
slot list. 

### `Names`

 Slot names can be read from a public operand or from a previously
initialized bank of private registers. Both reads take one local instruction. 

### `Names.load`

 The instruction that loads slot `j`'s ordinal into `dst` from its public operand or private
register and continues at `next`. 

### `Names.Valid`

 Every slot-name source holds its slot ordinal as a machine word in the public data or the
current register file. 

### `Names.Apart`

 The private slot-name bank is disjoint from the working registers. Public slot names impose
no register condition. 

### `setupWith`

 Load the slot ordinal, add the site's first physical port, then enter the outgoing or
incoming width lookup according to the slot direction. 

### `setup`

 The public-operand version of the two slot setup instructions. 

### `LinkedWith`

 The machine links each listed slot's address setup, width lookup, and field guess in
sequence and passes control to `ret` after the last slot. 

### `Linked`

 The slot scan is linked through its return address with slot ordinals supplied by public
operands. 

### `length`

 Total semantic field length in the specified part of the scan. 

### `bits`

 The guessed half-wire bits concatenated in the given slot order, with each field listed in
increasing bit index. 

### `events`

 The scan trace in slot order, recording two address-setup ticks, the incidence and width
lookup events for the slot direction, and the private field guess. 

### `scanWith`

 Ordered success and exact suffix. Every child slot, including an incoming
slot at a self-loop, consumes a separate segment of the stream. 

### `slots`

 All outgoing and then all incoming slots, including slots of width zero. 

### `length_all`

 The complete old site buffer exactly fills the cursor range. 

### `reject_shortWith`

 With too few bits some header eventually reaches an incomplete field. No
native suffix returns, regardless of the accepted bits in all earlier slots. 
