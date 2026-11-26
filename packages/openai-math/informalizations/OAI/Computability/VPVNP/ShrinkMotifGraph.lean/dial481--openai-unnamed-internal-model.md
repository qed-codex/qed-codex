---
{
  "module": "OAI/Computability/VPVNP/ShrinkMotifGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkMotifGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkMotifGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The six-party motif for the shrinking step

The parties are A, B, C, D, M, N in that order. Each supply edge carries
a layout bit recording the layout in which it survives, and a type from
zero to three. These are the same labels as in `SurvivingSlots`.


### `demandSource`

 The two demands in the order AB, CD. 

### `demandTarget`

 Target party of each demand edge, B for the AB demand and D for the CD demand. 

### `supplySource`

 The source party for each of BC, BN, CN, DM and AC, AM, CM, DN. 

### `supplyTarget`

 The target party in the same two supply groups. 

### `supply`

 Connected supply graph with one incident edge at every party for reading selectors. 

### `demandMass`

 Relative masses of AB and CD. 

### `relativeMass`

 Relative masses in each group of Lemma 6.2. 

### `supplyMass`

 Relative supply-edge mass indexed by edge type, using the same four masses in each layout. 
