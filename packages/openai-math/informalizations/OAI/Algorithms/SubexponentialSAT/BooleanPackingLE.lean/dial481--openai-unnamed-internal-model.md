---
{
  "module": "OAI/Algorithms/SubexponentialSAT/BooleanPackingLE.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BooleanPackingLE.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/BooleanPackingLE.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Little-endian Boolean chunks

The actual materializer writes the first label bit at the first variable
offset. This module supplies the matching numeric embedding, its inverse and
range, and the exact relation to the older most-significant-first encoding.
All reversals use the actual chunk size, including a shorter final chunk.


### `testBit_toNat`

 The indexed bit of an actual little-endian word is its numeric test bit. 

### `word_eq_of_length_value`

 Fixed-width little-endian words are determined by their numeric value.
Leading zeroes are allowed because the two widths agree. 

### `testBit_toNat_getD`

 Missing high bits have their usual value false. 

### `decodeChunk`

 A total low-bit decoder; validity is needed only to re-encode exactly. 

### `word_getElem_eq_decodeZMod`

 The materializer's actual word lookup equals the matching semantic
chunk decoder, for every available bit. No validity premise is hidden here. 

### `msb_value`

 The old recursive equivalence reads its first coordinate as the most
significant bit. This exact formula makes the convention difference explicit. 

### `chunkEmbedding_eq_msb_rev`

 Reversal is at the actual b-bit chunk, including a short final chunk. 
