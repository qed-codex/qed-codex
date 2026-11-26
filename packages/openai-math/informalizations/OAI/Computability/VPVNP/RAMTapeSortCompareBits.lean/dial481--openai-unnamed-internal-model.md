---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortCompareBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortCompareBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortCompareBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite bit summaries for physical record comparison

The sorter scans each five-word record from its tag through its probe
ordinal. Within a word, the most recent unequal pair of bits decides the
unsigned order. Only the low two bits and the presence of a higher set bit
matter for tag validation. The summaries therefore use a fixed finite state
space independent of the word width.


### `orderStep`

 A low-order result is retained only while all remaining high bits agree. 

### `WordState`

 Finite state of one word scan. The bounded tag observations also detect
an all-zero payload word without storing its numerical value. 

### `WordState.lhs`

 Finite tag-decoder state summarizing the bits scanned so far in the left word. 

### `WordState.rhs`

 Finite tag-decoder state summarizing the bits scanned so far in the right word. 

### `WordState.ord`

 Unsigned order of the two little-endian prefixes. A later unequal pair of bits supersedes
  the earlier order. 

### `WordState.start`

 Start a field comparison with both tag decoders empty and the operand words provisionally
equal. 

### `WordState.step`

 Feed one bit from each operand to its tag decoder and update the unsigned order at this bit
position. 
