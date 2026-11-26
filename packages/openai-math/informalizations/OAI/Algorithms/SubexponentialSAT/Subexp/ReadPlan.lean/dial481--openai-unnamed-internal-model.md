---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ReadPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ReadPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ReadPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit local read plans

Read plans are lists of numeric positions in the explicit seed array. The
machine-facing data are fixed-width one-hot word records and unary indices.
Gathering them in head/slot order reproduces the actual type encoding.


### `encodeWord`

 Position first, then color: each letter is a one-hot r-bit record. 

### `encodeType_eq_words`

 Concatenating encoded head and slot words is the existing type encoding. 

### `vertexPlan`

 Seed-array positions, with the head first and the slots in numeric order. 

### `remainingPlan`

 Test only numeric membership in the two explicit vertex plans. 

### `selectPosition`

 A free seed reads its candidate-tuple position after the current array;
every other seed keeps its original current-array position. 

### `selectionTable`

 First-match lookup table for the selector, built by one finite recursion. 

### `applyChoices`

 The optional-coordinate update semantics used by the padded leaf tree,
driven by one explicit list of candidate words. 

### `leaves_eq_tuples`

 Each actual leaf is obtained by one explicit tuple in the same recursive
order as the padded completion tree. 

### `partialEncoding`

 Bit records for the current words followed by the candidate tuple. 

### `currentArray`

 A finite, explicit current array from the search's reverse fixed list. 

### `completedAssignment_eq_leaf`

 The preparation uses the actual search state and tuple, and reconstructs
the actual optional-update leaf assignment at every seed coordinate. 

### `plannedCollision`

 This local test compares two explicit bit lists. 

### `plannedPairLeaves`

 A concrete pair leaf stream, generated from tuple words and list reads. 

### `plannedNumeratorLeaves`

 Assemble all ordered-pair streams using the same explicit vertex list. 
