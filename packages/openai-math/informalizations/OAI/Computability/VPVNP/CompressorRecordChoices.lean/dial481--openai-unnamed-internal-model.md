---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordChoices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordChoices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordChoices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the outer compressor term choices

In the second shrinking scan of Appendix E, and in the corresponding port-block
scan, the term index consists of one integer per supply edge. The reader checks
each binary word against the payload cap and tests the quadratic energy of the
result. Its successful streams are in bijection with the outer indices of
Theorem 6.1. The readers compose in motif order and along branch-dependent
compression passes.


### `ChoiceReader`

 A prefix parser with exactly one code per output. The untouched suffix can
contain the choices of all later motifs and compression levels. 

### `ChoiceReader.encode`

 Boolean word encoding an individual choice so that the reader can consume it as a prefix. 

### `ChoiceReader.read`

 Decode the next choice and return its unconsumed suffix, or fail when the stream has no
  valid choice prefix. 

### `completeEquiv`

 Successful complete transcripts carry exactly one admitted choice each. 

### `single`

 A deterministic choice takes no bits. 

### `reindex`

 Keep the same concrete reader under a change of indices. 

### `sigma`

 Read the first choice before looking up the next reader. This preserves
multiplicity when two first choices lead to identical continuation data. 

### `restrict`

 Reject a candidate which fails the deterministic admission test. 

### `vector`

 Read a finite ordered list of motifs. Each motif can have its own set of
terms and its own number of supply coordinates. 

### `bounded`

 One checked machine-word candidate. 

### `outerCap`

 The bound on each coordinate checked before the quadratic admission test. 

### `coordinateBits`

 With zero repetitions every payload is forced to zero and no choice bit is used. 

### `outerReader`

 The concrete binary reader for exactly the terms of the fixed conversion.
The numbering of the supply edges is chosen once for the motif. 

### `read_outer_iff`

 A successful read consumes just the specified edge order, including the
leading zero bits of each word. Rejection can occur after the cap check or
after the total energy test. 

### `zero_outerIndices`

 A motif with zero-width demands has the zero vector as its sole outer index. 

### `zero_entry_value`

 At zero demand the sole term's local map multiplies an empty list of
parameters. This proves its unit value independently of the parameter ring. 

### `outerCap_bits_le`

 For a fixed motif the required word width is logarithmic in the maximum
demand width. The cap itself is computed by the same fixed integer formula
used in the reader. 

### `motifPassReader`

 One complete ordered pass over the motifs, as in the shrinking and
degree-refresh scans. Demand widths may vary independently from motif to motif. 

### `passReaders`

 At each compression pass, the complete next set of motifs can depend on
the earlier layout and widths. A pass reader consumes just its own prefix. 

### `execution`

 The complete descriptor-phase reader on a branch-dependent sequence of
compression passes. Its output is the existing compressor's term sequence. 
