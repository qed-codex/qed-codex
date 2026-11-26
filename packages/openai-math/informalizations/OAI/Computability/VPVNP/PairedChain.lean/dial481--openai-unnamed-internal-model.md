---
{
  "module": "OAI/Computability/VPVNP/PairedChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedChain.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairedChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two contractions of the primed chain

Equation (9.2) uses consecutive pairs of groups of length `2^h` pairs.
Each pair has two complete processor groups. Even cuts are shared with
neighboring pairs; its odd cut and all communication sends in its two groups
are private to that pair. The four header bits on a site contain its group's
actual one-based number, the advice, and the incident cut bits. This numbering
is independent of the live group which later simulates the pair.


### `lengths`

 The pair's exterior cuts are `2i` and `2i+2` and its interior cut is
`2i+1`, using a zero-based pair index `i`. 

### `groupIndex`

 The `H+1`-bit literal encoding of the primed group's own one-based number. 

### `headers`

 The fixed literal and exterior fields supplied to both groups of a pair.
The full bit string at a site is built by `PrimedInputRAM.input`. 

### `PairBits`

 A Boolean assignment to the internal wires of the paired-chain instance at the specified
chain index and RAM parameters. 

### `siteInput`

 Full literal-and-wire input of a primed site. Communication bits are
summed even when they do not form a valid RAM transcript. 

### `original`

 The integer contraction (9.2), with the shared bit assignments indexed
by the even cuts and the independent internal bits of every pair. 

### `primed`

 The formal joint polynomial of equations (9.3) and (9.5), leaving the
integer production labels as variables until the contraction is evaluated. 

### `primed_eq_original`

 Equation (9.3) for the paper's actual bit sharing, `Uₙ`, and `Bₓ`.
Equation (8.1) at each site replaces a grammar query by the path count of
the very same input string. 
