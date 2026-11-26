---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSelect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Computing greedy row and column indices from a streamed matrix

At each prefix the five-word controller starts the complete physical rank
scan in private workspace. All matrix-entry requests address the original
matrix. For a column query the two address ports of its reader are
interchanged. Both routines return the original selected index.


### `local instance : DecidableEq (PrefixPort K)`

 Compare prefix-rank stack addresses using the port labels of the Gram scan. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decide equality of addresses in the template, working copy, and scratch stack of a
prefix-rank call. 

### `rankResult`

 Cursor argument register containing the rank returned by the Gram scan. 

### `prefixRank`

 Compute the rank of the current row prefix by passing its length to the Gram routine and
reading its result register. 

### `rows`

 Scan row prefixes for the rank increase that identifies the requested greedy basis row. 

### `columns`

 Apply the greedy row scan to the transpose reader to find the requested original column
index. 

### `workCap`

 Maximum stack length needed for either the initial prefix template or the running Gram
scan. 

### `timePerRank`

 Step bound for copying the prefix template, computing one rank, and returning the result. 

### `scanTime`

 Step bound for testing up to `n` prefixes, including rank calls and updates to the
controller words. 

### `scanSpace`

 Maximum stack length over the prefix controller's arithmetic and its private rank calls. 

### `side`

 Initialize the reusable rank template with zero rows and `m` columns, leaving the working
copy and scratch stack empty. 

### `prefixRank_runs`

 The rank subroutine called by the greedy controller. The incoming
prefix register determines every dynamic dimension in the two nested scans. 

### `row_runs`

 Complete physical row selection, including all prefix rank and scalar
entry requests, with a reusable private workspace. 

### `column_runs`

 The transpose scan returns the columns chosen for the square Cramer
minor of the original matrix. 

### `row_correctSpace`

 Native ordinal reader for greedy rows of the streamed matrix. Its
private work template is restored on every return. 

### `column_correctSpace`

 Native ordinal reader for the selected columns of the square Cramer minor. 
