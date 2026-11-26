---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpBlockPacking.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBlockPacking.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpBlockPacking.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full-block packing with a variable loss parameter

This is the arithmetic and finite packing step of Section 3.4 of the
multi-color manuscript. The variance and type-label assignment are inputs;
the blocks, coverage, and dimension consequences are proved here.


### `threshold`

 The exact ceiling threshold in equation (3.10). 

### `threshold_le_iff`

 The ceiling in the manuscript is precisely the division-free threshold. 

### `scaled_deviation_bound`

 The total squared-deviation estimate controls an individual scaled deviation. 

### `count_lower_of_square_bound`

 A scaled lower bound avoids all divisibility and floor issues. 

### `exists_completeBlocks_of_count_lower`

 Taking the minimum actual fiber count incurs no additional rounding loss. 

### `exists_completeBlocks_of_deviation_bound`

 The full parameterized packing implication in equation (3.10). 

### `exists_completeBlocks_of_ceiling_threshold`

 The same theorem using the manuscript's ceiling threshold literally. 

### `packed_card_le`

 Packed coordinates occupy at most the entire coordinate set. 

### `card_packedSupportFinset`

 The support in the packed copies has exactly one copy per block. 

### `packed_support_card_upper`

 Equally sized color sides remain no larger than a `1/r` fraction of the input. 

### `leftovers_le`

 At most an `ε` fraction of coordinates is left outside the complete blocks. 

### `packed_color_lower`

 Multiplying the loss in local dimension by the loss in block coverage. 

### `sum_color_lower`

 Adding all color lower bounds cancels the number of colors. 

### `finrank_le_card_support`

 A subspace whose vectors vanish outside a finite coordinate set has at
most as many dimensions as that set has coordinates. 

### `packed_finrank_lower`

 Equation (3.11), with denominators cleared, for the actual packed subspace. 

### `packed_finrank_upper`

 The upper dimension bound follows from the local bound and injective packing. 

### `packed_finrank_upper_of_support`

 Derive the upper dimension bound directly from support containment and
the size of a local color side, without assuming the dimension bound. 

### `packed_finrank_upper_fraction`

 The displayed individual bound `d_g <= D/r`. 

### `packed_finrank_lower_fraction`

 The displayed individual lower bound `(1-ε)^2 D/r <= d_g`. 

### `sum_packed_finrank_lower`

 The total dimension bound used in the separated enumeration exponent. 
