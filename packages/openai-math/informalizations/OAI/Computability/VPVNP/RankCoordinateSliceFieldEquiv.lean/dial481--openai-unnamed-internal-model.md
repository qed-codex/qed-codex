---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSliceFieldEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceFieldEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceFieldEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Identifying the native and advised index sets of the slice minors

The native rank code selects rows and columns after interpreting packed
scalars in the polynomial-basis extension. The query data selects them in
the advised field. The field isomorphism identifies both sets, including
the dense ordinal of the row replaced in the numerator.


### `interpretedMatrix`

 The encoded base matrix after interpreting each scalar in the polynomial extension field. 

### `interpretedMatrix_eq`

 Reading the physical scalar followed by its ring interpretation produces
the inverse image of the queried matrix entry in the advised field. 

### `nativeOrdinal`

 The next quotient coordinate's ordinal among all greedy basis rows, cast to the rank
computed over the extension field. 
