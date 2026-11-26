---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decoding an arbitrary complete native hidden-field stream

The same field widths that the native loop reads determine a partition of
any sufficiently long bit list. This includes empty fields and preserves
the remaining bits for the next node operation.


### `decode`

 Replace each field's bits, retaining its ID and consuming its recorded width. 

### `decode_tail`

 The decoder drops exactly the total number of requested field bits. 

### `decode_valid`

 Sufficient input determines both the actual accepted prefix and its tail. 

### `native_decode`

 The actual native run from a raw stream writes the decoded fields and
passes the exact remaining suffix to its continuation. 
