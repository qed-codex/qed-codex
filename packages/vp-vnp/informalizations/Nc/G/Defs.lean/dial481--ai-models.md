---
{
  "module": "Nc/G/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The cut from general exchange identities: definitions

A law has roles, slots (one bit per block, seen by the two roles at the ends of the slot), channels (strings shared by
two roles) and an index: the product of the equalities of the two copies of the bit of every slot is a sum, over
indices and strings, of products of tables of the roles. A move has a law and a party for every role. In a move `t`
units are given at every slot (missing units are replaced by zeros), and the strings on a channel (a label and the
string of the law for every block) are cut into new units.


### `Law`

 A law. 

### `Law.Ro`

 roles 

### `Law.Sl`

 slots 

### `Law.Cn`

 channels 

### `Law.I`

 indices 

### `Law.a`

 one end of a slot 

### `Law.b`

 the other end of a slot 

### `Law.c`

 one end of a channel 

### `Law.d`

 the other end of a channel 

### `Law.lam`

 length of labels 

### `Law.lab`

 labels 

### `Law.len`

 lengths of strings 

### `Law.tab`

 the tables: a role sees the bits of its slots and the strings of its channels 

### `Law.law`

 the identity 

### `Law.conn`

 indices that agree along channels are equal 

### `SlAt`

 The slots of a role. 

### `CnAt`

 The channels of a role. 

### `slEnd`

 The role at an end of a slot. 

### `cnEnd`

 The role at an end of a channel. 

### `Sys`

 The moves: a law, and a party for every role. 

### `Sys.kind`

 the law of a move 

### `Sys.part`

 the parties of a move 

### `R`

 All roles. 

### `Z`

 All slots. 

### `N`

 All channels (new bundles). 

### `rp`

 The party of a role. 

### `zr`

 The role at an end of a slot. 

### `nr`

 The role at an end of a channel. 

### `zp`

 The party at an end of a slot. 

### `np`

 The party at an end of a channel. 

### `Uid`

 Names of units. `init a b k`: unit number `k` of the string from party `a` to party `b` (only the `A` base parties
have strings at the beginning); `new ν k`: unit number `k` of the channel `ν` of a move. 

### `Uid.init`

 initial unit 

### `Uid.new`

 unit made by a move 

### `cparty`

 The holders of a unit (`np`: the parties at the ends of the channels). There are `A` base parties and `A'` extra
parties. 

### `hold0`

 First holder of a unit. 

### `hold1`

 Second holder of a unit. 

### `allIds`

 All units, in the order of the enumeration. 

### `unum`

 The number of a unit in its string. 

### `ucnt`

 The number of units of the string to which a unit belongs. 

### `seen0`

 The units at the beginning. 

### `newUnits`

 The new units of move `x` for the outcome `o`. 

### `slotBits`

 The bits given at a slot: the bits of the units, and zeros up to `t` units. 

### `chString`

 The string on a channel: for every block the label and the string of the law. 

### `ChOk`

 The copies of the new units of the channel `ν` are the `J + 1` units of the string. 

### `role`

 The table of the role `p` of move `x`: `ids e` are the units given at the slot `e`, `t` the number of units,
`o` the outcome. 

### `Plan`

 A plan: which units are given at every slot, and the number of units of every move (slots with fewer units are
filled with zeros), as functions of the numbers of units at the beginning and of the outcomes of the earlier moves. 

### `Plan.cons`

 the units given 

### `Plan.num`

 the number of units 

### `Plan.good`

 outcomes that are allowed 

### `seenAt`

 The units seen before move `x` (for `x = E`: in the end). 

### `used`

 The units given before move `x`. 

### `cur`

 The current units before move `x`. 

### `Poss`

 The outcome of the move `x` is possible: there is one index for every block. 

### `Ok`

 The rules that a plan obeys (`cap` bounds the numbers of units given in a move). 

### `ids`

 The units given at a slot, in the order of the enumeration of all units. 

### `roleAt`

 The table of the role `p` of move `x` in the play. 

### `partyTab`

 The table of party `a` after all moves, as a function of its copies of all units it has ever held. 

### `tabInit`

 The table of party `p` at the beginning, as a function of its copies `y` of units. 

### `tabFinal`

 The table of a party after all moves: base parties start with the table of their block or part of the input, extra
parties with 1. 

### `grpVal`

 The value of a group. 
