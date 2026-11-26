---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic dispatch for each position in the pair counter

The two passes of Section 11 enumerate the rectangular input positions in
row-major order. Division and remainder identify the group, site, and tape
offset. Comparisons with the public field boundaries decide whether the bit
is literal, comes from a header word, or must be read at a designated
scratch address. The same computation marks the first-pass branch sites.


### `RawCopy`

 Raw addresses precede conversion to the bounded address word. 

### `rectangleAddress`

 The group, site and tape bit designate a row-major scratch word. 

### `dispatchHeader`

 Decide which of the header and path bits to fetch. The middle cut
always resides in the outgoing cut slot of group zero. 

### `dispatchPort`

 Resolve the transcript part of the row. No parsing is applied to
the data at the designated location. 

### `dispatchRow`

 Dispatch within one row. The prefix is a private public-data array, and
the field lengths and widths are public registers. Charges cover boundary
arithmetic, comparisons, branching, and the calculation of the result. 

### `dispatch`

 Scalar program, with group, site and within-row bit extracted from the
enumeration counter. The four quotient/remainder operations and the shift
constructing `2^r` cost five word steps. 

### `prefixAt`

 The prefix table is indexed in private storage and padded by zero. 

### `dispatch_fetch_lt`

 Every header or scratch address returned by the natural-number
calculation fits the physical address word before the conversion. 

### `compileCopy`

 Convert the arithmetic result into the actual source instruction of a
bounded-word burst RAM. At every valid position the fetch address fits. 

### `dispatch`

 Both instructions needed by the two loops at this flattened position. 

### `dispatch_eq`

 The scalar dispatcher recovers both the second-pass copy source and
the first-pass owner decision at every position. 
