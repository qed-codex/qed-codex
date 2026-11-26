---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPackingParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPackingParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPackingParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computable packing parameters for the subexponential argument

All schedules are total functions of the input size. The main construction is
used only on `GoodInput`; smaller inputs are handled by exhaustive search.
The logarithms are computed by natural-number binary logarithms, with exact
dyadic characterizations recording their rounding behavior.


### `s`

 The integer part of the iterated binary logarithm on the intended domain. 

### `u`

 The slowly growing number of bits per field coordinate. 

### `D`

 Number of actual Boolean chunks, with the ceiling computed in integers. 

### `r`

 Number of interpolation colors. 

### `GoodInput`

 Domain on which the growing-parameter branch is used. 

### `chunkSize`

 Sizes of the actual chunks for this input-dependent schedule. 

### `primeTest`

 Executable primality test; its range of candidate inputs is bounded below. 

### `primeScan`

 Scan exactly the integers strictly between `2^u` and `2^(u+1)`.
The second component records the number of primality tests. 

### `p`

 Total input-dependent prime selection. The small-input branch explicitly
returns 3. On `GoodInput`, Bertrand's theorem proves that the finite scan
succeeds, so its fallback value is not used. 

### `primeScan_calls_le`

 A bound on the number of primality tests, not a claim of unit bit cost. 
