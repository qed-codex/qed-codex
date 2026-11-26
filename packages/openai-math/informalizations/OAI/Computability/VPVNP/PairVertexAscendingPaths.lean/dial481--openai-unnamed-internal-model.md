---
{
  "module": "OAI/Computability/VPVNP/PairVertexAscendingPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexAscendingPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexAscendingPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ascending calls of the final vertex worker

Each physical vertex ordinal consumes one occurrence tape and adds the occurrence's
exponents to the external histogram. A final empty call checks the exhausted ordinal.
This fold retains the actual reports and excludes incomplete or overlong call lists.


### `IndexedSites`

 Occurrence types, tapes and dense exponent coordinates in physical site order. 

### `IndexedSites.Choice`

 The type of local computation choices at each final site ordinal. 

### `IndexedSites.encode`

 Encode a choice at one site as the part of the choice tape consumed by that vertex. 

### `IndexedSites.powers`

 Histogram exponents contributed by a site's choice, indexed by the common parameter
  labels. 

### `ActiveCalls`

 Native facts for one active ordinal on the fixed arc assignment. The frame
carries the descriptor words and the invariant needed for the next call. 

### `closingReport`

 Report produced by the equal-ordinal branch, including its header read. 

### `Closes`

 The native sentinel's unique tape and report at the specified call clock. 

### `template_closes`

 The assembled worker's bootstrap supplies the closing call at every fuel ≥ 15. 

### `IndexedSites.calls`

 All site tapes in order, followed by the mandatory exhausted call. 

### `IndexedSites.finalMemory`

 External memory after all active ordinals. 

### `ascending_reports`

 The native report list has one active call per site and the exact final
header report. Its external effect is the sum of the selected exponent vectors. 

### `ascendingEquiv`

 A bijection with the accepted native tapes at a fixed shared arc assignment. 

### `closingReport_checks`

 The only exhausted-call read is header field seven, and the clock charge is fifteen. 

### `ascending_report_checks`

 Reads and clock bounds on the encoded site calls hold on every closed native
source path, including its exhausted call. The report list is the computed one. 

### `siteOrdinals`

 Index the actual monomial occurrences and their readers by the worker's ordinals. 

### `sitePathsEquiv`

 Visit the monomial choices in physical ordinal order and close the actual vertex template. 

### `sitePaths_histogram`

 Read back a selected histogram from the source worker's own event log. 
