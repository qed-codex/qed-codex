---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkMotifAbsolute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkMotifAbsolute.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkMotifAbsolute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Absolute role-table identifiers in dense CD piece order

A source port gives its residual lane by division by the old degree and
reduction modulo the lane radix. Append this lane to its normalized CD key
and scatter the resulting word by classified owner and sorted rank. The
preceding rectangle receives the thick wires' auxiliary words. The CD
rectangle has one entry for every motif and no holes.


### `columns`

 The first five parameters use the shared scatter layout. The last two
are the old degree and the residual-lane radix. 

### `payload`

 Encode an old port's absolute identifier by appending its residual-lane digit to the
normalized key, using the old degree and lane radix. 

### `visit`

 Native scatter visit that reads an old port's owner, sorted rank and key, writes its
lane-extended key at the owner and rank, and advances the cursor. 

### `events`

 Chronological trace for one absolute-identifier scatter, with the three observed source
words, the write to the classified row, and the intervening ticks. 

### `denseIndex`

 All dense addresses are used once. Recovering a motif from a dense index
recovers both its absolute bundle and its sorted piece number. 

### `absoluteIndex`

 The compact role-table identifier in the exact order of the slot compiler. 

### `Inputs`

 Read all three columns at the physical port. The normalized key is needed
only on a CD port. Thick scratch words may have arbitrary values. 

### `Inputs.of_ranked`

 The owner and rank cells coincide with the previously constructed width
scatter inputs. Only the third column is changed to the classifier's key. 

### `Directory`

 Contents of every dense cell, including the complete inverse enumeration. 

### `graph_run`

 A single physical scan emits every requested absolute motif identifier
into its dense rank cell. Its frame preserves every address outside occupied
CD and thick scratch cells. 
