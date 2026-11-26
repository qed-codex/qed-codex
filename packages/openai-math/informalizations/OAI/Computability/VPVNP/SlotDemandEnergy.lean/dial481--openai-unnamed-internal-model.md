---
{
  "module": "OAI/Computability/VPVNP/SlotDemandEnergy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandEnergy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotDemandEnergy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Energy of the packed demand wires

The first inequality of §7.2 charges every actual wire exactly once. In a
thick–thick bundle the old payloads are concatenated and divided as evenly
as possible among its assigned motifs. Each remaining wire retains its old
width in the CD demand of its motif.


### `pieceCount`

 The number Q of pieces in each concatenated payload. 

### `BundleNumbering`

 Number the motifs assigned to each bundle in the common order used at A and B. 

### `ThickWire`

 The original wires concatenated at A and B. 

### `bundleNumbering`

 Lemma C.1 supplies an ordering with exactly Q pieces in each bundle. 

### `bundleWidth`

 Total number of bits in the concatenation, before rounding. 

### `abWidth`

 Width of the AB wire paired with the unchanged CD wire of a motif. 

### `card_thick_fiber`

 Number of thick–thick wires over each original bundle. 

### `bundleWidth_le`

 Concatenation uses at most the number of bundled wires times the maximum old width. 

### `abWidth_le`

 The individual AB pieces are no wider than the largest old wire. 

### `sum_abWidth`

 Concatenation followed by the Q-way division preserves the payload width. 

### `bundle_energy_le`

 The bundle's perfect fractional division inherits the total old mass.
Integral division incurs at most Q/(4(p/3)) additional energy. 

### `demand_energy_le`

 Total demand energy at the actual masses p/3 and p, before any supply
substitution. The last term is the per-bundle integral rounding cost. 
