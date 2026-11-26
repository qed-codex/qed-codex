---
{
  "module": "OAI/Computability/VPVNP/CursorNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local vertex factors of the cursor network

Section 12 gives each mask system a field on each of the two outgoing arcs.
At a nonzero cursor its local factor tests the routing equalities. At cursor
zero it also evaluates the site's validator on the selected outgoing and
returning fields. These factors accept arbitrary independent half-wire
indices, as required by the substitutions in (12.2).


### `Position`

 A cursor position, consisting of the current mask-bit index and the site occupied at that
index. 

### `Arc`

 A directed cursor arc indexed by the current bit position, sending site, and decision to
flip that bit. 

### `Payload`

 One Boolean word of the prescribed width for each system sharing a cursor arc. 

### `head`

 The head of an arc after advancing the cursor and applying its bit choice. 

### `network`

 The two arcs at a position are indexed by their sender and choice. 

### `incomingArc`

 Source of the unique incoming arc with the prescribed choice. 

### `out`

 A site's half-wire arguments can be read using local outgoing and incoming
slot numbers, without consulting any other site's arguments. 

### `inc`

 Incoming payload at a cursor position from the arc with the specified flip decision. 

### `sent`

 Assemble each system's sent payload from the outgoing arc selected by its current mask bit. 

### `received`

 Assemble each system's received payload from the incoming arc selected by its mask bit at
the preceding cursor position. 

### `Checks`

 Clamp every unused outgoing field, and at each nonzero cursor tie the
selected incoming and outgoing fields bitwise. 

### `factors`

 The uncompressed tensor factors, one per position. The validator takes
the selected send vector followed by the selected receive vector. 

### `rotate_of_step`

 The last cursor is the incoming cursor of every site validator. 

### `returned`

 Returns at cursor zero pull the corresponding send back through the full
xor permutation for each individual mask. 

### `contract_eq`

 Contracting the actual two-arc graph gives one term per source setting.
All intermediate equalities and clamps are evaluated on their own half-wires. 
