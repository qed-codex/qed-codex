---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native reads of the distributed live header

One processor location stores its four local header bits in the low end of
one external word. A microcall addresses a single site, extracts a statically
chosen field, and stores one bit in a separate scratch array. The cursor and
the array base are words, independently of the distributed index length.


### `fetch`

 A slot extractor. Register 0 holds the site address. Register 1 receives
the bit word. The scratch registers are 2 and 3. 

### `copyCell`

 Copy one field of the processor at `state - pub 0` to the same offset in
the scratch array beginning at `pub 1`, and advance the persistent cursor.
This is a constant instruction list at every input length. 

### `copyCell_trace`

 The exact interpreter trace of a copy call, on arbitrary external memory. 

### `copyCell_native`

 A correctly packed header is copied to the unpacked destination array as a
single bit. The native program takes two probes and returns the next cursor. 
