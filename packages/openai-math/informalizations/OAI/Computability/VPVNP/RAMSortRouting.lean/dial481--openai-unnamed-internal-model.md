---
{
  "module": "OAI/Computability/VPVNP/RAMSortRouting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortRouting.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortRouting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing comparator layers between sites

In Lemma 10.1 of *VP and VNP differ over every field*, every site holds a block of
`2^h = 4H` consecutive positions. A comparator at stride `2^j` pairs positions whose
indices differ in bit `j`. When `j < h` this changes only the offset inside the block.
Otherwise every record in the block goes to the same other site with its offset preserved.


### `partner`

 The comparator partner of an array index in a layer with stride `2^j`. 

### `partner_lt`

 A comparator partner is a valid position in the same power-of-two array. 

### `partner_local`

 The low bit belongs to the offset, so every comparator is internal to its site. 

### `partner_cross`

 A high bit changes the site and leaves every within-site offset unchanged. 

### `partner_lo`

 The partner of a lower-half index lies at the same offset in the upper half. 

### `partner_hi`

 The reverse comparison sends the upper-half index back to its lower-half mate. 

### `crossStrides`

 Stride exponents in phase `a` are `a-1, …, 0`. The ones requiring a whole-block
exchange are exactly those at least `h`. 

### `total_crossStrides`

 Summing over the phases of a `2^(h+d)` array gives the factor in equation (10.1).
Phase zero is included in the index set and has no comparator layers. 
