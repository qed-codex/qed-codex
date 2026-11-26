---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortScheduleFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortScheduleFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortScheduleFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming the physical exchange blocks in stage order

Local strides leave the incident stream untouched. At every cross-site
stride its next two whole blocks are the outgoing and incoming fields for
that layer. Thus one forward pass over the stream implements the address
formula of Lemma 10.1 without storing a numerical global wire address.


### `exchangeNumber`

 Physical layer number, present only for cross-site comparisons. 

### `exchangeNumbers`

 Reading two consecutive blocks per cross stride visits physical layer
ordinals from zero up to the full incident width, in exactly that order. 

### `exchangeStream`

 Concatenating the blocks in execution order gives the same input stream
as iterating over their physical field indices. 

### `fieldPair`

 The two contiguous directions reserved for a physical layer ordinal. 

### `incident_stream`

 The tape bytes consumed by the successor pass and by the chronological
stage loop are exactly the supplied incident bit vector, including for
arbitrary malformed record encodings. 
