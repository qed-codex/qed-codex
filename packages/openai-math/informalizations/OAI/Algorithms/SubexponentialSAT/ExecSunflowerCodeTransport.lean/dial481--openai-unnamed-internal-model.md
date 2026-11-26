---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecSunflowerCodeTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSunflowerCodeTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecSunflowerCodeTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering typed sunflower witnesses from encoded candidates

The executable search manipulates literal words. Selected clauses come from
the input list, and the accepted common core lies in each selected clause.
These facts suffice to recover typed lists for proof purposes. The executable
algorithm never needs a choice of a typed inverse.


### `lift_list`

 A selected list has an ordered preimage; multiplicities are retained. 

### `lift_sublist`

 The stronger sublist case also preserves the selected positions. 

### `sunflower_reflect`

 Injective encoding reflects the exact common-intersection condition. 

### `sunflower_image`

 Typed sunflower witnesses remain valid after the actual injective encoding. 

### `lift_candidate`

 No separate inverse-decoder hypothesis is required for an accepted core:
it is contained in a selected encoded clause. 

### `uniform_reflect`

 Width checks on encoded clause sets reflect to the typed selected family. 

### `typed_sunflower`

 An accepted encoded family yields the exact branching witness required by
the mathematical sparsifier, with the selected family inside the input. 

### `literalWord`

 The actual literal payload used by the encoded CNF programs. 

### `recovered_petals`

 Filtering the common core out of the selected clauses recovers the
actual petals, even when their list order is different from the old selector. 

### `nonemptyCoreSunflowerFree_reflect`

 Every typed nonempty-core sunflower would encode to a raw one. 

### `width_filter_image`

 Injective literal encoding preserves each exact-width family. 

### `minimumWidth_reflect`

 The raw exhaustive-search result supplies the precise charging invariant. 

### `typed_choice`

 The encoded search's local outputs produce exactly the certified choice
used by the existing path-charging and decomposition proofs. 
