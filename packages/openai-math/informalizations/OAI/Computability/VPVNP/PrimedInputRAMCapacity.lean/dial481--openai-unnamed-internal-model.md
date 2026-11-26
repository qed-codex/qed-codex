---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMCapacity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMCapacity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMCapacity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Allocating the pair counter's headers and two rectangles

The bit-valued index, advice and cut arrays and the nominated histogram
occupy a polynomial number of header addresses independent of `B`. Choosing
`B` last puts all these addresses below the actual virtual site count `R′`.
The two rectangles then start at `R′` and their addresses fit the paper's
prescribed word width.


### `rectangleAddressSpace`

 Both row-major rectangles fit above the full virtual header interval. 

### `headerCapacity`

 A fixed degree bound for the header data is absorbed by the choice of
address multiplier `B`; the same capacity covers the middle cut. 

### `eventually_layout`

 The literal prefix and the paper's processor parameters give an actual
two-pass layout, including the room for every histogram header and exactly
the virtual site's header interval as the scratch base. 

### `eventually_pairedLayouts`

 The choice of `B` and the threshold length work simultaneously for
every primed pair, including the endpoint pairs whose exterior cuts are
empty. The cut capacity uses the paper's `n^a * n^d₂` upper bound. 

### `initialMemory_headerMemory`

 The header provider agrees with the zero-elsewhere initial memory of
Lemma 10.1 when all nominated histogram words fit in the header interval. 
