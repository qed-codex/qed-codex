---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRingProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRingProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRingProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native arithmetic after immediate Boolean specialization

The existing finite sparse-product program is used with empty formal support.
Its keys still carry the ambient input coordinate type; this does not compress
the declared variables. There are at most `u * J` retained entries, including
zero cutoffs. Polynomial local time therefore bounds all its source prefixes,
including the table, inputs, output, normalization copies and arithmetic scratch.


### `constant_good`

 The native constant keeps its origin record exactly at positive cutoffs. 

### `jetProjection`

 The semantic projection for already-specialized correction variables. 

### `rawValue`

 Decode an actual finite native dictionary into the dense ring. 

### `rawValue_constant_one`

 An actual decoded unit represents the neutral factor, including zero cutoffs. 

### `readout_codes_dense`

 The existing native additive readout is exactly the dense marker sum. 

### `negation_dense`

 A physically represented negative unit supplies the finite-difference sign. 

### `empty_support_card_le`

 Empty formal support has at most one possible support, also when `J = 0`. 

### `product_input_bits_le`

 The concrete product input includes all three structure-constant indices,
the two coefficient arrays and the marker/Taylor controls. 

### `normalization_run_space`

 Specialization can create equal keys; normalization accepts those collisions.
The source bound counts every emitted record, before equal keys are merged. 

### `addition_run_space`

 Native addition normalizes one bounded array into another bounded array. 

### `scaling_run_space`

 Scalar multiplication also implements signs using the cached negative unit. 

### `productBudget`

 Polynomial in dimensions, coefficient width and ambient input length. 

### `product_run_space`

 Actual multiplication, its clean return, and every local source prefix.
The initial stack sum explicitly includes every persistent cache and both inputs. 

### `readout_run_space`

 The readout uses only `u * J` records and returns exactly `J` coefficient words. 

### `localBudget`

 A common explicit polynomial majorant for every local arithmetic service.
`N` counts unnormalized specialized records; it need not be at most `u * J`. 

### `localBudget_le`

 The degree and constant are fixed before every runtime dimension. 

### `readoutBudget_polynomial`

 Additive readout has a fixed degree-six bound. 
