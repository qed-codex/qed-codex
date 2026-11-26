---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Transform.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Transform.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Transform.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Budget for packing calls with a common table label 

### `cap`

 Allow one enable bit per call. The rest of the address can encode
the shared label and the dictionary's enable bit. 


# One dictionary for heterogeneous calls

A row contains one table label and several argument tuples for that
same table. Unused positions contribute the scalar one.


### `packed_calls`

 The arity bound for the output can be chosen independently of the
labels. It suffices to admit all required sorting tables. 

 # Reading labeled gates on a common tape 

### `tape`

 Replace just the labeled factors by one dictionary. 


# Applying small dictionaries with many output bits

Guess the output bits and check each complete answer with one scalar
dictionary call. The tape then has a unique extension, so the output
can feed a second weighted computation without a multiplicity factor.


### `bind`

 Existentially hide the unique output tape after weighting it. 


# Packet matching with two permitted long sorts

Compare the sorted list before and after reversing active directions.
No distinctness test is needed for the inactive records.


 # A packet plan may have repeated inactive headers 

### `matching`

 The long-sort test now checks exactly one equality of payloads per
active pair. Padded positions and inactive records require no pairing. 

 # Hardwired packet layouts for a partial batch 

### `packet_plan_with`

 The tensor is fixed before the headers are known. The semantic
description only requires well-formedness on inputs where it is used. 

 # Pairing and padding bit positions on a shared row tape 


# Naming whole rows by signed identifiers

Several pins can share one header. It suffices that equality of signed
identifiers coincide with equality of rows. Every live row then has a
unique opposite row, even if the unused headers are all identical.



# Routing arbitrarily wide records by short sorts

Repeat the same permutation test with successive slices of the payload.
Each test compares two sorted arrays of pairs. Source addresses are
constants, and all the tests share a single array of target addresses.

