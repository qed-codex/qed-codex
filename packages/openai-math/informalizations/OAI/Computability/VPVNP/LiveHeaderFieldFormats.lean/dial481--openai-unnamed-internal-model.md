---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderFieldFormats.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldFormats.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldFormats.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decoding both incident fields from a completed live header

The incident cut index determines the evaluated layout, including the pair
layout at the midpoint on the input side of the first tail group. Each
interior padding condition refers to the same bits as the typed layout.


### `interval_endpoint`

 A missing endpoint has no field on either side, in every mode. 

### `interval_pair`

 The payload at a first-half cut uses the pair layout up to and including the midpoint. 

### `interval_tail`

 Every interior cut strictly after the midpoint uses the serialized configuration layout. 

### `validPadding_endpoint`

 At each missing endpoint the padding guard is vacuous. 

### `decodedPadding`

 Canonical trailing bits in the layout of one cut. Endpoint strings have no entries. 

### `validPadding_evaluated_iff`

 The two evaluated padding guards are exactly the typed trailing-bit tests
on the incoming and outgoing cut, including endpoint and midpoint cases. 

### `Image.copiedField`

 A complete image contains the occupied part of each of the six payload buffers. 

### `Image.unoccupied`

 An unoccupied word of a payload buffer retains its value at entry to the field suffix. 

### `Image.pair_exponents`

 The actual buffer at either pair-format cut represents its decoded exponent vector. 

### `Image.pair_exterior`

 The exterior scratch words contain the exact bits of the doubled primed cut. 

### `Image.tail_config`

 Each tail configuration word is the corresponding decoded configuration bit. 

### `Image.first_exponents`

 The missing incoming cut at the first group preserves the zero exponent vector
installed before the suffix. This also applies at any intermediate suffix cursor. 
