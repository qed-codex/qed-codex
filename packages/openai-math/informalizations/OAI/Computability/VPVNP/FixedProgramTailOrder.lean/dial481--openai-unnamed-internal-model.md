---
{
  "module": "OAI/Computability/VPVNP/FixedProgramTailOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedProgramTailOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The model's label order on the native evaluator input

The first half stores productions first and motif variables second. The model's
advice specifies their positions in the joint label order. The native ordinal
words and the reindexed runtime exponent field are exactly the words of the
fixed diagonal program, including the length-dependent width of each counter.


### `physicalLabelCount`

 Number of dense exponent coordinates in the physical group at this input length. 

### `physicalCounterWidth`

 Number of bits allocated to each exponent counter in the physical group. 

### `nativeLabelOrder`

 The native scatter has a single index type, whereas the model names
both the dense and the formal label count. Their equality transports only
the bounds of the indices. The permutation itself is the model's one. 

### `nativeOrdinalWords`

 Encode the evaluator ordinal of each physical label as a binary word in the advice
permutation. 

### `nativeAdvice_eq`

 The literal native advice tape is the diagonal program's distributed advice. 

### `nativeRuntime_eq`

 Reading the reindexed exponent field produces the same complete binary
input as `Program.initial` on the model's dense counter values. 

### `nativeInitialCode_eq`

 Exact initial state used by the contraction after the middle exponent cut. 

### `inputLength_of_fits`

 A nonempty evaluator has a nonblank tape cell for each input bit. Its
bounded initial configuration therefore fits the whole input in the right
half of the physical window. 

### `ScalarData.initialRoom`

 Derive midpoint input space from the verified physical evaluator histories. 
