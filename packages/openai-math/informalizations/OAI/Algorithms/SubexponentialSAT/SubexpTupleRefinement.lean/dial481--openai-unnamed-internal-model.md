---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTupleRefinement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTupleRefinement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTupleRefinement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Representation and coverage of the fixed tuple program

The tuple program reverses its record order at each Cartesian expansion.
These theorems retain that actual order and show that it is a permutation of
the explicit coefficient-vector enumeration. Fixed-width injective encodings
then give uniqueness, not just coverage.


### `powerRows_perm`

 All record reversals affect order only; every prefix/suffix combination
is generated with its correct multiplicity. 

### `powerRows_encoded_perm`

 The actual fixed-control tuple program enumerates precisely the encoded
vectors for any fixed-width code, in its own explicit order. 

### `encodeTuple_mem_powerRows`

 Every requested tuple is visited when the scalar alphabet is complete. 

### `encodePair_mem_powerRows`

 One tuple loop at depth d+e covers all concatenated coefficient pairs. 

### `generated_unique_pair`

 Each generated word has a unique pair of prefixes of the requested
coefficient lengths, including zero-length parts. 
