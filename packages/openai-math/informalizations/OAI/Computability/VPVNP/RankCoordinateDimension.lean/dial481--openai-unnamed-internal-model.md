---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateDimension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateDimension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateDimension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite register routines for slice dimension and basis-index queries

The dimension in Appendix D is the difference between the rank of the full
matrix and the rank of its equation prefix. To locate a basis monomial, add the
prefix rank to its ordinal, scan the original matrix for that greedy row, then
remove the equation-row offset. The arithmetic runs on binary registers.
The rank and prefix scans are returning calls in the same physical stack bank.


### `RegisterBank`

 The binary ISA ports inside a larger bank. The other ports can hold the
caller's query or advice and have the same contents after register writeback. 

### `registerCall`

 Install a fixed instruction sequence at the caller's actual register ports. 

### `registerClock`

 Bound the cost of a binary-register program by its instruction count and the word-width
arithmetic cost. 

### `arithmeticClock`

 A binary operation stages its two operands before changing the destination.
Both instructions of the subtraction implementation are covered by this bound. 

### `dimensionMachine`

 The caller provides the two matrix rank routines. Their selected result
registers remain available until the final subtraction. 

### `dimensionMachine_runs`

 The two completed rank calls and the compiled word operation compute the
dimension. All other registers after the final operation equal their values
at the return of the full-rank call. 

### `combinedOrdinal`

 Ordinal of the same selected monomial among all independent rows. 

### `suffixMachine`

 The scan reads `offset` and returns the original zero-based row in `found`.
The prefix length lives in a register, so the same finite control serves every length. 

### `suffixMachine_runs`

 Correctness for an actual returning prefix scan. Its row result is the
greedy index of the offset ordinal in the combined matrix. Rank and scan
scratch registers may change inside their calls. 

### `suffixGreedy_runs`

 Instantiate the suffix query with the finite prefix-scan controller. The
test and increment subroutines run on the current candidate. No call to select
an earlier basis index occurs in the scan. 
