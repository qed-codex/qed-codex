---
{
  "module": "OAI/Computability/VPVNP/SlotDemandLocal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandLocal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandLocal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the four demand words locally

The bit slices of an AB demand can contain pieces from several old wires.
Every outgoing old factor in those pieces lands at the single packed A site,
and every incoming factor lands at B. The unsplit CD words are read at the
new site of their respective old endpoint. This supplies the demand arguments
of the local map rows in equation (7.1).


### `place_thick_source`

 All thick source positions of a bundle are packed together at A. 

### `place_thick_target`

 All thick destination positions of the same bundle are packed at B. 

### `PlacedHalf`

 Half-wire fields of all whole old vertices placed at a single new site. 

### `localAWord`

 Extract the source half of the AB slice from the local inputs at A. 

### `localBWord`

 Extract the destination half of the same slice from the inputs at B. 

### `localCWord`

 Extract the CD half-wire at C, whichever original slot supplied it. 

### `localDWord`

 Read the opposite CD half-wire at D's new position. 
