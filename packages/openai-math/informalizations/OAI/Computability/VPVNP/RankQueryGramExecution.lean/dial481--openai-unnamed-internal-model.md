---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rectangular rank on a streamed relation matrix

From the binary row and column dimensions the machine constructs both scan
bounds. It invokes the concrete Schur, weighted Gram, and field arithmetic
controls. The remaining matrix-specific operation is a bounded read of one
scalar entry. A single time budget and a separate stack-height budget cover
every row prefix satisfying the same numerical size bound.


### `gramWidth`

 Sufficient binary width for the decision trees of both the Schur
interpreter and the outer degree scan. 

### `queryAllowance`

 A root clock that depends on the common bit bound for the entire matrix
and therefore applies to each smaller prefix. 

### `gramTime`

 Uniform step bound for the streamed Gram rank routine with a common `d`-bit size bound. It
charges initialization and up to `(2^d + 1)^2` coefficient queries and cursor checks using
the entry-read time bound `B`. 

### `gramSpace`

 Every prefix may reuse the same storage. The cap of the individual
entry reader enters this expression independently of its clock. 

### `gramRank`

 An entry-point shared by all matrix shapes and every width. 

### `rawGram`

 The input includes the two matrix dimensions, the field advice and the
entry reader's own state. The Schur-depth stack starts empty. 

### `gramRank_bounded`

 The rank of a streamed rectangular matrix is in cursor register one on
return. Both displayed resource bounds are uniform over all row counts up
to `N`; the instruction table depends only on the supplied entry routine. 
