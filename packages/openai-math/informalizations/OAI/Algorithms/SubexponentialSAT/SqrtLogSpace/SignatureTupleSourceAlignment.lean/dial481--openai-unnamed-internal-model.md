---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleSourceAlignment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleSourceAlignment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleSourceAlignment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The frontend's actual mask, the produced head rows and the authentic
source factory use the same ambient variables and the same full integer keys.
No selected-coordinate or factory-alignment witness is supplied by the caller. 

### `forward_bits`

 Reversing the physical descending mask gives the forward ambient mask. 

### `low_bits`

 Every ambient coordinate is retained, including variables with no source
occurrence. The low mask is the actual complement of the produced high set. 

### `row_cast_eq_iff`

 Equality of all raw rows is unchanged by the actual length cast. 

### `factor_row`

 Factor rows follow all ambient head rows in the actual produced table. 

### `factor_ids`

 The physical factor stream is the complete increasing filter by its
produced color, including every neutral factor for an unused low variable. 

### `factor_partition`

 Every produced factor occurs in exactly one group. This quantifies over
all factor IDs, so a neutral factor cannot be omitted by head incidence tests. 

### `selected_mem`

 The actual row lookup selects exactly the free coordinates of the
produced head, without a packing-coverage or occurrence premise. 

### `free_head_card`

 The semantic free-head width is exactly the emitted cursor width. 

### `selected_length_le_max`

 The runtime exponent uses the original actual maximum over selected
node/head widths. Ambient n bounds retained storage separately. 

### `maximum_width_budget`

 The same actual maximum has the original balanced packing bound. The
alphabet premises are discharged by the physical complete-alphabet producer. 

### `owner_head`

 The owner and head are read from the original produced packing. 

### `owner_low`

 Every actual incidence owner is low; unused low coordinates still
participate in selected_mem independently of whether they own an incidence. 

### `plans_owner`

 Changing factor IDs to physical ambient-offset addresses preserves the
owner in each actual saved plan position. 

### `produced_literal`

 The source factory uses the same original integer matrix; only the
proof-level row index is transported to the actual saved plan-list length. 

### `produced_shifted_typed`

 The actual loader's signed matrix and shift relation give the exact
source-factory coefficient words. The plan-owner alignment is proved from the
addressed constructor, including all raw rows and the actual column order. 

### `ordered_source_key`

 Every source row of the exact head label equals the raw integer key of
its actual cursor assignment. No row basis or coordinate tuple is substituted. 

### `source_key_eq_iff`

 The canonical cursor and authentic source label have exactly the same
equality classes after every source row is retained. 

### `card_representatives_eq_labels`

 Canonical cursor representatives count precisely the attained full
source labels on this selected free head. No arbitrary row-coordinate grid
is introduced, and the assignment width remains the physical selected size. 

### `shifted_key_eq_iff`

 Equality of the actual emitted shifted keys is exactly equality of
complete source labels. The physical matrix witnesses come from the paid
loader; no separately supplied successful coefficient layout is needed. 
