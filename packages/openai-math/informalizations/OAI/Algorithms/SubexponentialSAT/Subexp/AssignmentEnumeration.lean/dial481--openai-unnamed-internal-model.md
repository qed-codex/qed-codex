---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit enumerations for the conditional-expectation assignment

Words are enumerated by a finite recursion over the alphabet `List.finRange r`.
Seed indices are enumerated from supplied factor and vertex lists. Numeric
codes use `idxOf`, and inverse lookups use the same lists. No arbitrary finite
equivalence or choice operator occurs in these executable definitions.


### `tuples_nodup`

 Distinct alphabet entries and distinct tails give distinct tuples. 

### `wordAlphabet`

 The complete word alphabet, in the recursion's explicit lexicographic order. 

### `zeroWord`

 Explicit default for a nonempty color alphabet. 

### `firstWord`

 Head and tail supplied to the existing sequential choice procedure. 

### `wordCode`

 Numeric word codes are exactly the positions used by `indexCode`. 

### `wordAt`

 Bounded word lookup in the actual enumeration. 

### `wordAt`

 Partial lookup is available when a caller holds only a natural number. 

### `wordIndexEquiv`

 An explicit index equivalence whose two functions are lookup and `idxOf`. 

### `universalAlphabet`

 Explicitly enumerate a head word and all slot words. 

### `sumList`

 List the left summand followed by the right summand. 

### `seedIndices`

 Factors, vertex heads, then all vertex/slot padding words. 

### `seedIndexEquiv`

 Both directions execute the supplied-list lookup and position search. 

### `decode_eq_reverse_getD`

 The search stores chosen values newest first; numerical coordinates use
the reverse list, so coordinate zero is the first choice. 

### `encodeChoices`

 Serialize a total assignment in exactly the search's reversed-list format. 

### `enumeratedAssignment`

 The existing assignment algorithm with its word and seed enumerations
constructed explicitly from the input vertex and factor lists. 

### `assignmentValues`

 The actual reverse-chronological choices made by that algorithm. 

### `assignmentValues_lookup`

 The assigned word is found at precisely its seed code in the chronological
choice list. Every seed lookup is in range. 

### `enumeratedAssignment_deviation_le`

 The deviation theorem now requires only the actual input lists; alphabet
and seed completeness are discharged by the explicit constructions above. 
