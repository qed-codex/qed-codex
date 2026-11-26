---
{
  "module": "OAI/Computability/VPVNP/LiveProgramLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public geometry and disjoint working regions of the live program

The group header occupies addresses below `2^d`. The external tag, the
header parser's own workspace and the remaining arrays start above it. The
shadow of the auxiliary RAM has room for every virtual site. Unused shadow
addresses have zero default and need no initialization.


### `Constants`

 Fixed choices for a circuit exponent and a fixed expander and evaluator. 

### `Constants.circuitExponent`

 Circuit-size exponent used in the grammar state bound `n^(circuitExponent + 5)`. 

### `Constants.chainPower`

 Exponent giving the height parameter of the paired chain as a power of the input length. 

### `Constants.advicePower`

 Exponent giving the capacity of the live header’s advice field as a power of the input
  length. 

### `Constants.deltaPower`

 Exponent giving the cut-width parameter of the live header as a power of the input
  length. 

### `Constants.radiusPower`

 Exponent giving the radius of the bounded tape windows in an evaluator configuration. 

### `Constants.prefixPower`

 Exponent reserving space for the packed literal prefix in the live memory layout. 

### `Constants.motifLabels`

 Number of motif labels appended to the grammar production labels. 

### `states`

 Public expression for the number of grammar states at length n, namely n raised to the
circuit exponent plus five. 

### `grammarLabels`

 Number of terminal and ordered binary production labels. Terminals contribute two per
position and state, and each degree split contributes one per ordered triple of states. 

### `labels`

 Total number of counters for grammar productions and motif labels together. 

### `height`

 Public chain height `n^chainPower`, one more than the header’s chain parameter h. 

### `Z`

 Number of exponent bits per label, twice the public chain height. 

### `radius`

 Radius of each evaluator tape window at the current input length. 

### `configWords`

 Words per evaluator configuration, comprising one state word and two tape windows of twice
the radius plus one cell each. 

### `prefixCapacity`

 Reserved capacity for storing the program prefix at the current input length. 

### `lengths`

 Header parameters for chain height minus one, cut width, advice capacity, total exponent
bits, and the two-tape configuration’s bit length. 

### `grammarLabels_eq`

 Concrete triangular production index used in the auxiliary preorder parser. 

### `stageTag`

 Address of the external dispatch tag, immediately above the range of the d-bit site
addresses. 

### `header`

 Start of the live header parser’s workspace, one word after the stage tag. 

### `descriptor`

 Start of the auxiliary descriptor table at the end of the live header workspace. 

### `counter`

 Start of the label-counter array after the seven three-word auxiliary descriptors. 

### `oldState`

 Start of the saved evaluator configuration immediately after the label counters. 

### `newState`

 Start of the next evaluator configuration after the saved configuration’s word array. 

### `transitionScratch`

 Start of temporary storage for evaluator transitions after both configuration arrays. 

### `adviceFrames`

 Start of the advice frames after the five transition scratch words. 

### `packedPrefix`

 Start of the packed literal-prefix area after the twenty-four advice-frame words. 

### `orderMap`

 Reserve the full prefix capacity in addresses. Packing uses at most one
word per bit, including when the active prefix is shorter than its capacity. 

### `shadow`

 Start of the virtual RAM shadow after the order map, which reserves one entry per label. 

### `virtualBucketBits`

 Virtual bucket exponent obtained by rounding the ceiling binary logarithm of n up to the
next multiple of four and dividing by four. 

### `virtualSiteBits`

 Virtual site address width obtained by subtracting the virtual bucket exponent from the
ceiling binary logarithm of the total virtual capacity. 

### `pairWorkspace`

 Start of the pair table’s workspace after reserving one shadow word per virtual site. 
