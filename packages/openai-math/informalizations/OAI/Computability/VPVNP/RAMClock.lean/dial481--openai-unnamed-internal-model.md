---
{
  "module": "OAI/Computability/VPVNP/RAMClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The word-step exponent for parsimonious RAM transcripts

The site loop can charge a linear scan of the private-write log at each
instruction. The sorting term pays for every offset at every comparator
layer. Since the word width and the stage counts are polylogarithmic, their
constants and powers fit the slack in the exponent of Lemma 10.1.


### `eventually_polylog_le`

 A fixed polynomial in the logarithm fits within the input length,
with a threshold independent of every private computation or message. 

### `eventually_word_stage_le`

 The logarithmic number of address bits and the prescribed quartic word
width simultaneously fit the bounds used below. `r ≤ B(log₂ n+1)` includes
the rounded address format of the live and virtual RAMs. 

### `transcriptWorkBound`

 An upper envelope in primitive word steps. Here `stages` is the number
of bitonic phases, `H` the bucket capacity, and `k` a fixed program constant.
Each of the `4H` slots is visited at each sorting layer. 

### `transcriptWorkBound_le_clock`

 The envelope with private fuel `n^u` is within the paper's site clock.
The threshold on the fixed program constant and the polylogarithmic
parameters can be taken before choosing the messages. 

### `eventually_transcriptWorkBound_le_clock`

 With `S=2^d`, `H=2^e`, a logarithmic site identifier and
`H ≤ 2n`, the site-clock estimate holds eventually and uniformly over all
permitted choices of the parameters. 
