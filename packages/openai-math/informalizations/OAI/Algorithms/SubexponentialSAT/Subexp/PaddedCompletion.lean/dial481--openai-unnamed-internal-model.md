---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PaddedCompletion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PaddedCompletion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PaddedCompletion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit padded completion leaves

Every optional coordinate branches over the entire word alphabet. A real
coordinate updates the assignment; a dummy coordinate ignores the word.
Padding therefore implements the common-denominator multiplicity by actual
finite leaves rather than a multiplication of the resulting score.


### `boolValue`

 The natural value of a successful or unsuccessful collision test. 

### `successful`

 A unary score is the list of successful Boolean leaves. 

### `assignOptional`

 Real coordinates update the assignment; dummy coordinates consume a
choice without changing it. 

### `leaves`

 Actual finite generation of collision Booleans, including every dummy
choice. No arithmetic scaling is used by this executable definition. 

### `paddedIndices`

 Append enough ignored coordinates to reach the common support bound. 

### `trueCount_dummy`

 Dummy coordinates repeat each terminal Boolean once for every tuple of
dummy word choices. 

### `trueCount_some_append_dummy`

 Padding is precisely the common-denominator factor in the natural
completion count. This equality holds even before imposing the size bound. 

### `numeratorLeaves`

 Concatenate all padded local completion trees. This is a single finite
Boolean input whose successful leaves encode the common numerator. 

### `numeratorLeaves_trueCount`

 The successful-leaf count is exactly the existing natural common
numerator, for arbitrary bounded zero/one local terms. 

### `numeratorLeaves_length`

 Every term contributes exactly q^S leaves once its free support is
bounded by S. 

### `pairLeaves`

 The concrete concatenated collision leaves for all ordered vertex pairs. 

### `pairLeaves_length_eq_block`

 The actual leaf list has exactly D²N² entries for a complete word
alphabet, not just an abstract numerical upper bound. 
