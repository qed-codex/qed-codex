---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateTargetRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateTargetRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateTargetRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical scalar reader for the powered target row

The monomial pair scan compares the requested original column with the
powered target exponent. The returned bit selects a canonical field zero
or one. Both the exponent scan and the scalar copy restore the prepared
target parameters, so subsequent column queries use the same advice.


### `reader`

 The equality word has numeric value zero or one. The tag scan reads its
low bit before the whole word is reclaimed. 

### `live`

 Inputs for a query of one target-row entry. The source ordinal is fixed and the column
ordinal is set to the requested column. 

### `ordinals`

 The two bounded monomial indices used by a target query, with the source at false and the
column at true. 

### `entryFlag`

 Whether the enumerated column monomial equals the source monomial after applying the
specified power and coordinate shift. 

### `clock`

 Step bound for scanning both monomial indices, testing the powered exponents, copying the
selected field literal, and clearing the flag. 

### `space`

 Stack-height bound for the target-row reader, including the powered-monomial scan and the
copy of an `e`-limb scalar with `v` bits per limb. 

### `literal`

 The packed field element returned for a Boolean entry flag, encoding one on a monomial
match and zero otherwise. 

### `Ready`

 The target reader’s work stacks contain the prepared monomial parameters and the two packed
field literals for this extension. 

### `ready_bound`

 Bound on each auxiliary stack before and after a target query. 

### `correctSpace`

 The actual finite routine reads the target independently of the dense
row and uses the original column index as its second monomial address. 

### `map_match`

 The native equality flag reads exactly the field-valued powered target
of a Frobenius or label operation. 
