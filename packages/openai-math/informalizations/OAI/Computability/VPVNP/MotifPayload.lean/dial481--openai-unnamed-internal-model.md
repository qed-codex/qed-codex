---
{
  "module": "OAI/Computability/VPVNP/MotifPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Grouping repeated motif maps by the total edge payload

Theorem 6.1 uses one outer term for each total supply-width vector. The
wire on an edge contains a selector list and the concatenated fields for
the selected base maps. The coordinate arithmetic below is mixed-radix
binary concatenation in the order of the copies.


### `Word`

 A width-`b` wire coordinate, numbered by its binary word. 

### `unpackFields`

 Mixed-radix decomposition into the fields for consecutive copies. 

### `wireFields`

 The payload occupies the low bits, with the list of selectors above it. 

### `totalWidth`

 Each edge's accumulated payload width. 

### `EntryIndices`

 The complete list of table lookups for a single party. Each copy selects
one base map and supplies its output and input coordinates. 

### `payloadIndices`

 Split the payload only if its total width agrees on every supply edge. 

### `sequenceCode`

 Encode the selectors for all copies using the same fixed code table. 

### `tagIndices`

 Invalid tags reject the entry. Membership in the image can be checked
copy by copy against the fixed finite table. 

### `groupedIndices`

 The scalar-independent evaluator description at a party, including all
checks on the selector copies, their validity and the supplied widths. 

### `evalIndices`

 Evaluate a successful list of base entries multiplicatively. Failed checks
produce the zero scalar in any commutative semiring. 

### `groupedMap`

 The map in one term of the grouped motif identity. 

### `mem_sequenceCode_range`

 The common code-table membership test is equivalent to testing each
selector separately. Decoding requires no search over selector sequences. 
