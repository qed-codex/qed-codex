---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshArgumentSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshArgumentSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshArgumentSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word coordinates of a refresh argument site

The promoted site has coordinates `(base, port, residual lane)`. The old lane stores the
same port as its high field, so promotion preserves the numerical site ordinal. The old
and new first slots multiply that ordinal by their respective degrees. The external
segment directory instead uses the old port as the segment index within the bundle.


### `portIndex`

 The port of a promoted site, above the residual-lane field. 

### `blockIndex`

 Block ordinal for the term table. Consecutive divisions recover the base vertex. 

### `oldFirst`

 Compute the first old slot of the site by multiplying its ordinal by the old degree. 

### `newFirst`

 Compute the first refreshed slot of the same physical site using the restored degree. 

### `segment`

 External segment in the current bundle's source-port order. 

### `diagonal`

 Address the diagonal segment by using the site's own promoted port as the segment number. 

### `oldSite_number`

 Splitting the old binary word preserves the ordinal of the promoted physical site. 

### `oldFirst_eval`

 The old outgoing or incoming field list starts at the first slot of the old site. 

### `newFirst_eval`

 The new field list starts at the first slot of the promoted site in the selected state. 
