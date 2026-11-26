---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualPairCanonicalScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairCanonicalScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairCanonicalScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Payload coordinates and vertex counters of a virtual pair

Index the semantic shared-bit choices by a zero-based scan. Its payload
equivalence can be composed with the physical shared-bit worker at the
address computed for a selected descriptor branch. The native readback uses
the actual address. The ordinal emission and each vertex's increments use
the same payload and site witnesses through this reindexing.


### `CanonicalScan`

 Data for scanning one nominated virtual pair in a fixed model. It bounds the leaf startup
clock and final wire width and supplies the term workers' inputs for each possible sequence
of selected passes. 

### `CanonicalScan.inputs`

 Term-worker inputs for the selected compressor execution at its RAM word width, indexed
  recursively by the originating pass and all subsequent choices. 

### `CanonicalScan.encoding`

 Trace encoding of the nominated pair's algebraic occurrences using the final-bit scanner
started at cursor zero in zero memory and the clocked nomination leaf readers. 

### `CanonicalScan.emission`

 Injectively re-encode a canonical scan's selector phases as native term tapes in motif
order, carrying along the same shared-arc and vertex phases. 

### `CanonicalScan.arc`

 Shared-arc scan phase on the terminal network of the selected compression branch, using the
final-bit machine and its zero starting cursor. 

### `CanonicalScan.leafSites`

 Clocked parsers for the initial cursor-network sites, using the nominated auxiliary
machine, its reset memory and the selected model's label values. 

### `selectedChain`

 Chain of compression terms along the chosen execution branch, using the templates' record
data for those passes. 

### `CanonicalScan.sites`

 Final-network site parsers obtained by carrying the nomination leaf parsers through the
chosen chain with that branch's local parsers. 

### `CanonicalScan.ordinals`

 Bijection between a descriptor branch with its terminal arc and site choices and the
ordinal phase lists emitted by the canonical scan. 

### `CanonicalScan.jobSums`

 For every real per-level pointer assignment, the sum of the selected
preorder jobs at all sites is the exponent of the recovered occurrence. 

### `CanonicalScan.siteTotals`

 Sum of increments to one model-label counter over the preorder jobs of one terminal site,
using the supplied row pointers and leaf addresses. 

### `CanonicalScan.flush`

 All real site deposits, in the site's physical order, give the precise
canonical counter memory required by the pair source-run certificate. 
